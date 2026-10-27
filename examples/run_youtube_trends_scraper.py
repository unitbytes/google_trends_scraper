#!/usr/bin/env python3
"""
YouTube Trends Scraper: Breakout Keywords & SEO — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/youtube-trends-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/youtube-trends-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/youtube-trends-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_youtube_trends_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "keywords": ["AI Agents", "Claude Code"],
    "common_geo": "US",
    "scrape_type": "all",
    "compare_keywords": True,
    "category": 0,
    "predefined_timeframe": "today 12-m"
}

run = client.actor("unitbytes/youtube-trends-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("original_keyword"), item.get("related_keyword"), item.get("value"), item.get("search_type"))
