#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print top ten subreddit post titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/dani)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                print(post['data']['title'])
        else:
            print('None')

    except requests.RequestException as e:
        print('None')
