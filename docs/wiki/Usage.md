# Usage guide

## Read the dashboard

Start with `python3 cli.py dashboard`.
The server scans local transcripts before it starts. Later scans run every 30 seconds.
Server-sent events tell the browser when new messages arrive.

| Tab | Use |
| --- | --- |
| Overview | Compare token totals, daily activity, cache use, models, and projects. |
| Prompts | Find expensive prompts and examine their tool activity. |
| Sessions | Examine turns and tool calls in one session. |
| Projects | Compare project usage and file activity. |
| Skills | Examine skill counts and partial text-size estimates. |
| Tips | Read rule-based suggestions. Dismiss a tip for 14 days. |
| Settings | Select a plan label for the cost display. |

Use the Overview date controls to inspect a time range.
Not every route uses the same filter. Prompts and Tips use database-wide queries.

## Read terminal totals

These commands read the cached database. Run `scan` first when you need fresh totals.

```bash
python3 cli.py scan
python3 cli.py today
python3 cli.py stats
python3 cli.py tips
```

`today` uses UTC day boundaries. It can differ from your local calendar day.

## Change prices

Edit `pricing.json` to change rates or add model identifiers.
Restart the dashboard after the edit. The server reads prices at startup.
The subscription plan selection does not change token usage into subscription charges.
See [accuracy and privacy](https://github.com/wszaq/token-dashboard/blob/main/docs/accuracy-and-privacy.md) for the calculation limits.

## Share a problem safely

Use the bundled sample to reproduce a problem when possible.
Remove prompts, paths, project names, and identifiers from reports and screenshots.
Do not upload your SQLite database or original transcripts.
