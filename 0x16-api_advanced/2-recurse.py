#!/usr/bin/python3
"""Recurse function definition"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    Recurse function recursively produces a list of all hot articles
    on a subreddit
    """
    rdcheck = requests.get("https://reddit.com/api/search_reddit_names.json",
                           headers={
                               'User-Agent': 'Mozilla/5.0'
                           },
                           params={
                               'exact': True,
                               'query': subreddit
                           })
    if 'error' in rdcheck.json().keys():
        return None

    response = requests.get(f"https://reddit.com/r/{subreddit}/hot.json",
                            headers={
                                'User-Agent': 'Mozilla/5.0'
                            },
                            params={
                                'after': after
                            })
    for child in response.json().get('data').get('children'):
        hot_list.append(child.get('data').get('title'))
    if response.json().get('data').get('after') is None:
        return hot_list

    return recurse(subreddit,
                   hot_list,
                   response.json().get('data').get('after'))
