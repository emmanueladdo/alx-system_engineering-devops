#!/usr/bin/python3
"""
Script that contains a function
that prints the titles of the first 10 hot posts listed
for a given subreddit
"""
import requests


def top_ten(subreddit):
    # Make a request to check if the subreddit exists
    rdchecks = requests.get(
        "https://www.reddit.com/api/search_reddit_names.json",
        headers={
            'User-Agent': 'Mozilla/5.0'},
        params={
            'exact': True,
            'query': subreddit
        })

    # Check if there was an error in the response
    if 'error' in rdchecks.json():
        print("None")  # Subreddit does not exist
        return

    # Make a request to get the first 10 hot posts
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
        headers={
            'User-Agent': 'Mozilla/5.0'
        })

    # Extract and print the titles of the first 10 hot posts
    for post in response.json().get('data', {}).get('children', []):
        print(post.get('data', {}).get('title'))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
