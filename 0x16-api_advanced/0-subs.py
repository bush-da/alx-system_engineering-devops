#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Accept subreddit and return number of subscribers
    for the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent-v1.0'}

    try:
        """Make a GET request to the Reddit API"""
        response = requests.get(url, headers=headers, allow_redirects=False)

        """Check if the status code is 200 (OK)"""
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0

    except requests.RequestException as e:
        return 0
