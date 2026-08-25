import {
    ArtifactsApi,
    ChangesApi,
    DownloadsApi,
    DrivesApi,
    FoldersApi,
    GrantsApi,
    NavigationApi,
    SearchApi,
    SharesApi,
    UploadsApi,
    VersionsApi,
} from '../generated/apis';
import { Configuration, ResponseError, type FetchAPI } from '../generated/runtime';
import type { DownloadTargetOut } from '../generated/models';
import { AccessToken, TokenProvider } from './auth';
import { AgentDriveError, AuthenticationError, NetworkError, TransferError, typedError } from './errors';
import { cursorItems, cursorPages, Page } from './iteration';
import { ArtifactResource, ChangeResource, DriveResource, EntryResource, FolderResource, GrantResource, SearchResource, ShareResource, UploadResource, VersionResource } from './resources';

export const CANONICAL_BASE_URL = 'https://drive.tokencanopy.com';

export interface RetryPolicy {
    maxAttempts?: number;
    backoffMs?: number;
    maxBackoffMs?: number;
    retryStatuses?: readonly number[];
}

export interface AgentDriveClientOptions {
    tokenProvider?: TokenProvider;
    baseUrl?: string;
    fetchApi?: FetchAPI;
    /** Fetch implementation used only for signed transfer targets. */
    transferFetchApi?: FetchAPI;
    retryPolicy?: RetryPolicy;
    inlineUploadLimit?: number;
}

export class AgentDriveClient {
    readonly baseUrl: string;
    readonly inlineUploadLimit: number;
    readonly transferFetchApi: FetchAPI;
    readonly generated: {
        artifacts: ArtifactsApi;
        changes: ChangesApi;
        downloads: DownloadsApi;
        drives: DrivesApi;
        folders: FoldersApi;
        grants: GrantsApi;
        navigation: NavigationApi;
        search: SearchApi;
        shares: SharesApi;
        uploads: UploadsApi;
        versions: VersionsApi;
    };
    readonly drives: DriveResource;
    readonly entries: EntryResource;
    readonly folders: FolderResource;
    readonly artifacts: ArtifactResource;
    readonly versions: VersionResource;
    readonly search: SearchResource;
    readonly changes: ChangeResource;
    readonly grants: GrantResource;
    readonly shares: ShareResource;
    readonly uploads: UploadResource;
    private readonly tokenProvider?: TokenProvider;
    private readonly retry: Required<RetryPolicy>;

    constructor(options: AgentDriveClientOptions = {}) {
        this.baseUrl = absoluteOrigin(options.baseUrl ?? CANONICAL_BASE_URL);
        this.inlineUploadLimit = options.inlineUploadLimit ?? 15 * 1024 * 1024;
        this.transferFetchApi = options.transferFetchApi ?? ((input, init) => fetch(input, init));
        if (this.inlineUploadLimit <= 0) throw new Error('inlineUploadLimit must be positive');
        this.tokenProvider = options.tokenProvider;
        this.retry = {
            maxAttempts: options.retryPolicy?.maxAttempts ?? 3,
            backoffMs: options.retryPolicy?.backoffMs ?? 100,
            maxBackoffMs: options.retryPolicy?.maxBackoffMs ?? 1000,
            retryStatuses: options.retryPolicy?.retryStatuses ?? [408, 429, 502, 503, 504],
        };
        if (this.retry.maxAttempts < 1) throw new Error('maxAttempts must be at least 1');
        if (this.retry.backoffMs < 0 || this.retry.maxBackoffMs < 0) throw new Error('retry backoff values must be non-negative');
        const configuration = new Configuration({
            basePath: this.baseUrl,
            fetchApi: options.fetchApi,
            accessToken: this.tokenProvider ? async () => this.accessToken() : undefined,
        });
        this.generated = {
            artifacts: new ArtifactsApi(configuration),
            changes: new ChangesApi(configuration),
            downloads: new DownloadsApi(configuration),
            drives: new DrivesApi(configuration),
            folders: new FoldersApi(configuration),
            grants: new GrantsApi(configuration),
            navigation: new NavigationApi(configuration),
            search: new SearchApi(configuration),
            shares: new SharesApi(configuration),
            uploads: new UploadsApi(configuration),
            versions: new VersionsApi(configuration),
        };
        this.drives = new DriveResource(this);
        this.entries = new EntryResource(this);
        this.folders = new FolderResource(this);
        this.artifacts = new ArtifactResource(this);
        this.versions = new VersionResource(this);
        this.search = new SearchResource(this);
        this.changes = new ChangeResource(this);
        this.grants = new GrantResource(this);
        this.shares = new ShareResource(this);
        this.uploads = new UploadResource(this);
    }

    async accessToken(forceRefresh = false): Promise<string> {
        if (!this.tokenProvider) return '';
        try {
            const token: AccessToken | string = await this.tokenProvider.getToken(forceRefresh);
            const value = typeof token === 'string' ? token : token.value;
            if (!value) throw new Error('token provider returned an empty access token');
            return value;
        } catch (error) {
            if (error instanceof AgentDriveError) throw error;
            throw new AuthenticationError('could not obtain an AgentDrive access token', { code: 'TOKEN_PROVIDER_ERROR', cause: error });
        }
    }

