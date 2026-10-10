# Token Dashboard

A local dashboard for Claude Code token usage, estimated costs, and session history.
It reads local JSONL transcripts into a SQLite database. The frontend uses vanilla JavaScript and bundled Apache ECharts.

This repository maintains a version of [Nathan Herkelman's Token Dashboard](https://github.com/nateherkai/token-dashboard).
The original MIT copyright remains in [LICENSE](LICENSE).

## Features

- Token totals and daily charts, with input, output, and cache use.
- Expensive prompts, session details, project comparisons, and tool activity.
- Skill invocation counts and partial estimates for skill text size.
- Rule-based tips for repeated reads, large tool results, and cache use.
- Local pricing settings and live updates after each scan.

Cost figures are estimates from the bundled pricing table. They are not invoices or subscription charges.
See [accuracy and privacy](docs/accuracy-and-privacy.md) before you share data or interpret costs.

## Quick start

Use Python 3.8 or newer, Git, and a modern browser.
Claude Code must have at least one local session for personal usage data.
You need no Python packages, Node.js, account, or build step.

```bash
git clone https://github.com/wszaq/token-dashboard.git
cd token-dashboard
python3 cli.py dashboard
```

On Windows, replace `python3` with `py -3` if necessary.
The command scans local transcripts, serves http://127.0.0.1:8080, and opens your browser.
The server scans every 30 seconds. Stop it with `Ctrl+C`.

Keep `HOST=127.0.0.1`. The server has no authentication or TLS.
The cache contains prompt text and tool arguments. Keep it private.

## Documentation

- [Installation and first run](docs/installation.md)
- [Usage guide](docs/usage.md)
- [CLI, configuration, and API reference](docs/reference.md)
- [Accuracy, privacy, and architecture](docs/accuracy-and-privacy.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Known limitations](docs/KNOWN_LIMITATIONS.md)
- [GitHub Wiki](https://github.com/wszaq/token-dashboard/wiki)
- [Contributing](CONTRIBUTING.md) and [security reports](SECURITY.md)

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
