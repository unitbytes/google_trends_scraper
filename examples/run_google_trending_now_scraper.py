#!/usr/bin/env python3
"""
Google Trending Now & Realtime Trends Scraper — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/google-trending-now-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/google-trending-now-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/google-trending-now-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_google_trending_now_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "common_geo": "US",
    "trending_language": "en",
    "max_events": 200,
    "time_window": "24h",
    "output_format": "flat",
    "trending_hours": 24
}

run = client.actor("unitbytes/google-trending-now-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("keyword"), item.get("volume"), item.get("volume_growth_pct"), item.get("geo"))