    async invoke<T>(operation: string, fn: () => Promise<T>, options: { retry?: boolean } = {}): Promise<T> {
        const attempts = options.retry === false ? 1 : this.retry.maxAttempts;
        let refreshed = false;
        for (let attempt = 0; attempt < attempts; attempt += 1) {
            try {
                return await fn();
            } catch (error) {
                if (
                    error instanceof ResponseError
                    && error.response.status === 401
                    && !refreshed
                    && this.tokenProvider?.refreshable
                    && attempt + 1 < attempts
                ) {
                    await this.accessToken(true);
                    refreshed = true;
                    continue;
                }
                const status = error instanceof ResponseError ? error.response.status : undefined;
                if (status != null && this.retry.retryStatuses.includes(status) && attempt + 1 < attempts) {
                    await delay(Math.min(this.retry.maxBackoffMs, this.retry.backoffMs * 2 ** attempt));
                    continue;
                }
                const mapped = await typedError(error, operation);
                if (mapped instanceof NetworkError && attempt + 1 < attempts) {
                    await delay(Math.min(this.retry.maxBackoffMs, this.retry.backoffMs * 2 ** attempt));
                    continue;
                }
                throw mapped;
            }
        }
        throw new NetworkError(`AgentDrive ${operation} retry loop exhausted`, { operation });
    }

    pages<T>(loader: (cursor?: string) => Promise<Page<T>>, options?: { cursor?: string; maxPages?: number }): AsyncGenerator<Page<T>, void, undefined> {
        return cursorPages(loader, options);
    }

    items<T>(pages: AsyncIterable<Page<T>>): AsyncGenerator<T, void, undefined> {
        return cursorItems(pages);
    }
}

export function newIdempotencyKey(): string {
    const cryptoObject = globalThis.crypto;
    if (cryptoObject?.randomUUID) return `sdk-${cryptoObject.randomUUID()}`;
    if (!cryptoObject?.getRandomValues) throw new Error('secure randomness is unavailable for idempotency key generation');
    const bytes = cryptoObject.getRandomValues(new Uint8Array(16));
    return `sdk-${Array.from(bytes, (byte) => byte.toString(16).padStart(2, '0')).join('')}`;
}

export function strongIfMatch(revision: string): string {
    const value = revision.trim();
    if (!value || value === '*' || value.startsWith('W/') || /[\u0000-\u001f\u007f,]/.test(value)) {
        throw new Error('If-Match requires one strong revision');
    }
    if (value.startsWith('"') || value.endsWith('"')) {
        if (!/^"[^"\\]+"$/.test(value)) throw new Error('If-Match requires one strong revision');
        return value;
    }
    if (value.includes('"') || value.includes('\\')) throw new Error('If-Match requires one strong revision');
    return `"${value}"`;
}

export function absoluteOrigin(value: string): string {
    const parsed = new URL(value);
    if (
        !['http:', 'https:'].includes(parsed.protocol)
        || parsed.username
        || parsed.password
        || parsed.search
        || parsed.hash
        || (parsed.pathname !== '/' && parsed.pathname !== '')
    ) {
        throw new Error('baseUrl must be an absolute HTTP(S) origin');
    }
    return parsed.origin;
}

export async function fetchDownloadTarget(target: DownloadTargetOut, fetchApi: FetchAPI = fetch): Promise<Blob> {
    const url = new URL(target.url);
    if (!['http:', 'https:'].includes(url.protocol)) throw new TransferError('download target must be HTTP(S)');
    if (target.method !== 'GET') throw new TransferError('download target must use GET');
    const headers = transferHeaders(target.requiredHeaders);
    let response: Response;
    try {
        response = await fetchApi(url.toString(), {
            method: 'GET',
            headers,
            credentials: 'omit',
            redirect: 'error',
            referrerPolicy: 'no-referrer',
        });
    } catch (error) {
        throw new TransferError('download target request failed', { cause: error });
    }
    if (!response.ok) {
        throw new TransferError(`download target returned HTTP ${response.status}`, { statusCode: response.status });
    }
    return response.blob();
}

function transferHeaders(value: object): Record<string, string> {
    if (value == null || typeof value !== 'object' || Array.isArray(value)) {
        throw new TransferError('download target headers must be an object');
    }
    const headers: Record<string, string> = {};
    for (const [name, rawValue] of Object.entries(value)) {
        const lower = name.toLowerCase();
        if (['authorization', 'cookie', 'proxy-authorization'].includes(lower)) {
            throw new TransferError(`download target requested forbidden header: ${name}`);
        }
        if (typeof rawValue !== 'string') throw new TransferError(`download target header ${name} must be a string`);
        headers[name] = rawValue;
    }
    return headers;
}

function delay(milliseconds: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, milliseconds));
}
