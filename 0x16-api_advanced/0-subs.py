#!/usr/bin/python3
"""
Script that contains a function
that returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Check if a subreddit exists and get its subscribers"""

    # Make a request to check if the subreddit exists
    rdchecks = requests.get(
        "https://www.reddit.com/api/search_reddit_names.json",
        headers={
            'User-Agent': 'Mozilla/5.0'},
        params={
            'exact': True,
            'query': subreddit})

    # Check if there was an error in the response
    if 'error' in rdchecks.json():
        return 0  # Subreddit does not exist

    # Make a request to get the subscribers count
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={
            'User-Agent': 'Mozilla/5.0'
            })

    # Extract and return the number of subscribers
    return response.json().get('data', {}).get('subscribers', 0)
