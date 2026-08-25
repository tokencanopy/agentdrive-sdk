export class InvalidPathError extends Error {
    override name = 'InvalidPathError';
}

export function normalizeRelativePath(path: string): string {
    if (
        typeof path !== 'string'
        || !path
        || path.includes('\0')
        || path.includes('\\')
        || path.startsWith('/')
        || path.endsWith('/')
    ) {
        throw new InvalidPathError('path must use non-empty relative POSIX segments');
    }
    if (/^[A-Za-z]:\//.test(path)) throw new InvalidPathError('path must not be drive-absolute');
    const segments = path.split('/');
    if (segments.some((segment) => !segment || segment === '.' || segment === '..')) {
        throw new InvalidPathError('path contains an empty or dot segment');
    }
    return segments.join('/');
}

export function normalizeEntryName(name: string): string {
    const normalized = normalizeRelativePath(name);
    if (normalized.includes('/')) throw new InvalidPathError('entry name must be one path segment');
    return normalized;
}

export function splitParentPath(path: string): [string, string] {
    const normalized = normalizeRelativePath(path);
    const index = normalized.lastIndexOf('/');
    return index < 0 ? ['', normalized] : [normalized.slice(0, index), normalized.slice(index + 1)];
}

export function joinRelativePath(...parts: string[]): string {
    const normalized = parts.filter((part) => part.length > 0).map(normalizeRelativePath);
    if (!normalized.length) throw new InvalidPathError('at least one path segment is required');
    return normalizeRelativePath(normalized.join('/'));
}

export function looksLikeCredentialFile(path: string): boolean {
    const name = path.split('/').pop()?.toLowerCase() ?? '';
    return ['.env', '.npmrc', '.pypirc', 'id_rsa', 'id_ed25519', 'credentials.json'].includes(name)
        || ['.pem', '.key', '.p12', '.pfx'].some((suffix) => name.endsWith(suffix))
        || (name.startsWith('service-account') && name.endsWith('.json'));
}
