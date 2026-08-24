"""Typed facade errors with the raw generated response retained."""

from __future__ import annotations

import json
from typing import Any, NoReturn

from .generated.exceptions import ApiException as GeneratedApiException


class AgentDriveError(Exception):
    """Base error for an unsuccessful AgentDrive operation."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        code: str | None = None,
        details: Any = None,
        headers: Any = None,
        operation: str | None = None,
        request_id: str | None = None,
        cause: BaseException | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.code = code
        self.details = details
        self.headers = dict(headers or {})
        self.operation = operation
        self.request_id = request_id or self.headers.get("x-request-id")
        self.cause = cause

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(message={self.message!r}, "
            f"status_code={self.status_code!r}, code={self.code!r})"
        )


class InvalidRequestError(AgentDriveError):
    pass


class AuthenticationError(AgentDriveError):
    pass


class PermissionDeniedError(AgentDriveError):
    pass


class NotFoundError(AgentDriveError):
    pass


class ConflictError(AgentDriveError):
    pass


class PreconditionRequiredError(AgentDriveError):
    pass


class PreconditionFailedError(AgentDriveError):
    pass


class RateLimitError(AgentDriveError):
    pass


class TransferError(AgentDriveError):
    pass


class ValidationError(AgentDriveError):
    pass


class ServiceUnavailableError(AgentDriveError):
    pass


class NetworkError(AgentDriveError):
    pass


def raise_typed_error(
    exc: BaseException,
    *,
    operation: str | None = None,
) -> NoReturn:
    """Translate a generated exception without hiding its response context."""

    if not isinstance(exc, GeneratedApiException):
        if isinstance(exc, AgentDriveError):
            raise exc
        raise NetworkError(str(exc) or type(exc).__name__, operation=operation, cause=exc) from exc

    payload = _payload(exc)
    error = payload.get("error") if isinstance(payload, dict) else None
    error = error if isinstance(error, dict) else {}
    status = _as_int(exc.status)
    code = _as_str(error.get("code")) or _fallback_code(status)
    message = _as_str(error.get("message")) or _reason(exc) or "AgentDrive request failed"
    details = error.get("details")
    if details is None and isinstance(error, dict):
        details = {key: value for key, value in error.items() if key not in {"code", "message"}}
        if not details:
            details = None
    error_type = _type_for(status, code)
    raise error_type(
        message,
        status_code=status,
        code=code,
        details=details,
        headers=exc.headers,
        operation=operation,
        cause=exc,
    ) from exc


def _type_for(status: int | None, code: str | None) -> type[AgentDriveError]:
    if status == 400:
        return InvalidRequestError
    if status == 401:
        return AuthenticationError
    if status == 403:
        return PermissionDeniedError
    if status == 404:
        return NotFoundError
    if status == 409:
        return ConflictError
    if status == 412 or code in {"PRECONDITION_FAILED", "STALE_REVISION"}:
        return PreconditionFailedError
    if status == 428 or code == "PRECONDITION_REQUIRED":
        return PreconditionRequiredError
    if status == 429:
        return RateLimitError
    if status in {413, 415, 406} or code in {
        "TRANSFER_LIMIT_EXCEEDED",
        "TRANSFER_DISABLED",
        "NOT_ACCEPTABLE",
    }:
        return TransferError
    if status in {502, 503, 504}:
        return ServiceUnavailableError
    if status == 422:
        return ValidationError
    return AgentDriveError


def _payload(exc: GeneratedApiException) -> Any:
    data = getattr(exc, "data", None)
    if data is not None:
        if hasattr(data, "to_dict"):
            try:
                return data.to_dict()
            except Exception:  # pragma: no cover - defensive for generated models
                pass
        if isinstance(data, dict):
            return data
    body = getattr(exc, "body", None)
    if isinstance(body, bytes):
        body = body.decode("utf-8", errors="replace")
    if isinstance(body, str) and body:
        try:
            decoded = json.loads(body)
        except json.JSONDecodeError:
            return {}
        return decoded
    return {}


def _reason(exc: GeneratedApiException) -> str | None:
    reason = getattr(exc, "reason", None)
    return reason if isinstance(reason, str) else None


def _as_int(value: Any) -> int | None:
    return value if isinstance(value, int) else None


def _as_str(value: Any) -> str | None:
    return value if isinstance(value, str) else None


def _fallback_code(status: int | None) -> str | None:
    return {
        400: "INVALID_REQUEST",
        401: "UNAUTHORIZED",
        403: "PERMISSION_DENIED",
        404: "NOT_FOUND",
        409: "CONFLICT",
        412: "PRECONDITION_FAILED",
        422: "VALIDATION_ERROR",
        428: "PRECONDITION_REQUIRED",
        429: "RATE_LIMITED",
        503: "SERVICE_UNAVAILABLE",
    }.get(status)
