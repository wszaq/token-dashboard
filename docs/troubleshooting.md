# Troubleshooting

## Python command is missing

Check `python3 --version`. On Windows, try `py -3 --version`.
Install Python if neither command works.
Run all examples from the repository root.

## No data appears

Run `python3 cli.py scan`.
Check that the transcript root contains session `.jsonl` files.
Set `--projects-dir` if Claude Code stores them elsewhere.
Cloud-only sessions cannot appear without local transcripts.

## Port 8080 is busy

Stop your previous dashboard process if it owns the port.
Otherwise, select another port. See the [configuration reference](reference.md#environment-variables).

## Totals appear stale

Run a scan. Confirm that the dashboard and terminal command use the same database path.
`--no-scan` skips only the startup scan.

If you need a rebuild, stop every dashboard process first.
Rename the cache to retain a backup. A new scan creates a fresh database.

A rebuild resets saved plan settings and tip dismissals.
Protect the backup because it contains private data.

## The database is locked

Run one dashboard process per database.
Stop other processes that write to that database.
Use a separate `--db` path for a separate dataset.

## Costs differ from bills

The pricing table supplies estimates. Subscription charges use a different billing model.
Unknown models can have no price. Prompt costs cover only cache-read tokens.
See [accuracy and privacy](accuracy-and-privacy.md).

## Skill tokens are blank

The catalog scans only three local roots.
Project-local or dispatched skills can show invocation counts without text-size estimates.
See [known limitations](KNOWN_LIMITATIONS.md).

## Report a bug

Include your operating system, Python version, command, and a synthetic reproduction.
Do not include real prompts, transcripts, or databases.
For security issues, use [SECURITY.md](../SECURITY.md).
