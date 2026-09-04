# AgentDrive Setup

> Note: This document is authored in-repo and is no longer synced from an external website.

## Installing the SDKs

The AgentDrive client SDKs are published as:

### TypeScript / Node (npm)
```bash
npm install @tokencanopy/agentdrive-sdk
```

### Python (PyPI)
```bash
pip install agentdrive-sdk
```

### Go
```bash
go get github.com/tokencanopy/agentdrive-sdk/sdk/go
```

## Agent Use via MCP

For agent use, connect directly to the remote MCP endpoint (streamable HTTP, OAuth 2.1 PKCE, no API key required):

```
https://drive.mcp.tokencanopy.com/mcp
```

For configuration guides and paste-ready blocks for Claude, ChatGPT, Codex, Cursor, Gemini, and other agents, see [docs/add-to-your-agent.md](add-to-your-agent.md).
