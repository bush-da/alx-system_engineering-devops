#!/usr/bin/python3
"""function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Send Get request to reddit api to get number of
    subscribers for particular subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/dani)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get('data')

    return data.get('subscribers')
