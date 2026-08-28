import type {
    ArtifactOut,
    ChangePageOut,
    DriveListOut,
    DriveOut,
    EntriesInner,
    EntryListOut,
    FolderOut,
    GrantCreateIn,
    GrantListOut,
    GrantOut,
    GrantUpdateIn,
    LookupOut,
    SearchPageOut,
    ShareCreateIn,
    ShareCreateOut,
    ShareListOut,
    ShareOut,
    UploadBeginOut,
    UploadSessionOut,
    UploadsCreateRequest,
    VersionListOut,
    VersionOut,
} from '../generated/models';
import { UploadBeginOutFromJSON, UploadSessionOutFromJSON } from '../generated/models';
import type { ChangesListRequest } from '../generated/apis/ChangesApi';
import type { DriveSearchRequest } from '../generated/apis/SearchApi';
import type { AgentDriveClient } from './client';
import { fetchDownloadTarget, newIdempotencyKey, strongIfMatch } from './client';
import { TransferError } from './errors';
import { cursorItems, cursorPages, Page } from './iteration';
import { normalizeEntryName, normalizeRelativePath, splitParentPath } from './paths';

export interface PageOptions {
    limit?: number;
    cursor?: string;
    maxPages?: number;
}

export type SearchOptions = PageOptions & {
    mode?: DriveSearchRequest['mode'];
    parentId?: string;
    contentType?: string;
    label?: string;
    updatedAfter?: Date;
    updatedBefore?: Date;
};

export type ChangeOptions = PageOptions & {
    start?: ChangesListRequest['start'];
    type?: string;
};

type EntryListOptions = {
    parentId?: string;
    type?: string;
    name?: string;
    label?: string;
    contentType?: string;
    updatedAfter?: Date;
    updatedBefore?: Date;
    state?: string;
};

export class DriveResource {
    constructor(private readonly client: AgentDriveClient) {}

    list(options: PageOptions & { lifecycle?: string } = {}): Promise<DriveListOut> {
        return this.client.invoke('drives_list', () => this.client.generated.drives.drivesList({ lifecycle: options.lifecycle ?? 'active', limit: options.limit, cursor: options.cursor }));
    }

    iterPages(options: PageOptions & { lifecycle?: string } = {}): AsyncGenerator<Page<DriveOut>, void, undefined> {
        return cursorPages(async (cursor) => {
            const response = await this.list({ ...options, cursor });
            return { items: response.items, nextCursor: response.nextCursor, raw: response };
        }, options);
    }

    iterItems(options: PageOptions & { lifecycle?: string } = {}): AsyncGenerator<DriveOut, void, undefined> {
        return cursorItems(this.iterPages(options));
    }

    get(driveId: string, ifNoneMatch?: string): Promise<DriveOut> {
        return this.client.invoke('drives_read', () => this.client.generated.drives.drivesRead({ driveId, ifNoneMatch }));
    }

    create(name: string, options: { metadata?: Record<string, unknown>; idempotencyKey?: string } = {}): Promise<DriveOut> {
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('drives_create', () => this.client.generated.drives.drivesCreate({
            idempotencyKey,
            driveCreateIn: { name, metadata: options.metadata },
        }));
    }

    update(driveId: string, revision: string, options: { name?: string; metadata?: Record<string, unknown> | null; idempotencyKey?: string } = {}): Promise<DriveOut> {
        if (options.name == null && !hasOwn(options, 'metadata')) throw new Error('provide name or metadata');
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('drives_update', () => this.client.generated.drives.drivesUpdate({
            driveId,
            ifMatch: strongIfMatch(revision),
            idempotencyKey,
            driveUpdateIn: { name: options.name, metadata: options.metadata },
        }));
    }

