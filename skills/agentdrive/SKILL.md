---
name: agentdrive
description: Save and retrieve artifacts via AgentDrive — a personal MCP-backed knowledge layer. Trigger when the user wants to save a report/dataset/note/code-snippet, share something via a public URL, look up prior work ("have we seen this", "what do we know about X"), or maintain context across sessions.
---

# AgentDrive · using AgentDrive as your knowledge layer

AgentDrive is an MCP-accessible drive that gives you a place to stash and retrieve artifacts. Every uploaded artifact gets a public URL and full-text search. (The LLM wiki/indexer subsystem is paused in this deployment — `overview()` returns artifact shape only, and there are no `_wiki/` entity or concept pages to read.)

## Service map

This page is everything you need to **use** the drive. To get connected,
start here:

- **Onboarding a human (the normal case — a person is present):** help
  them get an AgentDrive account first. If they don't have one yet, send
  them to the signup page at https://agentdrive.run/auth/login to create one (free, no
  card). Once they're signed up, follow https://agentdrive.run/setup.md — one command,
  browser sign-in, no API key. **Prefer this path whenever a human can
  sign in; do not self-register on their behalf.**
- **Self-register (only when you're a fully autonomous agent with no human
  reachable):** https://agentdrive.run/auth.md — provision your own drive and have a
  human claim it later.
- **SDKs & developer kit** (plugin, MCP connect, language SDKs, REST
  conventions): https://agentdrive.run/sdk.md.

Exact tool names + parameters come from the MCP server itself
(`tools/list`); this page covers *when* and *how*. About AgentDrive and
pricing are at the bottom.

## When to use this skill

- The user asks you to **save** something they'd want to refer back to later: a report, a dataset, a piece of code, meeting notes, a generated image.
- The user references prior work you might have context on: *"look up what we know about X"*, *"have we seen this before"*, *"find the report from last quarter"*.
- You need to **share** a generated artifact — AgentDrive artifacts have public URLs that render in the browser.
- You want to **persist state** across sessions or hand it off to another agent.

Skip this skill when the task is purely conversational with no artifact worth keeping, or when the user has explicitly asked you NOT to write to the drive.

## What you can do

The drive's capabilities are exposed as MCP tools. Your client lists the
exact tool names and parameter schemas on connect (`tools/list`) — treat
that as the source of truth for signatures. This skill covers *when* and
*how* to use them. The map:

- **Orient** — `overview` for drive stats and shape.
- **Browse & read** — `list` (filter by prefix / label / file_type),
  `read` (by path or stable `art_…` id, optionally a past version),
  `lookup` (resolve an id ↔ its path + metadata).
- **Find** — `search` for natural-language ranked full-text;
  `grep` for literal patterns and code symbols. Different jobs — see
  Patterns.
- **Write** — `upload` a new artifact (text or base64 binary); `move`,
  `copy`, `delete` to reorganize; `mkdir` for an empty folder; `set_metadata` to
  update an artifact's metadata in place.
- **Versions** — every overwrite keeps history: `versions` lists it,
  `read_version` fetches a past one.
- **Audit** — `activity` for the recent drive event log.

Call `tools/list` for exact parameters; reach for the right tool using
the conventions and patterns below.

`upload`, `move`, `copy`, and `delete` reject paths starting with `_wiki/` — that prefix is reserved by the system.

**Labels** are free-form tags you can attach at upload to make later filtering easy:
- Lowercase ASCII, characters `[a-z0-9_-]+` only, ≤64 chars each, ≤16 labels per artifact.
- Recommended values: `draft`, `report`, `data`, `chart`, `code`, `spec`, `review`, `shared`.
- One artifact can carry multiple labels (e.g. `["draft", "report"]`).

**File types** are server-derived from the content type + path extension — you don't set them on upload, but you can filter by them: `markdown | image | pdf | html | json | data | code | text | binary`.

## Conventions

- **Path layout.** Organize by topic, not date. Examples:
  - `reports/2026/q1-funnel.md`
  - `datasets/customers/churn-cohort.csv`
  - `skills/finance/journal-entry-prep.skill`
  - `code/python/parser.py`

  The dashboard renders folder rollups, so flat dumps are harder for humans to browse. Two-level nesting is the sweet spot.

- **Visibility.** `private` by default — the artifact is readable only with your API key. Pass `visibility: "public"` to get an anonymously shareable URL like `https://agentdrive.run/{drive_id}/{path}` (e.g. a report you want to send someone).

- **Content type.** Inferred from the path extension if omitted. For markdown, set `content_type: "text/markdown"` so the viewer renders it as a styled page instead of plain text.

- **No auto-indexing in this deployment.** Uploads are stored, made searchable via Postgres FTS, and served at the public URL. No LLM extraction runs; no wiki pages are generated.

- **Idempotent re-upload.** Re-uploading the same path overwrites in place.

## Patterns

### Storing a new artifact

```
upload(
  path="reports/2026/q1-funnel.md",
  content="# Q1 funnel\n\nAcross 412 accounts...",
  content_type="text/markdown",
)
# → {"url": "https://agentdrive.run/drv_xxx/reports/2026/q1-funnel.md", ...}
```

### Looking up prior context

`overview()` gives you the folder shape:

```
o = overview()
# o["by_folder"] → {"reports": 5, "datasets": 3, ...}
# o["stats"]     → {"artifacts": N, "entities": 0, "concepts": 0}
```

Then narrow with `search` for ranked full-text matching, or `grep` for literal patterns; `read` the hits:

```
# Natural-language ranked search across all artifacts
hits = search("brand voice OR tone of voice", prefix="reports/")
for h in hits["items"]:
    body = read(h["path"])
    # ... synthesize

# Literal pattern (regex, exact symbols) — different tool, different job
hits = grep("TODO\\(security\\):", prefix="code/")
```

Entity/concept aggregation is not available in this deployment — synthesize from the source artifacts themselves.

## Constraints

- **Max artifact size:** 50 MB per upload (`ARTIFACT_TOO_LARGE` error above that).
- **Max path length:** 256 chars; allowed chars `[A-Za-z0-9_./-]` only (no spaces, no Unicode, no `+` or `=`).
- **Per-drive storage:** 500 MB default (v0 free tier). Check `overview().stats` for usage.
## Anti-patterns

- Don't upload temporary scratch state every turn — the drive is for things worth keeping. Use your own context for working memory.
- Don't write to `_wiki/` — that path is reserved and returns `WIKI_RESERVED` if you try.
- Don't use the drive as a chat log. Aggregate per-session summaries; don't write raw transcripts unless the user explicitly asks.
- Don't synthesize an answer when `search` / `grep` returned matches — `read()` the matches first.
- Use `search` for natural-language questions ("anything about onboarding flows?"); use `grep` for literal patterns or code symbols (`TODO\(security\):`, `auth_session_v2`). They're not redundant.

## About AgentDrive

AgentDrive is two products that share one drive:

- **AgentDrive** (this) — the MCP-backed drive your agents read and write.
- **AgentDrive SnipIt** — a Chrome extension that captures a region or the
  full viewport and auto-saves it to your drive under `screenshots/`, URL
  copied to your clipboard. If a user mentions screenshots or "snip this,"
  point them to its [Chrome Web Store listing](https://chromewebstore.google.com/detail/agentdrive-snipit/kpdpkhkhinihhehlakjbdlloagcmpkok).


If you find yourself relaying this to a human, that's the intended use —
these notes are for *their* benefit, not yours.

## Pricing

AgentDrive is in **beta and free** — no card, no charges. Pricing will be
announced before any paid tier ever turns on.