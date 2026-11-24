# Token Dashboard

A local dashboard for Claude Code token usage, estimated costs, and session history.

This repository maintains a version of [Nathan Herkelman's Token Dashboard](https://github.com/nateherkai/token-dashboard).
The original MIT copyright remains in [LICENSE](LICENSE).

## What it is

The dashboard reads the local JSONL transcripts that Claude Code writes.
It stores the results in a SQLite database and shows them in a browser.
The backend uses only the Python standard library.
The frontend uses vanilla JavaScript and bundled Apache ECharts. It has no build step.

It shows:

- Token totals and daily charts, with input, output, and cache use.
- Expensive prompts, session details, project comparisons, and tool activity.
- Skill invocation counts and partial estimates for skill text size.
- Rule-based tips for repeated reads, large tool results, and cache use.
- Local pricing settings and live updates after each scan.

Cost figures are estimates from the bundled pricing table. They are not invoices or subscription charges.
Read [accuracy and privacy](docs/accuracy-and-privacy.md) before you share data or interpret costs.

## Quick start

You need Python 3.8 or newer, Git, and a modern browser.
Claude Code must have at least one local session for personal usage data.
You need no Python packages, Node.js, account, or build step.

```bash
git clone https://github.com/wszaq/token-dashboard.git
cd token-dashboard
python3 cli.py dashboard
```

On Windows, run `py -3 cli.py dashboard` if `python3` is not available.
The command scans local transcripts, serves http://127.0.0.1:8080, and opens your browser.
The server scans again every 30 seconds. Press `Ctrl+C` to stop it.

Keep the bind address at `127.0.0.1`.
The server has no authentication or TLS.
The database contains prompt text and tool arguments. Keep it private.

To try the dashboard with synthetic data, see [the bundled sample](docs/installation.md#try-the-bundled-sample).

## Usage

Run these commands from the repository root:

| Command | Action |
| --- | --- |
| `python3 cli.py scan` | Scan source files into the database, then exit. |
| `python3 cli.py today` | Print cached token totals for the current UTC day. |
| `python3 cli.py stats` | Print cached token totals for all time. |
| `python3 cli.py tips` | Print active suggestions from cached data. |
| `python3 cli.py dashboard` | Scan, open the browser, and serve the dashboard. |

The `dashboard` command accepts `--no-open` to skip the browser and `--no-scan` to skip the startup scan.
Every command accepts `--projects-dir PATH` and `--db PATH`. Place them after the command name.

The dashboard has these tabs:

| Tab | Use |
| --- | --- |
| Overview | Compare token totals, daily activity, cache use, models, and projects. |
| Prompts | Find expensive prompts and examine their tool activity. |
| Sessions | Examine turns and tool calls in one session. |
| Projects | Compare project usage and file activity. |
| Skills | Examine skill counts and partial text-size estimates. |
| Tips | Read rule-based suggestions. Dismiss a tip for 14 days. |
| Settings | Select a plan label for the cost display. |

To change prices, edit `pricing.json` and restart the dashboard. The server reads prices at startup.

The local HTTP API has no authentication. Do not expose it to an untrusted network.
See [CLI, configuration, and API reference](docs/reference.md) for every route.

More guides:

- [Installation and first run](docs/installation.md)
- [Usage guide](docs/usage.md)
- [Troubleshooting](docs/troubleshooting.md)
- [GitHub Wiki](https://github.com/wszaq/token-dashboard/wiki)

## Configuration

The code reads these environment variables. Command-line flags override them.

| Variable | Default | Purpose |
| --- | --- | --- |
| `PORT` | `8080` | HTTP port. |
| `HOST` | `127.0.0.1` | Bind address. Keep loopback for private local use. |
| `CLAUDE_PROJECTS_DIR` | `~/.claude/projects` | Transcript root. Flag: `--projects-dir`. |
| `TOKEN_DASHBOARD_DB` | `~/.claude/token-dashboard.db` | SQLite cache file. Flag: `--db`. |

Set a port on macOS or Linux with `PORT=9000 python3 cli.py dashboard`.
The scanner also reads skill metadata from `~/.claude/skills`, `~/.claude/scheduled-tasks`, and `~/.claude/plugins`.
Prices and plan labels live in `pricing.json`.

## Layout

| Path | Contents |
| --- | --- |
| `cli.py` | Command entry point and options. |
| `token_dashboard/scanner.py` | Transcript parser and incremental scan. |
| `token_dashboard/db.py` | SQLite schema and queries. |
| `token_dashboard/server.py` | HTTP routes, SSE stream, and scan loop. |
| `token_dashboard/pricing.py` | Cost estimates and plan settings. |
| `token_dashboard/skills.py` | Local skill catalog. |
| `token_dashboard/tips.py` | Suggestion rules. |
| `web/` | Static frontend. `web/app.js` starts the app and `web/routes/` holds one file per tab. |
| `pricing.json` | Model prices and plan labels. |
| `tests/` | Unit tests with synthetic fixtures in `tests/fixtures/`. |
| `docs/` | User, reference, and privacy documents. |

## Status

The project is a working codebase. It has seven UI tabs.
The test suite has 74 tests. Run them with `python3 -m unittest discover tests`.
All tests passed on macOS with Python 3.14 in the release check on 2026-10-10.
Other operating systems and Python versions need separate checks.

Known limits are in [docs/KNOWN_LIMITATIONS.md](docs/KNOWN_LIMITATIONS.md).
Costs use the local pricing table. Only transcripts on this machine appear.

## Screenshots

These screenshots come from the public upstream repository.
They show upstream example usage, not this repository owner's sessions.
The figures and model labels are examples, not validation of current pricing.

![Overview totals and daily charts](docs/images/dashboard-overview-top.jpg)
![Project totals, model shares, tool counts, and sessions](docs/images/dashboard-overview-bottom.jpg)

## License and attribution

The project uses the [MIT License](LICENSE).
The bundled Apache ECharts 5.5.0 uses its own [license](web/echarts-LICENSE.txt) and [notice](web/echarts-NOTICE.txt).
Its JavaScript file also retains embedded third-party notices.
See [prior work](docs/inspiration.md) for the original project context.

Contributions are welcome. See [CONTRIBUTING](CONTRIBUTING.md).
Report security issues as described in [SECURITY](SECURITY.md).
