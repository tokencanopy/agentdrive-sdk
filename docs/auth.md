# AgentDrive Authentication

> Note: This document is authored in-repo and is no longer synced from an external website.

AgentDrive supports two authentication paths:

## 1. Agents and Humans (MCP)

Agents and interactive users connect via the remote Model Context Protocol (MCP) endpoint:

```
https://drive.mcp.tokencanopy.com/mcp
```

- Authentication uses OAuth 2.1 with PKCE (Proof Key for Code Exchange).
- No API key to paste: the MCP client handles the flow automatically on first tool use.
- Authorization server: `https://auth.tokencanopy.com/oidc`. Its metadata is at
  `https://auth.tokencanopy.com/oidc/.well-known/oauth-authorization-server`.
- Dynamic client registration (DCR) endpoint: `https://auth.tokencanopy.com/oidc/reg`.
  OAuth Client ID Metadata Documents (CIMD) are also supported; clients that
  support both let the server decide. Your MCP client performs this for you —
  there is nothing to register by hand.

## 2. Server-to-Server (REST API)

Server-to-server REST callers present a Bearer token in the HTTP `Authorization` header against the REST API base URL:

```
https://drive.tokencanopy.com
```

Header format:
```http
Authorization: Bearer <token>
```

- Machine credentials for server-to-server REST use are issued from the Token
  Canopy console at `https://app.tokencanopy.com`, are audience-bound to
  `https://drive.tokencanopy.com`, and carry only the scopes granted to them.
  An MCP session token is a different audience and is not a valid REST token.
