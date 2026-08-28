const assert = require('node:assert/strict');
const test = require('node:test');

const {
    AgentDriveClient,
    CallableTokenProvider,
    InvalidPathError,
    OAuthClientCredentialsProvider,
    PreconditionFailedError,
    StaticTokenProvider,
    cursorItems,
    cursorPages,
    fetchDownloadTarget,
    joinRelativePath,
    normalizeRelativePath,
    strongIfMatch,
} = require('../dist/index.js');

function jsonResponse(status, body, headers = {}) {
    return new Response(JSON.stringify(body), {
        status,
        headers: { 'content-type': 'application/json', ...headers },
    });
}

function syntheticDrive() {
    return {
        id: 'drv_synthetic',
        name: 'Synthetic drive',
        root_folder_id: 'fld_synthetic_root',
        revision: 'rev_1',
        state: 'active',
        metadata: {},
        created_at: '2026-01-01T00:00:00Z',
        updated_at: '2026-01-01T00:00:00Z',
    };
}

test('strict path helpers reject traversal, absolute paths, and silent sanitization', () => {
    assert.equal(normalizeRelativePath('notes/readme.md'), 'notes/readme.md');
    assert.equal(joinRelativePath('notes', 'readme.md'), 'notes/readme.md');
    for (const value of ['/etc/passwd', '../secret', 'notes//readme.md', 'notes\\readme.md', `notes/${String.fromCharCode(0)}secret`]) {
        assert.throws(() => normalizeRelativePath(value), InvalidPathError);
    }
    assert.throws(() => joinRelativePath('/notes', 'readme.md'), InvalidPathError);
});

test('strongIfMatch accepts one strong revision and rejects wildcard or compound tags', () => {
    assert.equal(strongIfMatch('rev_7'), '"rev_7"');
    assert.equal(strongIfMatch('"rev_7"'), '"rev_7"');
    for (const value of ['', '*', 'W/"rev_7"', '"rev_7", "rev_8"', '"unterminated']) {
        assert.throws(() => strongIfMatch(value));
    }
});

test('mutation retries reuse one idempotency key', async () => {
    const keys = [];
    let attempts = 0;
    const fetchApi = async (_url, init) => {
        keys.push(new Headers(init.headers).get('idempotency-key'));
        attempts += 1;
        return attempts === 1
            ? jsonResponse(503, { error: { code: 'SERVICE_UNAVAILABLE', message: 'synthetic outage' } })
            : jsonResponse(201, syntheticDrive());
    };
    const client = new AgentDriveClient({
        tokenProvider: new StaticTokenProvider('synthetic-token'),
        fetchApi,
        retryPolicy: { maxAttempts: 2, backoffMs: 0, maxBackoffMs: 0 },
    });

    const drive = await client.drives.create('Synthetic drive');

    assert.equal(drive.id, 'drv_synthetic');
    assert.equal(keys.length, 2);
    assert.ok(keys[0]);
    assert.equal(keys[0], keys[1]);
});

test('update helpers preserve explicit null for metadata clearing', async () => {
    let request;
    const client = new AgentDriveClient({
        tokenProvider: new StaticTokenProvider('synthetic-token'),
        fetchApi: async (_url, init) => {
            request = { headers: new Headers(init.headers), body: JSON.parse(init.body) };
            return jsonResponse(200, syntheticDrive());
        },
    });

    await client.drives.update('drv_synthetic', 'rev_1', {
        metadata: null,
        idempotencyKey: 'idem_synthetic_clear',
    });

    assert.deepEqual(request.body, { metadata: null });
    assert.equal(request.headers.get('if-match'), '"rev_1"');
    assert.equal(request.headers.get('idempotency-key'), 'idem_synthetic_clear');
});

