#!/usr/bin/python3
"""
A function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.
"""

import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ number_of_subscribers"""
    subreddit = argv[1]
    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    agent = "API-practice-holberton-cardano"

    subscribers = requests.get(url, headers={'User-Agent': agent})

    if subscribers.status_code != 200:
        return (0)
    else:
        json_response = subscribers.json()
        sub_count = json_response.get('data').get('subscribers')
        return sub_count
