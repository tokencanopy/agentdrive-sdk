"""Public AgentDrive SDK.

The OpenAPI-generated low-level client remains available from
``agentdrive_sdk.generated`` (and through the compatibility exports below).
New callers should use :class:`AgentDriveClient` and its resource helpers.
"""

from __future__ import annotations

import sys

from .generated import *  # noqa: F401,F403
from .generated import __all__ as _generated_all
from . import generated as _generated_package
from .auth import (
    AccessToken,
    CallableTokenProvider,
    OAuthClientCredentialsProvider,
    StaticTokenProvider,
    TokenProvider,
    TokenProviderError,
)
from .client import AgentDriveClient, AsyncAgentDriveClient, RetryPolicy
from .errors import (
    AgentDriveError,
    AuthenticationError,
    ConflictError,
    InvalidRequestError,
    NetworkError,
    NotFoundError,
    PermissionDeniedError,
    PreconditionFailedError,
    PreconditionRequiredError,
    RateLimitError,
    ServiceUnavailableError,
    TransferError,
    ValidationError,
)
from .iteration import CursorItems, CursorPages, Page
from .paths import InvalidPathError, normalize_relative_path, split_parent_path

# Keep the import paths emitted by the first generated release working while
# the real implementation lives below the generated namespace.  The aliases
# are installed after generated imports so generated modules never depend on
# the handwritten package.
sys.modules.setdefault(__name__ + ".api", _generated_package.api)
sys.modules.setdefault(__name__ + ".models", _generated_package.models)
for _module_name, _module in tuple(sys.modules.items()):
    if _module_name.startswith(__name__ + ".generated.api"):
        sys.modules.setdefault(
            __name__ + _module_name[len(__name__ + ".generated") :], _module
        )
    if _module_name.startswith(__name__ + ".generated.models"):
        sys.modules.setdefault(
            __name__ + _module_name[len(__name__ + ".generated") :], _module
        )

__all__ = list(_generated_all) + [
    "AccessToken",
    "AgentDriveClient",
    "AsyncAgentDriveClient",
    "CallableTokenProvider",
    "OAuthClientCredentialsProvider",
    "RetryPolicy",
    "StaticTokenProvider",
    "TokenProvider",
    "TokenProviderError",
    "AgentDriveError",
    "InvalidRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "ConflictError",
    "NotFoundError",
    "PreconditionFailedError",
    "PreconditionRequiredError",
    "RateLimitError",
    "ServiceUnavailableError",
    "TransferError",
    "ValidationError",
    "NetworkError",
    "CursorItems",
    "CursorPages",
    "Page",
    "InvalidPathError",
    "normalize_relative_path",
    "split_parent_path",
]

__version__ = "0.0.2"