test('a refreshable provider renews once after a 401', async () => {
    let current = 'expired-synthetic-token';
    const refreshFlags = [];
    const provider = new CallableTokenProvider((forceRefresh) => {
        refreshFlags.push(forceRefresh);
        if (forceRefresh) current = 'fresh-synthetic-token';
        return current;
    });
    const authorizations = [];
    const fetchApi = async (_url, init) => {
        const authorization = new Headers(init.headers).get('authorization');
        authorizations.push(authorization);
        return authorization === 'Bearer expired-synthetic-token'
            ? jsonResponse(401, { error: { code: 'UNAUTHORIZED', message: 'expired' } })
            : jsonResponse(200, { items: [syntheticDrive()], next_cursor: null });
    };
    const client = new AgentDriveClient({
        tokenProvider: provider,
        fetchApi,
        retryPolicy: { maxAttempts: 2, backoffMs: 0, maxBackoffMs: 0 },
    });

    const page = await client.drives.list();

    assert.equal(page.items.length, 1);
    assert.deepEqual(authorizations, ['Bearer expired-synthetic-token', 'Bearer fresh-synthetic-token']);
    assert.deepEqual(refreshFlags, [false, true, false]);
});

test('client-credentials provider coalesces renewal and sends the AgentDrive resource', async () => {
    const calls = [];
    const provider = new OAuthClientCredentialsProvider({
        tokenEndpoint: 'https://identity.example.com/oauth/token',
        clientId: 'synthetic-client',
        clientSecret: 'synthetic-secret',
        scopes: ['drive.read', 'drive.write'],
        fetchApi: async (url, init) => {
            calls.push({ url: String(url), init, body: new URLSearchParams(init.body) });
            await Promise.resolve();
            return jsonResponse(200, { access_token: `synthetic-access-${calls.length}`, expires_in: 3600 });
        },
    });

    const [first, concurrent] = await Promise.all([provider.getToken(), provider.getToken()]);
    const cached = await provider.getToken();

    assert.equal(calls.length, 1);
    assert.equal(first.value, 'synthetic-access-1');
    assert.equal(concurrent.value, first.value);
    assert.equal(cached.value, first.value);
    assert.equal(calls[0].url, 'https://identity.example.com/oauth/token');
    assert.equal(calls[0].body.get('grant_type'), 'client_credentials');
    assert.equal(calls[0].body.get('resource'), 'https://drive.tokencanopy.com');
    assert.equal(calls[0].body.get('scope'), 'drive.read drive.write');
    assert.equal(calls[0].init.credentials, 'omit');

    const refreshed = await provider.getToken(true);
    assert.equal(refreshed.value, 'synthetic-access-2');
    assert.equal(calls.length, 2);
});

test('download uses a capability and never forwards AgentDrive credentials', async () => {
    const apiHeaders = [];
    const transferCalls = [];
    const fetchApi = async (_url, init) => {
        apiHeaders.push(new Headers(init.headers));
        return jsonResponse(200, {
            download: {
                artifact_id: 'art_synthetic',
                version_id: 'ver_synthetic',
                expires_at: '2026-01-01T00:05:00Z',
                target: {
                    method: 'GET',
                    url: 'https://objects.example.com/synthetic-object',
                    required_headers: { 'x-synthetic-generation': '1' },
                    content_disposition: 'attachment; filename="synthetic.txt"',
                },
            },
        });
    };
    const transferFetchApi = async (url, init) => {
        transferCalls.push({ url: String(url), init, headers: new Headers(init.headers) });
        return new Response(new Blob(['synthetic bytes'], { type: 'text/plain' }), { status: 200 });
    };
    const client = new AgentDriveClient({
        tokenProvider: new StaticTokenProvider('synthetic-agentdrive-token'),
        fetchApi,
        transferFetchApi,
    });

    const content = await client.artifacts.download('drv_synthetic', 'art_synthetic');

    assert.equal(await content.text(), 'synthetic bytes');
    assert.equal(apiHeaders[0].get('authorization'), 'Bearer synthetic-agentdrive-token');
    assert.equal(transferCalls.length, 1);
    assert.equal(transferCalls[0].headers.get('authorization'), null);
    assert.equal(transferCalls[0].headers.get('cookie'), null);
    assert.equal(transferCalls[0].headers.get('x-synthetic-generation'), '1');
    assert.equal(transferCalls[0].init.credentials, 'omit');
});

test('download target rejects credential-bearing required headers', async () => {
    let called = false;
    await assert.rejects(
        fetchDownloadTarget({
            method: 'GET',
            url: 'https://objects.example.com/synthetic-object',
            contentDisposition: 'attachment',
            requiredHeaders: { Authorization: 'Bearer must-not-forward' },
        }, async () => {
            called = true;
            return new Response('unexpected');
        }),
        /forbidden header/i,
    );
    assert.equal(called, false);
});

