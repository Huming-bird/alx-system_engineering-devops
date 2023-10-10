#!/usr/bin/python3
""" thisi cript checks the number of subscribers to a subreddit """


from requests import get


def number_of_subscribers(subreddit):
    """mehod to return the total num of subs to a given subreddit."""

    if subreddit is not None or isinstance(subreddit, str):
        try:
            user_agent = {"User-agent": "Google Chrome Version 115.0.5790.171"}
            url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
            response = get(url, headers=user_agent)
            results = response.json()

            return results.get("data").get("subscribers")

        except Exception:
            pass
    return 0
