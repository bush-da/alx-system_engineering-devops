#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'X11; Ubuntu; Linux x86_64; rv:129.0) Firefox/129.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get('data')
    return results['subscribers']
