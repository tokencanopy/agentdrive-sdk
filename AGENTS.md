# AgentDrive SDKs — agent guide

This repository contains the **generated REST client libraries** for AgentDrive, and nothing else.

- To call the AgentDrive REST API from code, install one of the SDKs — see [`README.md`](README.md).
- To let an agent *use* AgentDrive as a tool, you want the MCP server, not these SDKs. The plugin, the `agentdrive` skill, per-agent setup instructions, and the MCP Registry connector all live in **[tokencanopy/agentdrive-plugin](https://github.com/tokencanopy/agentdrive-plugin)**.

## The API

- REST base: `https://drive.tokencanopy.com` (contract version `v0`)
- MCP endpoint: `https://drive.mcp.tokencanopy.com/mcp`

These are **different audiences and are not interchangeable**. A token minted for the MCP endpoint is not a valid REST token, and vice versa.

The authoritative contract is [`sdk/openapi.json`](sdk/openapi.json) in this repo. Generate from it rather than hand-copying endpoint shapes; [`docs/api.md`](docs/api.md) enumerates the operations it declares.

## Working in this repo

The SDKs are generated, not hand-written. Do not edit files under `sdk/python/`, `sdk/typescript/`, or `sdk/go/` directly — change the contract or the generation tooling in `scripts/` and regenerate. See [`docs/sdk-generation.md`](docs/sdk-generation.md).
