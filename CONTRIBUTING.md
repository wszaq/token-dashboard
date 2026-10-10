# Contributing

## Prepare a change

Fork the repository. Create a branch for one focused change.
Read the [source map](docs/reference.md#source-map) before edits.
Keep the backend standard-library-only and the frontend without a build step.
Use bound SQLite parameters for user input.
Preserve all project and third-party license notices.

## Test

Run from the repository root:

```bash
python3 -m unittest discover tests
```

The tests use synthetic fixtures and temporary databases. They need no downloaded fixtures.
Add a regression test for a bug. Add behavior checks for a feature.
Use the [sample installation](docs/installation.md#try-the-bundled-sample) for manual UI checks.
Do not commit real prompts, databases, or private screenshots.

## Submit a pull request

Describe the problem, behavior after the change, and checks you ran.
Include a screenshot from synthetic data for a visual change.
Update relevant documentation when a command, limit, or feature changes.
Use a specific commit message, such as `docs: explain cache privacy`.
Submit the pull request against `main`.

## Documentation and wiki

Repository documents are the canonical source.
The Markdown files in `docs/wiki/` supply the GitHub Wiki home, guides, and sidebar.
Update both navigation sets if you add or rename a document.
The wiki links to repository documents so detailed instructions have one maintained source.

## License

Contributions use the [MIT License](LICENSE), except files with their own third-party license.
For a vulnerability, use [SECURITY.md](SECURITY.md).
