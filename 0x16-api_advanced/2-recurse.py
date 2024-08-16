#!/usr/bin/python3
"""Recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given
subreddit, the function should return None."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit to query.
    - hot_list (list): The list to accumulate hot article titles.
    - after (str): The after token for pagination (used in recursion).

    Returns:
    - List of titles of hot articles, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/dani)'}

    params = {
        'after': after,
        'limit': 100
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])
    hot_list.extend(post['data']['title'] for post in posts)

    after = data.get('after')

    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
