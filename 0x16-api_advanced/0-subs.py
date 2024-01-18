#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers"""
    # set url strings
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "python/requests"}

    # make the API request
    resp = requests.get(url, headers=headers).json()
    subscribers = resp.get('data', {}).get('subscribers')
    if resp.status_code in [302, 404]:
        return 0
    return subscribers
