# CLI, configuration, and API reference

## Commands

Run commands from the repository root.

| Command | Action |
| --- | --- |
| `python3 cli.py scan` | Scan source files into the database, then exit. |
| `python3 cli.py today` | Print cached token totals for the current UTC day. |
| `python3 cli.py stats` | Print cached token totals for all time. |
| `python3 cli.py tips` | Print active suggestions from cached data. |
| `python3 cli.py dashboard` | Scan, open the browser, and serve the dashboard. |

Each command accepts `--projects-dir PATH` and `--db PATH`.
Put these options after the command. For example, `python3 cli.py scan --db /tmp/demo.db`.
Use `python3 cli.py --help` or `python3 cli.py dashboard --help` for built-in help.

| Dashboard flag | Action |
| --- | --- |
| `--no-open` | Do not open the browser automatically. |
| `--no-scan` | Skip the initial scan. The background scan still runs. |

## Environment variables

| Variable | Default | Purpose |
| --- | --- | --- |
| `PORT` | `8080` | HTTP port. |
| `HOST` | `127.0.0.1` | Bind address. Keep loopback for private local use. |
| `CLAUDE_PROJECTS_DIR` | `~/.claude/projects` | Transcript root. |
| `TOKEN_DASHBOARD_DB` | `~/.claude/token-dashboard.db` | SQLite cache file. |

For transcript and database paths, command flags override environment variables.
Environment variables override defaults.
The scanner also reads skill metadata from `~/.claude/skills`, `~/.claude/scheduled-tasks`, and `~/.claude/plugins`.

On macOS or Linux, change the port with:

```bash
PORT=9000 python3 cli.py dashboard
```

In PowerShell, use:

```powershell
$env:PORT = '9000'
py -3 cli.py dashboard
```

## Local HTTP API

This API has no authentication. It is an internal interface for the frontend, not a versioned public API.
Do not expose it to an untrusted network.

| Method and route | Result or action |
| --- | --- |
| `GET /api/overview` | Token totals and estimated cost. |
| `GET /api/projects` | Project summaries. |
| `GET /api/tools` | Tool activity. |
| `GET /api/daily` | Daily token totals. |
| `GET /api/by-model` | Model totals and estimated costs. |
| `GET /api/skills` | Skill counts and catalog text-size estimates. |
| `GET /api/sessions` | Recent sessions. |
| `GET /api/sessions/SESSION_ID` | Session turns. |
| `GET /api/prompts` | Expensive prompts. |
| `GET /api/tips` | Active suggestions. |
| `GET /api/plan` | Saved plan and pricing table. |
| `GET /api/scan` | Run a scan and return scan counts. |
| `GET /api/stream` | Server-sent events with scan notifications. |
| `POST /api/plan` | Save `{"plan":"api"}` or another configured plan. |
| `POST /api/tips/dismiss` | Dismiss the tip identified by `{"key":"TIP_KEY"}`. |

Overview, Projects, Tools, Daily, By-model, Skills, and Sessions accept `since` and `until` timestamps.
Sessions and Prompts accept `limit`. The server clamps it from 1 to 1000.
Prompts also accepts `sort=tokens` or `sort=recent`. Other values use token order.
`GET /api/scan` changes the database despite its GET method.

## Source map

- `cli.py`: command options and startup.
- `token_dashboard/scanner.py`: transcript parser and incremental scan.
- `token_dashboard/db.py`: schema and database queries.
- `token_dashboard/server.py`: HTTP routes and scan loop.
- `token_dashboard/pricing.py`: cost estimates and plan settings.
- `token_dashboard/skills.py`: local skill catalog.
- `token_dashboard/tips.py`: suggestion rules.
- `web/`: static frontend, with no build step.
