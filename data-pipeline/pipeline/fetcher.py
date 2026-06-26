"""
============================================================
PIPELINE LAYER 1 — FETCHER
============================================================
Role: Data Engineer

Responsibility: Talk to Lobsters' public JSON endpoint and return
the RAW response data. This layer does NOT clean, validate, or
reshape anything — it just fetches and hands back what Lobsters gave us.

Why a separate layer for this?
  - If Lobsters changes their API, only this file needs to change.
  - We can test the rest of the pipeline with fake fetched data,
    without needing the internet.

ABOUT THE DATA SOURCE — lobste.rs:
Lobsters (lobste.rs) is a programming-focused link aggregator. It has
simple, public, unauthenticated JSON endpoints — no API key, no login,
no OAuth needed:

    https://lobste.rs/hottest.json
    https://lobste.rs/newest.json
============================================================
"""

import requests

USER_AGENT = "python:lobsters-top-posts-student-project:v1.0 (by /u/your_username_here)"

LOBSTERS_HOTTEST_URL = "https://lobste.rs/hottest.json"


def fetch_top_posts_raw(limit: int = 10) -> list:
    """
    Fetches the raw "hottest" stories JSON from Lobsters.

    Args:
        limit (int): Number of posts requested (actual trimming happens
                     in transformer.py).

    Returns:
        list: Raw JSON response from Lobsters.
    """

    headers = {
        "User-Agent": USER_AGENT
    }

    response = requests.get(
        LOBSTERS_HOTTEST_URL,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    return response.json()