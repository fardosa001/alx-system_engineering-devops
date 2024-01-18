#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the

first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    data = {}
    headers = {"User-Agent": "My User Agent 1.0"}

    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
    top_ten_posts = data.get('data', {}).get('children', [])
    if not top_ten_posts:
        print(None)
    for post in top_ten_posts:
        print(post.get('data').get('title'))
