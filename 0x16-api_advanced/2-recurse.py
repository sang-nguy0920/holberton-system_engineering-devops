#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit.
"""

import json
import requests
from sys import argv


def recurse(subreddit, hot_list=[]):
    """Recursive function that queries the Reddit API"""
