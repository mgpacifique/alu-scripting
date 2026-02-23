#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API and return total subscribers for a subreddit.

    Returns 0 if the subreddit is invalid or the request fails.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu_scripting:v1.0 (by /u/mgpacifique)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers")
        if subscribers is not None:
            return subscribers
    return 0
