# AgentDrive — SDKs

Official REST client libraries for [**AgentDrive**](https://tokencanopy.com) — an artifact store for AI agents. Read, write, and search files by path; share by rendered URL.

The v0 REST data plane is hosted at `https://drive.tokencanopy.com`. This repo holds the **generated client libraries only**. No server source lives here.

> **Looking for the plugin, the agent skill, or the MCP connector?**
> They moved to **[tokencanopy/agentdrive-plugin](https://github.com/tokencanopy/agentdrive-plugin)**.

## Install

```bash
# Python
pip install agentdrive-sdk

# TypeScript / Node
npm install @tokencanopy/agentdrive-sdk

# Go
go get github.com/tokencanopy/agentdrive-sdk/sdk/go
```

> The bare `agentdrive` package on PyPI is a separate name-claim placeholder; the REST SDK ships as `agentdrive-sdk`.

## Using AgentDrive from an agent

If you want an agent to *use* AgentDrive rather than call its REST API from code, you want the MCP server, not these SDKs:

```
https://drive.mcp.tokencanopy.com/mcp
```

Streamable HTTP, OAuth 2.1 PKCE, no API key. Per-agent setup for Claude Code, Codex, Cursor, VS Code/Copilot, Windsurf, Gemini CLI and Zed lives in [tokencanopy/agentdrive-plugin](https://github.com/tokencanopy/agentdrive-plugin/blob/main/docs/add-to-your-agent.md).

## What's in this repo

| Path | Contents |
|---|---|
| [`sdk/`](sdk/) | REST SDKs for **Python**, **TypeScript**, and **Go**, generated from AgentDrive's committed contract |
| [`sdk/openapi.json`](sdk/openapi.json) | The pinned v0 contract every client is generated from — the authoritative API reference |
| [`scripts/`](scripts/) | Generation, contract-import, and provenance-check tooling |
| [`docs/`](docs/) | [setup](docs/setup.md) · [auth](docs/auth.md) · [api](docs/api.md) · [sdk-generation](docs/sdk-generation.md) |

## Generation

Clients are generated reproducibly from the reviewed AgentDrive contract via a
pinned [OpenAPI Generator](https://openapi-generator.tech/). See
[`sdk/README.md`](sdk/README.md) and [`docs/sdk-generation.md`](docs/sdk-generation.md).

## Links

- Website: https://tokencanopy.com
- API base: https://drive.tokencanopy.com · OpenAPI: https://drive.tokencanopy.com/openapi.json
- Plugin & MCP connector: https://github.com/tokencanopy/agentdrive-plugin

## License

[MIT](LICENSE) © Mnexa AI