test('response errors map to typed AgentDrive errors with request metadata', async () => {
    const client = new AgentDriveClient({
        tokenProvider: new StaticTokenProvider('synthetic-token'),
        fetchApi: async () => jsonResponse(
            412,
            { error: { code: 'STALE_REVISION', message: 'synthetic stale revision', details: { expected: 'rev_2' } } },
            { 'x-request-id': 'req_synthetic' },
        ),
        retryPolicy: { maxAttempts: 1 },
    });

    await assert.rejects(
        client.drives.delete('drv_synthetic', 'rev_1', 'idem_synthetic'),
        (error) => error instanceof PreconditionFailedError
            && error.code === 'STALE_REVISION'
            && error.requestId === 'req_synthetic',
    );
});

test('cursor iteration preserves opaque cursors and respects maxPages', async () => {
    const seen = [];
    const pages = cursorPages(async (cursor) => {
        seen.push(cursor);
        if (cursor == null) return { items: ['one'], nextCursor: 'opaque:two' };
        return { items: ['two'], nextCursor: 'opaque:three' };
    }, { maxPages: 2 });

    const values = [];
    for await (const value of cursorItems(pages)) values.push(value);

    assert.deepEqual(seen, [undefined, 'opaque:two']);
    assert.deepEqual(values, ['one', 'two']);
});

function syntheticUpload(extra = {}) {
    return {
        id: 'upld_synthetic',
        drive_id: 'drv_synthetic',
        state: 'active',
        target: { kind: 'artifact', parent_folder_id: 'fld_synthetic_root', name: 'book.xlsx' },
        content: {
            size_bytes: 5381,
            media_type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            checksum: { algorithm: 'crc32c', value: 'AAAAAA==' },
        },
        expires_at: '2026-01-01T04:00:00Z',
        target_disclosed: true,
        restart_required: false,
        result: null,
        failure: null,
        cleanup: { state: 'none' },
        ...extra,
    };
}

const SYNTHETIC_TRANSFER = {
    chunk_protocol: 'gcs-xml-resumable',
    initiation: { url: 'https://storage.invalid/synthetic-resumable-target', method: 'POST', headers: {} },
    chunks: { method: 'PUT', headers: {}, min_bytes: 262144 },
};

function uploadClient(status, body) {
    return new AgentDriveClient({
        baseUrl: 'https://drive.invalid',
        tokenProvider: new StaticTokenProvider('synthetic'),
        fetchApi: async () => jsonResponse(status, body),
    });
}

const BEGIN_REQUEST = {
    target: { kind: 'artifact', parentFolderId: 'fld_synthetic_root', name: 'book.xlsx' },
    content: {
        sizeBytes: 5381,
        mediaType: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        checksum: { algorithm: 'crc32c', value: 'AAAAAA==' },
    },
};

// The 201 is the ONLY response that ever carries the signed upload target, and
// the service discloses it exactly once -- a dropped `transfer` is not a
// degraded result, it is an unrecoverable one. The generated client picks a
// single deserializer per operation and chose the 200's `UploadSessionOut`,
// which has no `transfer` field, so every fresh begin silently lost the URL
// and direct upload could not work at all.
test('begin surfaces the one-time transfer target from a 201', async () => {
    const client = uploadClient(201, { upload: syntheticUpload({ transfer: SYNTHETIC_TRANSFER }) });
    const result = await client.uploads.begin('drv_synthetic', BEGIN_REQUEST);
    assert.equal(
        result.upload.transfer.initiation.url,
        'https://storage.invalid/synthetic-resumable-target',
    );
    assert.equal(result.upload.transfer.chunkProtocol, 'gcs-xml-resumable');
});

// The idempotent replay deliberately cannot carry the target: server-side
// `UploadSessionOut` is documented as "structurally incapable" of it. Parsing a
// 200 with the 201's model would invent a field the wire never sent.
test('begin does not invent a transfer target on a 200 replay', async () => {
    const client = uploadClient(200, { upload: syntheticUpload({ restart_required: true }) });
    const result = await client.uploads.begin('drv_synthetic', BEGIN_REQUEST);
    assert.equal(result.upload.transfer, undefined);
    assert.equal(result.upload.id, 'upld_synthetic');
});
