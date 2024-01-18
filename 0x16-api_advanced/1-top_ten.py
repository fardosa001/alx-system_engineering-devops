#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({"User-Agent": "Custom User Agent"})

    resp = requests.get(url, headers=headers).json()
    top_ten = resp.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for top in top_ten:
        print(top.get('data').get('title'))

