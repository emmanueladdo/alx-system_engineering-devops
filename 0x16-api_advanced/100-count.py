#!/usr/bin/python3
"""
counts the titles
"""


import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get('data')
    if data:
        children = data.get('children')
        for post in children:
            title = post.get('data').get('title').lower()
            for word in word_list:
                if f' {word.lower()} ' in f' {title} ':
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1

    after = data.get('after')
    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(
            counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
