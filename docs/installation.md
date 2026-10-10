# Installation and first run

## Requirements

Use Python 3.8 or newer, Git, and a modern browser.
The code uses only the Python standard library.

The expected transcript location is `~/.claude/projects/` on macOS and Linux.
On Windows, it is `%USERPROFILE%\.claude\projects`.
The source uses portable Python APIs. This release check ran on macOS with Python 3.14.
Other systems and Python versions were not tested in that check.

## Install

1. Check Python with `python3 --version`.
2. Clone the repository.

```bash
git clone https://github.com/wszaq/token-dashboard.git
cd token-dashboard
```

3. Start the dashboard.

```bash
python3 cli.py dashboard
```

4. Open http://127.0.0.1:8080 if the browser does not open.
5. Stop the server with `Ctrl+C` when you finish.

On Windows, use `py -3` in place of `python3` if necessary.
Python is not present on every system. Install it before these steps if the version check fails.

## Try the bundled sample

This example uses synthetic test data. It does not scan your transcript directory.
Choose an unused database path in a temporary directory.

```bash
python3 cli.py scan --projects-dir tests/fixtures --db /tmp/token-dashboard-demo.db
python3 cli.py dashboard --projects-dir tests/fixtures --db /tmp/token-dashboard-demo.db --no-open
```

On Windows, replace `/tmp/token-dashboard-demo.db` with an unused path under `%TEMP%`.
The sample contains one session, so some charts and tips can be empty.

## Custom transcript and cache paths

```bash
python3 cli.py dashboard --projects-dir /path/to/projects --db /path/to/cache.db
```

Create the parent directories before the command. Quote paths that contain spaces.
Do not copy real transcripts or the database into a public repository.

## Remove the installation

Stop the server. Remove the cloned directory if you no longer need it.
The default database remains at `~/.claude/token-dashboard.db`.
Remove that file separately if you no longer need the cached data or saved settings.
The dashboard does not change your source transcripts.
