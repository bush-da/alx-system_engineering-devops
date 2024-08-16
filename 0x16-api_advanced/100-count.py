#!/usr/bin/python3
"""Recursive function that queries the Reddit API, parses
the title of all hot articles,and prints a sorted count of given
keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/dani)'}

    params = {'after': after, 'limit': 100}

    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})

    children = data.get('children', [])

    for child in children:
        title = child['data']['title'].lower().split()
        for word in word_count:
            word_count[word] += title.count(word)

    after = data.get('after')

    if after:
        return count_words(subreddit, word_list, after, word_count)
    sorted_word_count = sorted([(word, count) for word, count in
                                word_count.items() if count > 0],
                               key=lambda item: (-item[1], item[0]))

    for word, count in sorted_word_count:
        print(f"{word}: {count}")