    delete(driveId: string, revision: string, idempotencyKey?: string): Promise<DriveOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('drives_delete', () => this.client.generated.drives.drivesDelete({ driveId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }

    restore(driveId: string, revision: string, idempotencyKey?: string): Promise<DriveOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('drives_restore', () => this.client.generated.drives.drivesRestore({ driveId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }

    usage(driveId: string) {
        return this.client.invoke('drives_usage', () => this.client.generated.drives.drivesUsage({ driveId }));
    }
}

export class EntryResource {
    constructor(private readonly client: AgentDriveClient) {}

    async list(driveId: string, options: { parentId?: string; type?: string; name?: string; label?: string; contentType?: string; updatedAfter?: Date; updatedBefore?: Date; state?: string; limit?: number; cursor?: string } = {}): Promise<EntryListOut> {
        const parentId = options.parentId ?? (await this.client.drives.get(driveId)).rootFolderId;
        return this.client.invoke('entries_list', () => this.client.generated.navigation.entriesList({ driveId, parentId, type: options.type, name: options.name, label: options.label, contentType: options.contentType, updatedAfter: options.updatedAfter, updatedBefore: options.updatedBefore, state: options.state, limit: options.limit, cursor: options.cursor }));
    }

    iterPages(driveId: string, options: EntryListOptions & PageOptions = {}): AsyncGenerator<Page<EntriesInner>, void, undefined> {
        return cursorPages(async (cursor) => {
            const response = await this.list(driveId, { ...options, cursor });
            return { items: response.entries, nextCursor: response.nextCursor, raw: response };
        }, options);
    }

    iterItems(driveId: string, options: EntryListOptions & PageOptions = {}): AsyncGenerator<EntriesInner, void, undefined> {
        return cursorItems(this.iterPages(driveId, options));
    }

    lookup(driveId: string, path: string, type?: string): Promise<LookupOut> {
        return this.client.invoke('lookup', () => this.client.generated.navigation.lookup({ driveId, path: normalizeRelativePath(path), type }));
    }
}

export class FolderResource {
    constructor(private readonly client: AgentDriveClient) {}

    list(driveId: string, options: PageOptions & { lifecycle?: string; parentId?: string; name?: string } = {}) {
        return this.client.invoke('folders_list', () => this.client.generated.folders.foldersList({ driveId, lifecycle: options.lifecycle ?? 'active', limit: options.limit, cursor: options.cursor, parentId: options.parentId, name: options.name }));
    }

    iterPages(driveId: string, options: PageOptions & { lifecycle?: string; parentId?: string; name?: string } = {}): AsyncGenerator<Page<FolderOut>, void, undefined> {
        return cursorPages(async (cursor) => {
            const response = await this.list(driveId, { ...options, cursor });
            return { items: response.items, nextCursor: response.nextCursor, raw: response };
        }, options);
    }

    iterItems(driveId: string, options: PageOptions & { lifecycle?: string; parentId?: string; name?: string } = {}): AsyncGenerator<FolderOut, void, undefined> {
        return cursorItems(this.iterPages(driveId, options));
    }

    get(driveId: string, folderId: string, ifNoneMatch?: string) {
        return this.client.invoke('folders_read', () => this.client.generated.folders.foldersRead({ driveId, folderId, ifNoneMatch }));
    }

    async create(driveId: string, name: string, options: { parentId?: string; parentPath?: string; metadata?: Record<string, unknown>; idempotencyKey?: string } = {}) {
        const parentId = await resolveParent(this.client, driveId, options.parentId, options.parentPath);
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('folders_create', () => this.client.generated.folders.foldersCreate({
            driveId,
            idempotencyKey,
            folderCreateIn: { parentId, name: normalizeEntryName(name), metadata: options.metadata },
        }));
    }

    createPath(driveId: string, path: string, options: { metadata?: Record<string, unknown>; idempotencyKey?: string } = {}) {
        const [parentPath, name] = splitParentPath(path);
        return this.create(driveId, name, { ...options, parentPath: parentPath || undefined });
    }

    async update(driveId: string, folderId: string, revision: string, options: { name?: string; parentId?: string; parentPath?: string; metadata?: Record<string, unknown> | null; idempotencyKey?: string } = {}) {
        if (options.name == null && options.parentId == null && options.parentPath == null && !hasOwn(options, 'metadata')) throw new Error('provide name, parent, or metadata');
        const parentId = options.parentPath == null ? options.parentId : await resolveParent(this.client, driveId, undefined, options.parentPath);
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('folders_update', () => this.client.generated.folders.foldersUpdate({
            driveId,
            folderId,
            ifMatch: strongIfMatch(revision),
            idempotencyKey,
            folderUpdateIn: {
                name: options.name == null ? undefined : normalizeEntryName(options.name),
                parentId,
                metadata: options.metadata,
            },
        }));
    }

    move(driveId: string, folderId: string, revision: string, options: { parentId?: string; parentPath?: string; name?: string; idempotencyKey?: string } = {}) {
        return this.update(driveId, folderId, revision, options);
    }

    delete(driveId: string, folderId: string, revision: string, options: { recursive?: boolean; idempotencyKey?: string } = {}) {
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('folders_delete', () => this.client.generated.folders.foldersDelete({ driveId, folderId, ifMatch: strongIfMatch(revision), recursive: options.recursive, idempotencyKey }));
    }

    restore(driveId: string, folderId: string, revision: string, idempotencyKey?: string) {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('folders_restore', () => this.client.generated.folders.foldersRestore({ driveId, folderId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }

    copy(driveId: string, folderId: string, options: { destinationParentId: string; destinationName: string; destinationDriveId?: string; revision?: string; idempotencyKey?: string }) {
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('folders_copy', () => this.client.generated.folders.foldersCopy({ driveId, folderId, ifMatch: options.revision == null ? undefined : strongIfMatch(options.revision), idempotencyKey, folderCopyIn: { destinationParentId: options.destinationParentId, destinationName: normalizeEntryName(options.destinationName), destinationDriveId: options.destinationDriveId } }));
    }
}

export class ArtifactResource {
    constructor(private readonly client: AgentDriveClient) {}

    list(driveId: string, options: PageOptions & { lifecycle?: string; parentId?: string; name?: string; contentType?: string; label?: string; updatedAfter?: Date; updatedBefore?: Date } = {}) {
        return this.client.invoke('artifacts_list', () => this.client.generated.artifacts.artifactsList({ driveId, lifecycle: options.lifecycle ?? 'active', limit: options.limit, cursor: options.cursor, parentId: options.parentId, name: options.name, contentType: options.contentType, label: options.label, updatedAfter: options.updatedAfter, updatedBefore: options.updatedBefore }));
    }

    iterPages(driveId: string, options: PageOptions & { lifecycle?: string; parentId?: string; name?: string; contentType?: string; label?: string; updatedAfter?: Date; updatedBefore?: Date } = {}): AsyncGenerator<Page<ArtifactOut>, void, undefined> {
        return cursorPages(async (cursor) => {
            const response = await this.list(driveId, { ...options, cursor });
            return { items: response.items, nextCursor: response.nextCursor, raw: response };
        }, options);
    }

    iterItems(driveId: string, options: PageOptions & { lifecycle?: string; parentId?: string; name?: string; contentType?: string; label?: string; updatedAfter?: Date; updatedBefore?: Date } = {}): AsyncGenerator<ArtifactOut, void, undefined> {
        return cursorItems(this.iterPages(driveId, options));
    }

    get(driveId: string, artifactId: string, ifNoneMatch?: string) {
        return this.client.invoke('artifacts_read', () => this.client.generated.artifacts.artifactsRead({ driveId, artifactId, ifNoneMatch }));
    }

    async create(driveId: string, name: string, content: Blob | ArrayBuffer | Uint8Array | string, options: { parentId?: string; parentPath?: string; contentType?: string; metadata?: Record<string, unknown>; sha256?: string; idempotencyKey?: string } = {}) {
        const parentId = await resolveParent(this.client, driveId, options.parentId, options.parentPath);
        const blob = asBlob(content, options.contentType);
        assertInlineSize(blob, this.client.inlineUploadLimit);
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('artifacts_create', () => this.client.generated.artifacts.artifactsCreate({
            driveId,
            idempotencyKey,
            content: blob,
            name: normalizeEntryName(name),
            parentId,
            contentType: options.contentType,
            metadata: options.metadata,
            sha256: options.sha256,
        }));
    }

    uploadBytes(driveId: string, path: string, content: Blob | ArrayBuffer | Uint8Array | string, options: { contentType?: string; metadata?: Record<string, unknown>; idempotencyKey?: string } = {}) {
        const [parentPath, name] = splitParentPath(path);
        return this.create(driveId, name, content, { ...options, parentPath: parentPath || undefined });
    }

    async update(driveId: string, artifactId: string, revision: string, options: { name?: string; parentId?: string; parentPath?: string; metadata?: Record<string, unknown> | null; labels?: string[] | null; idempotencyKey?: string } = {}) {
        if (
            options.name == null
            && options.parentId == null
            && options.parentPath == null
            && !hasOwn(options, 'metadata')
            && !hasOwn(options, 'labels')
        ) throw new Error('provide an artifact field');
        const parentId = options.parentPath == null ? options.parentId : await resolveParent(this.client, driveId, undefined, options.parentPath);
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('artifacts_update', () => this.client.generated.artifacts.artifactsUpdate({
            driveId,
            artifactId,
            ifMatch: strongIfMatch(revision),
            idempotencyKey,
            artifactUpdateIn: {
                name: options.name == null ? undefined : normalizeEntryName(options.name),
                parentId,
                metadata: options.metadata,
                labels: options.labels,
            },
        }));
    }

    move(driveId: string, artifactId: string, revision: string, options: { parentId?: string; parentPath?: string; name?: string; idempotencyKey?: string } = {}) {
        return this.update(driveId, artifactId, revision, options);
    }

    delete(driveId: string, artifactId: string, revision: string, idempotencyKey?: string) {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('artifacts_delete', () => this.client.generated.artifacts.artifactsDelete({ driveId, artifactId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }

    restore(driveId: string, artifactId: string, revision: string, idempotencyKey?: string) {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('artifacts_restore', () => this.client.generated.artifacts.artifactsRestore({ driveId, artifactId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }

    copy(driveId: string, artifactId: string, options: { destinationParentId: string; destinationName: string; destinationDriveId?: string; versionId?: string; revision?: string; idempotencyKey?: string }) {
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('artifacts_copy', () => this.client.generated.artifacts.artifactsCopy({ driveId, artifactId, ifMatch: options.revision == null ? undefined : strongIfMatch(options.revision), idempotencyKey, artifactCopyIn: { destinationParentId: options.destinationParentId, destinationName: normalizeEntryName(options.destinationName), destinationDriveId: options.destinationDriveId, versionId: options.versionId } }));
    }

    async content(driveId: string, artifactId: string, ifNoneMatch?: string): Promise<Blob> {
        return this.client.invoke('artifacts_content', () => this.client.generated.artifacts.artifactsContent({ driveId, artifactId, ifNoneMatch }));
    }

    async download(driveId: string, artifactId: string): Promise<Blob> {
        const capability = await this.client.invoke('download_capabilities_create', () => (
            this.client.generated.downloads.downloadCapabilitiesCreate({
                driveId,
                downloadCapabilitiesCreateRequest: {
                    target: { kind: 'artifact', artifactId },
                },
            })
        ));
        return fetchDownloadTarget(capability.download.target, this.client.transferFetchApi);
    }
}

export class VersionResource {
    constructor(private readonly client: AgentDriveClient) {}

    list(driveId: string, artifactId: string, options: PageOptions = {}): Promise<VersionListOut> {
        return this.client.invoke('versions_list', () => this.client.generated.versions.versionsList({ driveId, artifactId, limit: options.limit, cursor: options.cursor }));
    }

    iterPages(driveId: string, artifactId: string, options: PageOptions = {}): AsyncGenerator<Page<VersionOut>, void, undefined> {
        return cursorPages(async (cursor) => {
            const response = await this.list(driveId, artifactId, { ...options, cursor });
            return { items: response.items, nextCursor: response.nextCursor, raw: response };
        }, options);
    }

    iterItems(driveId: string, artifactId: string, options: PageOptions = {}): AsyncGenerator<VersionOut, void, undefined> {
        return cursorItems(this.iterPages(driveId, artifactId, options));
    }

    get(driveId: string, artifactId: string, versionId: string, ifNoneMatch?: string) {
        return this.client.invoke('versions_read', () => this.client.generated.versions.versionsRead({ driveId, artifactId, versionId, ifNoneMatch }));
    }

    async append(driveId: string, artifactId: string, revision: string, content: Blob | ArrayBuffer | Uint8Array | string, options: { contentType?: string; sha256?: string; idempotencyKey?: string } = {}) {
        const blob = asBlob(content, options.contentType);
        assertInlineSize(blob, this.client.inlineUploadLimit);
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('versions_append', () => this.client.generated.versions.versionsAppend({ driveId, artifactId, ifMatch: strongIfMatch(revision), idempotencyKey, content: blob, contentType: options.contentType, sha256: options.sha256 }));
    }

    restore(driveId: string, artifactId: string, versionId: string, revision: string, idempotencyKey?: string) {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('versions_restore', () => this.client.generated.versions.versionsRestore({ driveId, artifactId, versionId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }

    async content(driveId: string, artifactId: string, versionId: string, ifNoneMatch?: string): Promise<Blob> {
        return this.client.invoke('versions_content', () => this.client.generated.versions.versionsContent({ driveId, artifactId, versionId, ifNoneMatch }));
    }

    async download(driveId: string, artifactId: string, versionId: string): Promise<Blob> {
        const capability = await this.client.invoke('download_capabilities_create', () => (
            this.client.generated.downloads.downloadCapabilitiesCreate({
                driveId,
                downloadCapabilitiesCreateRequest: {
                    target: { kind: 'version', artifactId, versionId },
                },
            })
        ));
        return fetchDownloadTarget(capability.download.target, this.client.transferFetchApi);
    }
}

export class SearchResource {
    constructor(private readonly client: AgentDriveClient) {}

    find(driveId: string, query: string, options: SearchOptions = {}): Promise<SearchPageOut> {
        return this.client.invoke('drive_search', () => this.client.generated.search.driveSearch({ driveId, q: query, mode: options.mode, limit: options.limit, cursor: options.cursor, parentId: options.parentId, contentType: options.contentType, label: options.label, updatedAfter: options.updatedAfter, updatedBefore: options.updatedBefore }));
    }

    iterPages(driveId: string, query: string, options: SearchOptions = {}): AsyncGenerator<Page<SearchPageOut['items'][number]>, void, undefined> {
        return cursorPages(async (cursor) => {
            const response = await this.find(driveId, query, { ...options, cursor });
            return { items: response.items, nextCursor: response.nextCursor, raw: response };
        }, options);
    }

    iterItems(driveId: string, query: string, options: SearchOptions = {}) {
        return cursorItems(this.iterPages(driveId, query, options));
    }
}

export class ChangeResource {
    constructor(private readonly client: AgentDriveClient) {}

    list(driveId: string, options: ChangeOptions = {}): Promise<ChangePageOut> {
        return this.client.invoke('changes_list', () => this.client.generated.changes.changesList({ driveId, limit: options.limit, start: options.start, cursor: options.cursor, type: options.type }));
    }

    iterPages(driveId: string, options: ChangeOptions = {}): AsyncGenerator<Page<ChangePageOut['items'][number]>, void, undefined> {
        return cursorPages(async (cursor) => {
            const response = await this.list(driveId, { ...options, cursor });
            return { items: response.items, nextCursor: response.nextCursor, raw: response };
        }, options);
    }

    iterItems(driveId: string, options: ChangeOptions = {}) {
        return cursorItems(this.iterPages(driveId, options));
    }
}

export class GrantResource {
    constructor(private readonly client: AgentDriveClient) {}

    list(driveId: string, options: PageOptions & { lifecycle?: string; resourceType?: string; resourceId?: string; principalType?: string } = {}): Promise<GrantListOut> {
        return this.client.invoke('grants_list', () => this.client.generated.grants.grantsList({ driveId, lifecycle: options.lifecycle ?? 'active', limit: options.limit, cursor: options.cursor, resourceType: options.resourceType, resourceId: options.resourceId, principalType: options.principalType }));
    }

    iterPages(driveId: string, options: PageOptions & { lifecycle?: string; resourceType?: string; resourceId?: string; principalType?: string } = {}): AsyncGenerator<Page<GrantOut>, void, undefined> {
        return cursorPages(async (cursor) => {
            const response = await this.list(driveId, { ...options, cursor });
            return { items: response.items, nextCursor: response.nextCursor, raw: response };
        }, options);
    }

    iterItems(driveId: string, options: PageOptions & { lifecycle?: string; resourceType?: string; resourceId?: string; principalType?: string } = {}) {
        return cursorItems(this.iterPages(driveId, options));
    }

    create(driveId: string, grantCreateIn: GrantCreateIn, idempotencyKey?: string): Promise<GrantOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('grants_create', () => this.client.generated.grants.grantsCreate({ driveId, idempotencyKey: requestKey, grantCreateIn }));
    }

    get(driveId: string, grantId: string, ifNoneMatch?: string): Promise<GrantOut> {
        return this.client.invoke('grants_read', () => this.client.generated.grants.grantsRead({ driveId, grantId, ifNoneMatch }));
    }

    update(driveId: string, grantId: string, revision: string, grantUpdateIn: GrantUpdateIn, idempotencyKey?: string): Promise<GrantOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('grants_update', () => this.client.generated.grants.grantsUpdate({ driveId, grantId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey, grantUpdateIn }));
    }

    revoke(driveId: string, grantId: string, revision: string, idempotencyKey?: string): Promise<GrantOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('grants_revoke', () => this.client.generated.grants.grantsRevoke({ driveId, grantId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }
}

export class ShareResource {
    constructor(private readonly client: AgentDriveClient) {}

    list(driveId: string, options: PageOptions & { lifecycle?: string; resourceType?: string; resourceId?: string } = {}): Promise<ShareListOut> {
        return this.client.invoke('shares_list', () => this.client.generated.shares.sharesList({ driveId, lifecycle: options.lifecycle ?? 'active', limit: options.limit, cursor: options.cursor, resourceType: options.resourceType, resourceId: options.resourceId }));
    }

    iterPages(driveId: string, options: PageOptions & { lifecycle?: string; resourceType?: string; resourceId?: string } = {}): AsyncGenerator<Page<ShareOut>, void, undefined> {
        return cursorPages(async (cursor) => {
            const response = await this.list(driveId, { ...options, cursor });
            return { items: response.items, nextCursor: response.nextCursor, raw: response };
        }, options);
    }

    iterItems(driveId: string, options: PageOptions & { lifecycle?: string; resourceType?: string; resourceId?: string } = {}) {
        return cursorItems(this.iterPages(driveId, options));
    }

    create(driveId: string, shareCreateIn: ShareCreateIn, idempotencyKey?: string): Promise<ShareCreateOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('shares_create', () => this.client.generated.shares.sharesCreate({ driveId, idempotencyKey: requestKey, shareCreateIn }));
    }

    get(driveId: string, shareId: string, ifNoneMatch?: string): Promise<ShareOut> {
        return this.client.invoke('shares_read', () => this.client.generated.shares.sharesRead({ driveId, shareId, ifNoneMatch }));
    }

    revoke(driveId: string, shareId: string, revision: string, idempotencyKey?: string): Promise<ShareOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('shares_revoke', () => this.client.generated.shares.sharesRevoke({ driveId, shareId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }

    rotate(driveId: string, shareId: string, revision: string, idempotencyKey?: string): Promise<ShareCreateOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('shares_rotate', () => this.client.generated.shares.sharesRotate({ driveId, shareId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }
}

export class UploadResource {
    constructor(private readonly client: AgentDriveClient) {}

    /**
     * Begin an upload session.
     *
     * Deserializes the response HERE, by status, instead of calling the
     * generated `uploadsCreate`. The endpoint has two different success
     * schemas -- 201 is `UploadBeginOut`, which carries the one-time
     * `transfer` target, and 200 is the idempotent replay `UploadSessionOut`,
     * which deliberately cannot carry it. `typescript-fetch` emits a single
     * deserializer per operation and picked the 200 one, so every fresh begin
     * was parsed by a model with no `transfer` field and the signed upload URL
     * was silently dropped. Since the service discloses that target EXACTLY
     * ONCE, the URL was then unrecoverable: re-reading the session only sets
     * `restart_required`. That made direct upload impossible through this SDK.
     *
     * The Python generator emits a per-status `response_types_map` and gets
     * this right, which is why only TypeScript was affected.
     *
     * Not fixed by widening the schemas: `UploadSessionOut` is documented
     * server-side as "structurally incapable of carrying the bearer target",
     * and that property is worth more than the convenience of one return type.
     */
    begin(driveId: string, request: UploadsCreateRequest, options: { revision?: string; idempotencyKey?: string } = {}): Promise<UploadBeginOut | UploadSessionOut> {
        const idempotencyKey = options.idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('uploads_create', async () => {
            const response = await this.client.generated.uploads.uploadsCreateRaw({ driveId, ifMatch: options.revision == null ? undefined : strongIfMatch(options.revision), idempotencyKey, uploadsCreateRequest: request });
            // `value()` would apply the generated (wrong) transformer; the body
            // is still unread here because JSONApiResponse only reads it there.
            const body = await response.raw.json();
            return response.raw.status === 201 ? UploadBeginOutFromJSON(body) : UploadSessionOutFromJSON(body);
        });
    }

    read(driveId: string, uploadId: string, ifNoneMatch?: string): Promise<UploadSessionOut> {
        return this.client.invoke('uploads_read', () => this.client.generated.uploads.uploadsRead({ driveId, uploadId, ifNoneMatch }));
    }

    cancel(driveId: string, uploadId: string, revision: string, idempotencyKey?: string): Promise<UploadSessionOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('uploads_delete', () => this.client.generated.uploads.uploadsDelete({ driveId, uploadId, ifMatch: strongIfMatch(revision), idempotencyKey: requestKey }));
    }

    complete(driveId: string, uploadId: string, idempotencyKey?: string): Promise<UploadSessionOut> {
        const requestKey = idempotencyKey ?? newIdempotencyKey();
        return this.client.invoke('uploads_complete', () => this.client.generated.uploads.uploadsComplete({ driveId, uploadId, idempotencyKey: requestKey }));
    }
}

async function resolveParent(client: AgentDriveClient, driveId: string, parentId?: string, parentPath?: string): Promise<string> {
    if (parentId != null && parentPath != null) throw new Error('provide parentId or parentPath, not both');
    if (parentId != null) return parentId;
    if (parentPath != null) return (await client.entries.lookup(driveId, parentPath, 'folder')).id;
    return (await client.drives.get(driveId)).rootFolderId;
}

function asBlob(content: Blob | ArrayBuffer | Uint8Array | string, contentType?: string): Blob {
    if (content instanceof Blob && contentType == null) return content;
    if (content instanceof Blob) return new Blob([content], { type: contentType });
    if (typeof content === 'string') return new Blob([content], { type: contentType });
    return new Blob([content as unknown as BlobPart], { type: contentType });
}

function assertInlineSize(content: Blob, limit: number): void {
    if (content.size > limit) throw new TransferError(`content is ${content.size} bytes, above the inline upload limit of ${limit} bytes`, { code: 'TRANSFER_LIMIT_EXCEEDED' });
}

function hasOwn(value: object, key: PropertyKey): boolean {
    return Object.prototype.hasOwnProperty.call(value, key);
}
