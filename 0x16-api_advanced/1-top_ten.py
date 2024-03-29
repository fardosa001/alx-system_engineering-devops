#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the

first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    resp = requests.get(url, headers=headers, allow_redirects=False).json()
    top_ten_posts = resp.get('data', {}).get('children', [])
    if not top_ten_posts:
        print(None)
    for post in top_ten_posts:
        print(post.get('data').get('title'))
