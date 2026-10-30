#!/usr/bin/env python3
"""
Google Trends Scraper API: Interest, Regions & Queries — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/google-trends-api?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/google-trends-api/
n8n Template: https://unitbytes.com/n8n/workflows/google-trends-api-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_google_trends_api.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "keywords": ["OpenAI", "ChatGPT"],
    "custom_timeframe": "2023-01-01 2023-12-31",
    "common_geo": "US",
    "scrape_type": "all",
    "compare_keywords": True,
    "gprop": "web"
}

run = client.actor("unitbytes/google-trends-api").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("geoName"), item.get("keyword"), item.get("value"))
