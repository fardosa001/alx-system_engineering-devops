#!/usr/bin/python3
"""queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """returns a list containing the titles of all hot articles
    for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    if after:
        url += "&after={}".format(after)

    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        resp_json = resp.json()
        hot_posts = resp_json.get('data').get('children')
        after = resp_json.get('data').get('after')

        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    return None
