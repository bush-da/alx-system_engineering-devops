#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Accept subreddit and return number of subscribers
    for the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
