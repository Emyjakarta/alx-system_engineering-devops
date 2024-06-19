#!/usr/bin/python3

"""Script that queries the Reddit API and prints the titles of the first 10 top
posts for a give subreddit."""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Send a GET request to the Reddit API to retrieve the top 10 hot posts
    reply = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "nabuntu_bot-01"},
        allow_redirects=False,
    )

    # Check if the request was successful
    if reply.status_code != 200:
        print(None)
        return

    # Print the titles of the top 10 hot posts
    for send in reply.json()["data"]["children"]:
        print(send["data"]["title"])
