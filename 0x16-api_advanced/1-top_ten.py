#!/usr/bin/python3
"""
A function that queries the Reddit API and
prints the titles of the first 10 hot posts listed
for a given subreddit.
"""

import json
import requests
from sys import argv


def top_ten(subreddit):
    """first 10 hot posts"""
    subreddit = argv[1]
    url = "http://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    agent = "Holberton-Reddit-API-project"

    top_ten = requests.get(url, headers={'User-Agent': agent})

    if top_ten.status_code != 200:
        print(None)
    else:
        jsondata = top_ten.json()
        fire = jsondata.get('data').get('children')
        for hot in fire:
            title = hot.get('data').get('title')
            print(title)
