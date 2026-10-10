# Accuracy, privacy, and architecture

## Data flow

```text
Local Claude Code transcripts -> scanner -> SQLite cache
SQLite cache -> local HTTP API -> browser dashboard
Local skill files -> catalog -> Skills tab
pricing.json -> cost estimates
```

The scanner reads transcripts. It does not change them.
It tracks file offsets and modification times for incremental scans.
It deduplicates assistant snapshots by session and message identifier.
Duplicate snapshots no longer inflate totals.
It does not prove that totals equal an Anthropic invoice.

## What the database contains

The cache contains user prompt text, session identifiers, timestamps, model names, and token counts.
It also stores tool arguments and selected file paths or command targets.
The dashboard does not retain a complete copy of every assistant response or tool result.
Tool-result sizes use a character-based token estimate. They are not exact billed tokens.
Treat both the original transcripts and the cache as private data.

## Cost estimates

The server reads rates from the bundled `pricing.json` at startup.
Rates can become outdated. Verify them before financial use.

Unknown model identifiers use an Opus, Sonnet, or Haiku fallback if the name contains that tier.
Other unknown models have no cost estimate. The Overview cost omits these models.
A low displayed total can therefore exclude usage.

The subscription selection supplies a plan label and monthly reference price.
The displayed cost remains an API-equivalent estimate.
The Prompts route estimates cost from cache-read tokens only. It is not a complete per-prompt bill.
Skill text sizes estimate catalog content, not measured per-invocation token usage.

## Privacy boundary

The default server binds to `127.0.0.1`.
The runtime serves JavaScript, CSS, and charts locally. It does not send transcript data to an external service.
There is no built-in telemetry. Git clone and other installation tools use the network separately.

The server has no authentication, TLS, or access controls for remote clients.
If you change `HOST`, other clients can read the API and change plan or tip settings.
Do not expose it through a public proxy or shared network.
Local applications with access to the port can also read the API.
Backups, browser extensions, screenshots, and manual exports are outside this privacy boundary.
