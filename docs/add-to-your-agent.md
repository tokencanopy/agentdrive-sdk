# Add AgentDrive to your agent

AgentDrive is a **remote MCP server** — one HTTPS endpoint, OAuth 2.1 (PKCE + dynamic client registration). The same endpoint works across every MCP client:

```
https://api.agentdrive.run/mcp
```

On first connect you'll be sent through an OAuth sign-in; after that the agent has access to your drive. No API key to paste for the OAuth flow.

---

## Claude (Desktop / web)

1. **Settings → Connectors → Add custom connector**
2. Name: `AgentDrive`
3. URL: `https://api.agentdrive.run/mcp`
4. Sign in when prompted.

## Claude Code (CLI)

**Recommended — the plugin** (wires the MCP *and* installs the `agentdrive` skill + `/publish`, `/drive`, `/compile`):

```bash
claude plugin marketplace add Mnexa-AI/agentdrive-sdk
claude plugin install agentdrive@agentdrive
```

**MCP only** (no skill/commands):

```bash
claude mcp add --transport http agentdrive https://api.agentdrive.run/mcp
```

Either way, Claude Code opens the OAuth flow on first tool use — no API key to paste.

## ChatGPT

Requires **Developer Mode** (Plus / Pro / Team / Enterprise).

1. **Settings → Apps & Connectors → Advanced → Developer Mode** (toggle on)
2. **Add new connector**
3. Name: `AgentDrive` · MCP Server URL: `https://api.agentdrive.run/mcp`
4. Authentication: **OAuth** → "I trust this application."

ChatGPT supports remote (HTTPS) MCP servers only — which is exactly what AgentDrive is.

## Codex (CLI)

Codex supports remote streamable-HTTP MCP servers with OAuth.

```bash
codex mcp add        # choose streamable HTTP, url = https://api.agentdrive.run/mcp, auth = OAuth
codex mcp login agentdrive
```

Or edit `~/.codex/config.toml`:

```toml
[mcp_servers.agentdrive]
url = "https://api.agentdrive.run/mcp"
# optional: bind tokens to the resource (RFC 8707)
# oauth_resource = "https://api.agentdrive.run/mcp"
```

then `codex mcp login agentdrive`.

## Gemini CLI

Add to your Gemini CLI `settings.json`:

```json
{
  "mcpServers": {
    "agentdrive": {
      "httpUrl": "https://api.agentdrive.run/mcp"
    }
  }
}
```

Gemini CLI supports OAuth 2.0 for remote MCP servers. (Note: the consumer Gemini app only supports a curated set of partner connectors today — the CLI, the Gemini SDK, and Gemini Enterprise are the self-serve paths.)

---

## API key alternative (non-OAuth clients / scripts)

For headless use you can authenticate with an API key instead of OAuth — pass it as a bearer token:

```bash
curl -H "Authorization: Bearer ad_live_..." https://drive.tokencanopy.com/v0/...
```

See [`auth.md`](auth.md) and [`api.md`](api.md) for the full auth model.
