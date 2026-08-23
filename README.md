# AgentDrive — SDKs, Skills & Connector

Official developer kit for [**AgentDrive**](https://agentdrive.run) — an artifact store for AI agents. Read, write, and search files by path; share by rendered URL.

AgentDrive is a **remote MCP server** with OAuth 2.1 (PKCE + dynamic client registration). The v0 REST data plane is hosted at `https://drive.tokencanopy.com`; this repo holds the **client-side** pieces: language SDKs, the agent Skill, and connector metadata. No server source lives here.

> Listed in the official MCP Registry as [`run.agentdrive/agentdrive`](https://registry.modelcontextprotocol.io/v0.1/servers?search=run.agentdrive/agentdrive).

## Install the plugin

The plugin wires the AgentDrive MCP **and** installs the `agentdrive` skill + `/publish`, `/drive`, `/compile`. One command detects your agents (Claude Code, Codex, Cursor) and installs to each:

```bash
npx plugins add Mnexa-AI/agentdrive-sdk
```

Or per agent:

```bash
# Claude Code
claude plugin marketplace add Mnexa-AI/agentdrive-sdk && claude plugin install agentdrive@agentdrive

# Codex
codex plugin marketplace add Mnexa-AI/agentdrive-sdk

# Cursor
/add-plugin agentdrive
```

First tool use opens the OAuth sign-in — no API key to paste.

## Connect (MCP only — no plugin)

For agents without a plugin system, add the remote MCP directly:

| Agent | How |
|---|---|
| **Claude** (Desktop/web) | Settings → Connectors → Add custom connector → `https://api.agentdrive.run/mcp` |
| **ChatGPT** | Settings → Apps & Connectors → Developer Mode → Add connector → `https://api.agentdrive.run/mcp` (OAuth) |
| **Codex** | `codex mcp add` (streamable HTTP) → `codex mcp login agentdrive` |
| **Gemini CLI** | Add to `settings.json` under `mcpServers` |
| **Claude Code** | `claude mcp add --transport http agentdrive https://api.agentdrive.run/mcp` |

Full paste-ready blocks: [`docs/add-to-your-agent.md`](docs/add-to-your-agent.md). Cross-agent instructions: [`AGENTS.md`](AGENTS.md).

## What's in this repo

| Path | Contents |
|---|---|
| [`plugin/`](plugin/) | The **Claude Code plugin** — wires the MCP + bundles the skill + `/publish` `/drive` `/compile`. Installed via the `marketplace.json` at the repo root. |
| [`sdk/`](sdk/) | REST SDKs for **Python**, **TypeScript**, and **Go**, generated from AgentDrive's committed contract |
| [`skills/`](skills/) | The `agentdrive` agent Skill (synced from the production service) |
| [`connector/`](connector/) | `server.json` (MCP registry manifest), connector icon, `llms.txt` |
| [`docs/`](docs/) | Connect-your-agent guide, plus mirrored `setup.md` / `auth.md` / `api.md` |
| [`AGENTS.md`](AGENTS.md) | Cross-agent usage guide (Codex, Cursor, Copilot, Windsurf, Zed read this natively) |

## SDKs

Generated reproducibly from the reviewed AgentDrive contract via pinned
[OpenAPI Generator](https://openapi-generator.tech/). See
[`sdk/README.md`](sdk/README.md).

```bash
# Python  (once published)
pip install agentdrive-sdk

# TypeScript / Node  (once published)
npm install @mnexa-ai/agentdrive-sdk

# Go
go get github.com/Mnexa-AI/agentdrive-sdk/sdk/go
```

> The bare `agentdrive` package on PyPI is the [stdio MCP companion](https://pypi.org/project/agentdrive/); the REST SDK ships as `agentdrive-sdk`.

## Links

- Website: https://agentdrive.run
- API base: https://drive.tokencanopy.com · OpenAPI: https://drive.tokencanopy.com/openapi.json
- Docs: [setup](https://agentdrive.run/setup.md) · [auth](https://agentdrive.run/auth.md) · [api](https://agentdrive.run/api.md) · [skill](https://agentdrive.run/agentdrive.md)

## License

[MIT](LICENSE) © Mnexa AI
