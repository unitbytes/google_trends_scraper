#!/usr/bin/env python3
"""
Google Shopping Trends Scraper: Product Demand — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/google-shopping-trends-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/google-shopping-trends-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/google-shopping-trends-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_google_shopping_trends_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "keywords": ["Air Fryer", "Espresso Machine"],
    "common_geo": "US",
    "scrape_type": "all",
    "compare_keywords": True,
    "category": 0,
    "predefined_timeframe": "today 12-m"
}

run = client.actor("unitbytes/google-shopping-trends-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("keyword"), item.get("date"), item.get("value"), item.get("geo"))
