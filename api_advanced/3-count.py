#!/usr/bin/python3
"""Recursively queries Reddit API and counts keyword occurrences in hot titles."""
import requests


def count_words(subreddit, word_list, word_counts=None, totals=None, after=None):
    """Recursively query Reddit API and print sorted keyword counts.

    Counts are case-insensitive and based on exact word matches (java. does not
    count as java). Duplicate keywords in word_list multiply the count.
    Results are printed in descending order by count, then alphabetically.
    Prints nothing if no matches or subreddit is invalid.
    """
    if word_counts is None:
        word_counts = {}
        for word in word_list:
            key = word.lower()
            word_counts[key] = word_counts.get(key, 0) + 1

    if totals is None:
        totals = {k: 0 for k in word_counts}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after is not None:
        url += "&after={}".format(after)

    headers = {"User-Agent": "alu-scripting:api_advanced:v0.1 (by /u/alu_student)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title_words = post.get("data", {}).get("title", "").lower().split()
        for title_word in title_words:
            if title_word in word_counts:
                totals[title_word] += word_counts[title_word]

    next_after = data.get("after")

    if next_after is None:
        sorted_results = sorted(
            totals.items(), key=lambda item: (-item[1], item[0])
        )
        for word, count in sorted_results:
            if count > 0:
                print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, word_counts, totals, next_after)
