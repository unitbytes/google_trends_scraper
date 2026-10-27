# Contributing to UnitBytes Google Trends Scraper Suite

Thank you for your interest in contributing to the **UnitBytes Google Trends Python SDK Quickstarts & n8n Automation Suite** (`unitbytes/google_trends_scraper`)! We welcome bug reports, workflow improvements, Python integration examples, and documentation updates.

## Table of Contents

- [How to Submit Changes](#how-to-submit-changes)
- [Python Code Style & Quality](#python-code-style--quality)
- [Testing Examples & n8n Workflows](#testing-examples--n8n-workflows)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)

## How to Submit Changes

1. Fork this repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/google_trends_scraper.git
   cd google_trends_scraper
   ```
3. Create a new branch for your work:
   ```bash
   git checkout -b feature/my-improvement
   ```
4. Make and verify your changes locally.
5. Commit your changes with a clear, descriptive message:
   ```bash
   git add .
   git commit -m "docs: improve Python quickstart example"
   ```
6. Push your branch and open a Pull Request against `main`.

## Python Code Style & Quality

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python formatting.
- Never hardcode API tokens or credentials; always read `APIFY_API_TOKEN` from environment variables (`os.getenv("APIFY_API_TOKEN")`).
- Keep dependencies minimal (`apify-client`, `requests`).

## Testing Examples & n8n Workflows

- Verify Python syntax across all example scripts before submitting:
  ```bash
  python3 -m py_compile examples/*.py
  ```
- Verify that any modified `.json` workflow in `n8n/` parses as valid JSON and imports cleanly into n8n (`Ctrl+V`).

## Reporting Bugs

If you encounter an issue with an extraction run, schema field, or workflow template, please open a [GitHub Issue](https://github.com/unitbytes/google_trends_scraper/issues) or contact us at [contact@unitbytes.com](mailto:contact@unitbytes.com) with:

- The target Actor slug (e.g., `unitbytes/google-trends-scraper`).
- The input parameters (`keywords`, `scrape_type`, `timeframe`, `geo`) used.
- Expected versus actual output fields.

## Feature Requests

To propose a new integration example, n8n workflow template, or schema enhancement, open an issue or reach out via [https://unitbytes.com](https://unitbytes.com).
