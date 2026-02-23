#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Query the Reddit API and print the top 10 hot post titles.

    Prints None if the subreddit is invalid or the request fails.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:alu_scripting:v1.0 (by /u/mgpacifique)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children")

    if posts is None:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
