#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.
"""
from requests import get


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a particular subreddit.
    If no results are found for the given subreddit, the function
    return None
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = get(url, headers=headers, params=params, allow_redirects=False)

    try:
        if response.status_code == 404:
            return None

        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")

        hot_list = \
            [i.get("data").get("title") for i in results.get("children")]

    except Exception:
        return None

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
