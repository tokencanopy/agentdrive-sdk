export interface Page<T> {
    items: readonly T[];
    nextCursor?: string | null;
    raw?: unknown;
}

export async function* cursorPages<T>(
    loader: (cursor?: string) => Promise<Page<T>>,
    options: { cursor?: string; maxPages?: number } = {},
): AsyncGenerator<Page<T>, void, undefined> {
    if (options.maxPages != null && (!Number.isInteger(options.maxPages) || options.maxPages < 1)) {
        throw new RangeError('maxPages must be a positive integer');
    }
    let cursor = options.cursor;
    let pages = 0;
    const seen = new Set<string>();
    if (cursor != null) seen.add(cursor);
    while (options.maxPages == null || pages < options.maxPages) {
        const page = await loader(cursor);
        yield page;
        pages += 1;
        if (!page.nextCursor) return;
        if (seen.has(page.nextCursor)) throw new Error('cursor pagination returned a repeated cursor');
        seen.add(page.nextCursor);
        cursor = page.nextCursor;
    }
}

export async function* cursorItems<T>(pages: AsyncIterable<Page<T>>): AsyncGenerator<T, void, undefined> {
    for await (const page of pages) yield* page.items;
}
