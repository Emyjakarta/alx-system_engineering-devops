#!/usr/bin/python3
"""Script that queries the Reddit API and returns the number of total
subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the
        request fails or the subreddit does not exist.
    """
    reply = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        allow_redirects=False,
        headers={"user-agent": "nabuntu_bot-01"},
        timeout=60,
    )

    return (
        reply.json()["data"]["subscribers"]
        if reply.status_code == 200
        else 0
    )
