import { FetchError, RequiredError, ResponseError } from '../generated/runtime';

export class AgentDriveError extends Error {
    readonly statusCode?: number;
    readonly code?: string;
    readonly details?: unknown;
    readonly headers: Record<string, string>;
    readonly operation?: string;
    readonly requestId?: string;
    readonly cause?: unknown;

    constructor(message: string, options: { statusCode?: number; code?: string; details?: unknown; headers?: Record<string, string>; operation?: string; cause?: unknown } = {}) {
        super(message);
        this.name = 'AgentDriveError';
        this.statusCode = options.statusCode;
        this.code = options.code;
        this.details = options.details;
        this.headers = options.headers ?? {};
        this.operation = options.operation;
        this.requestId = this.headers['x-request-id'];
        this.cause = options.cause;
    }
}

export class InvalidRequestError extends AgentDriveError { override name = 'InvalidRequestError'; }
export class AuthenticationError extends AgentDriveError { override name = 'AuthenticationError'; }
export class PermissionDeniedError extends AgentDriveError { override name = 'PermissionDeniedError'; }
export class NotFoundError extends AgentDriveError { override name = 'NotFoundError'; }
export class ConflictError extends AgentDriveError { override name = 'ConflictError'; }
export class PreconditionRequiredError extends AgentDriveError { override name = 'PreconditionRequiredError'; }
export class PreconditionFailedError extends AgentDriveError { override name = 'PreconditionFailedError'; }
export class RateLimitError extends AgentDriveError { override name = 'RateLimitError'; }
export class TransferError extends AgentDriveError { override name = 'TransferError'; }
export class ValidationError extends AgentDriveError { override name = 'ValidationError'; }
export class ServiceUnavailableError extends AgentDriveError { override name = 'ServiceUnavailableError'; }
export class NetworkError extends AgentDriveError { override name = 'NetworkError'; }

export async function typedError(error: unknown, operation?: string): Promise<AgentDriveError> {
    if (error instanceof AgentDriveError) return error;
    if (error instanceof RequiredError) {
        return new InvalidRequestError(error.message, {
            code: 'INVALID_REQUEST',
            details: { field: error.field },
            operation,
            cause: error,
        });
    }
    if (error instanceof ResponseError) {
        const response = error.response;
        const headers: Record<string, string> = {};
        response.headers.forEach((value, key) => { headers[key.toLowerCase()] = value; });
        const payload = await response.clone().json().catch(() => undefined) as Record<string, unknown> | undefined;
        const envelope = payload?.error && typeof payload.error === 'object'
            ? payload.error as Record<string, unknown>
            : {};
        const status = response.status;
        const code = typeof envelope.code === 'string' ? envelope.code : fallbackCode(status);
        const message = typeof envelope.message === 'string' ? envelope.message : `AgentDrive request failed with HTTP ${status}`;
        const Ctor = errorType(status, code);
        return new Ctor(message, {
            statusCode: status,
            code,
            details: envelope.details,
            headers,
            operation,
            cause: error,
        });
    }
    if (error instanceof FetchError) return new NetworkError(error.message, { operation, cause: error });
    if (error instanceof Error) return new AgentDriveError(error.message, { operation, cause: error });
    return new AgentDriveError(String(error), { operation, cause: error });
}

function errorType(status: number, code?: string): typeof AgentDriveError {
    if (status === 400) return InvalidRequestError;
    if (status === 401) return AuthenticationError;
    if (status === 403) return PermissionDeniedError;
    if (status === 404) return NotFoundError;
    if (status === 409) return ConflictError;
    if (status === 412 || code === 'PRECONDITION_FAILED' || code === 'STALE_REVISION') return PreconditionFailedError;
    if (status === 428 || code === 'PRECONDITION_REQUIRED') return PreconditionRequiredError;
    if (status === 429) return RateLimitError;
    if ([406, 413, 415].includes(status) || ['TRANSFER_LIMIT_EXCEEDED', 'TRANSFER_DISABLED', 'NOT_ACCEPTABLE'].includes(code ?? '')) return TransferError;
    if (status === 422) return ValidationError;
    if ([502, 503, 504].includes(status)) return ServiceUnavailableError;
    return AgentDriveError;
}

function fallbackCode(status: number): string | undefined {
    return ({ 400: 'INVALID_REQUEST', 401: 'UNAUTHORIZED', 403: 'PERMISSION_DENIED', 404: 'NOT_FOUND', 409: 'CONFLICT', 412: 'PRECONDITION_FAILED', 422: 'VALIDATION_ERROR', 428: 'PRECONDITION_REQUIRED', 429: 'RATE_LIMITED', 503: 'SERVICE_UNAVAILABLE' } as Record<number, string>)[status];
}
