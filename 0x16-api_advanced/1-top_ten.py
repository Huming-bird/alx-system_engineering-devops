#!/usr/bin/python3
"""
a script that prints the titles of the
first 10 hot posts for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a particular subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "limit": 10
    }

    response = get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(i.get("data").get("title")) for i in results.get("children")]
