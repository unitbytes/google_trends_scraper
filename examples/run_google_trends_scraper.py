#!/usr/bin/env python3
"""
Google Trends Scraper: Keywords, Geo & Topics — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/google-trends-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/google-trends-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/google-trends-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_google_trends_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "keywords": ["OpenAI", "ChatGPT"],
    "custom_timeframe": "2023-01-01 2023-12-31",
    "common_geo": "US"
}

run = client.actor("unitbytes/google-trends-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("keyword"), item.get("value"), item.get("date"))
