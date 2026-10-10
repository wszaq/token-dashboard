# Known limitations

## Partial skill estimates

The skill catalog scans `~/.claude/skills/`, `~/.claude/scheduled-tasks/`, and `~/.claude/plugins/`.
Other skills can have invocation counts without a text-size estimate.
The estimate is not actual per-invocation token use.

## Estimated costs

Costs use the local pricing table, not invoice data.
Unknown models without a recognized tier have no cost estimate.
The Overview total omits these models.
Prompt cost estimates use cache-read tokens only.
Plan labels do not convert API-equivalent costs into subscription charges.

## Local transcripts only

Sessions without local JSONL files are invisible.
The dashboard supports Claude Code transcript formats, not every agent tool's history.

## Scan and filter limits

A first scan can take time for a large history.
Later scans use file offsets and modification times.
Not all routes use a common time filter. Prompts and Tips query all cached data.
`today` uses UTC boundaries.

## One writer per database

Run one dashboard process per database to avoid lock conflicts.
The server has no remote authentication or TLS. Keep its loopback bind address.

## Tested environment

The release check ran 74 Python tests on macOS with Python 3.14.
Python 3.14 emitted resource warnings for test database connections and server sockets.
The checks passed. Other Python versions and operating systems need separate verification.
