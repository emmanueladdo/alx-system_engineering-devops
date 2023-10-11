#!/usr/bin/python3
"""Recurse function definition"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    if subreddit is None or not isinstance(subreddit, str):
        return None

    req = requests.get(url, headers=headers, allow_redirects=False).json()
    data = req.get('data')
    if data:
        children = data.get('children')
        for post in children:
            postData = post.get('data')
            title = postData.get('title')
            hot_list.append(title)
        after = data.get('after')

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
