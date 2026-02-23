#!/usr/bin/python3
"""Recursively queries the Reddit API and returns all hot article titles."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively query the Reddit API and return a list of all hot titles.

    Returns None if the subreddit is invalid or no results are found.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after is not None:
        url += "&after={}".format(after)

    headers = {
        "User-Agent": "linux:alu_scripting:v1.0 (by /u/mgpacifique)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children")

    if posts is None or len(posts) == 0:
        return hot_list if hot_list else None

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    next_after = data.get("after")
    if next_after is None:
        return hot_list

    return recurse(subreddit, hot_list, next_after)
