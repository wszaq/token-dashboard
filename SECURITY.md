# Security policy

## Supported version

Security fixes apply to the current `main` branch.
No older release branch has a separate support commitment.

## Local data

Keep the default loopback bind address, `127.0.0.1`.
The HTTP server has no authentication or TLS.
The SQLite cache contains private prompt text and tool arguments.
Do not publish databases, transcripts, or screenshots of private sessions.
See [accuracy and privacy](docs/accuracy-and-privacy.md) for the limits.

## Report a vulnerability

Use [GitHub private vulnerability reporting](https://github.com/wszaq/token-dashboard/security/advisories/new) if it is available.
Do not report secret values or private transcripts in a public issue.
If private reporting is unavailable, open an issue that requests a private contact channel.
Include no vulnerability details until the maintainer supplies that channel.

Use synthetic input in a reproduction. Include the affected commit, system, Python version, and expected behavior.
The maintainer will confirm the report and review a fix. The maintainer does not guarantee a response time.
