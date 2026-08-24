/** Token acquisition for Hub-issued, audience-bound AgentDrive tokens. */

export interface AccessToken {
    value: string;
    /** Expiration time as Unix seconds. */
    expiresAt?: number;
}

export interface TokenProvider {
    readonly refreshable: boolean;
    getToken(forceRefresh?: boolean): Promise<AccessToken | string>;
}

export class TokenProviderError extends Error {
    override name = 'TokenProviderError';

    constructor(message: string, readonly cause?: unknown) {
        super(message);
    }
}

export class StaticTokenProvider implements TokenProvider {
    readonly refreshable = false;
    private readonly token: AccessToken;

    constructor(token: AccessToken | string) {
        this.token = coerceToken(token);
    }

    async getToken(_forceRefresh = false): Promise<AccessToken> {
        if (!this.token.value) throw new TokenProviderError('access token must not be empty');
        return this.token;
    }
}

export class CallableTokenProvider implements TokenProvider {
    readonly refreshable = true;
    private readonly callback: (forceRefresh: boolean) => Promise<AccessToken | string> | AccessToken | string;

    constructor(callback: (forceRefresh: boolean) => Promise<AccessToken | string> | AccessToken | string) {
        this.callback = callback;
    }

    async getToken(forceRefresh = false): Promise<AccessToken> {
        return coerceToken(await this.callback(forceRefresh));
    }
}

export interface OAuthClientCredentialsOptions {
    tokenEndpoint: string;
    clientId: string;
    clientSecret: string;
    resource?: string;
    scopes?: string[];
    expirySkewSeconds?: number;
    fetchApi?: typeof fetch;
}

/** Lazy client-credentials renewal. Refresh tokens are never retained. */
export class OAuthClientCredentialsProvider implements TokenProvider {
    readonly refreshable = true;
    private readonly options: Required<Pick<OAuthClientCredentialsOptions, 'resource' | 'scopes' | 'expirySkewSeconds'>> & OAuthClientCredentialsOptions;
    private cached?: AccessToken;
    private pending?: Promise<AccessToken>;

    constructor(options: OAuthClientCredentialsOptions) {
        const url = new URL(options.tokenEndpoint);
        if (!['http:', 'https:'].includes(url.protocol)) throw new Error('tokenEndpoint must be an absolute HTTP(S) URL');
        if (!options.clientId || !options.clientSecret) throw new Error('clientId and clientSecret are required');
        if (options.expirySkewSeconds != null && (!Number.isFinite(options.expirySkewSeconds) || options.expirySkewSeconds < 0)) {
            throw new Error('expirySkewSeconds must be a non-negative number');
        }
        this.options = {
            ...options,
            resource: options.resource ?? 'https://drive.tokencanopy.com',
            scopes: options.scopes ?? [],
            expirySkewSeconds: options.expirySkewSeconds ?? 60,
        };
    }

    async getToken(forceRefresh = false): Promise<AccessToken> {
        if (!forceRefresh && this.cached?.value && this.usable(this.cached)) return this.cached;
        // A pending renewal is the JavaScript equivalent of the provider lock:
        // all concurrent callers share exactly one token request.
        if (this.pending) return this.pending;
        const pending = this.fetchToken();
        this.pending = pending;
        try {
            const token = await pending;
            this.cached = token;
            return token;
        } finally {
            if (this.pending === pending) this.pending = undefined;
        }
    }

    private usable(token: AccessToken): boolean {
        return token.expiresAt == null || token.expiresAt - Date.now() / 1000 > this.options.expirySkewSeconds;
    }

    private async fetchToken(): Promise<AccessToken> {
        const form = new URLSearchParams({ grant_type: 'client_credentials', resource: this.options.resource });
        if (this.options.scopes.length) form.set('scope', this.options.scopes.join(' '));
        const fetchApi = this.options.fetchApi ?? fetch;
        let response: Response;
        try {
            response = await fetchApi(this.options.tokenEndpoint, {
                method: 'POST',
                headers: {
                    Authorization: `Basic ${encodeBasic(`${this.options.clientId}:${this.options.clientSecret}`)}`,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Accept: 'application/json',
                },
                body: form,
                credentials: 'omit',
            });
        } catch (error) {
            throw new TokenProviderError('token request failed', error);
        }
        const payload = await response.json().catch(() => ({} as Record<string, unknown>)) as Record<string, unknown>;
        if (!response.ok) throw new TokenProviderError(String(payload.error_description ?? `token request failed with HTTP ${response.status}`));
        const value = payload.access_token;
        if (typeof value !== 'string' || !value) throw new TokenProviderError('token response did not include access_token');
        const expiresIn = payload.expires_in;
        const lifetime = expiresIn == null ? undefined : Number(expiresIn);
        if (lifetime != null && (!Number.isFinite(lifetime) || lifetime <= 0)) throw new TokenProviderError('token response included invalid expires_in');
        return { value, expiresAt: lifetime == null ? undefined : Date.now() / 1000 + lifetime };
    }
}

function coerceToken(value: AccessToken | string): AccessToken {
    if (typeof value === 'string') {
        if (!value) throw new TypeError('token provider must not return an empty token');
        return { value };
    }
    if (value && typeof value.value === 'string' && value.value) return value;
    throw new TypeError('token provider must return a string or AccessToken');
}

function encodeBasic(value: string): string {
    const bytes = new TextEncoder().encode(value);
    let binary = '';
    for (const byte of bytes) binary += String.fromCharCode(byte);
    return btoa(binary);
}
