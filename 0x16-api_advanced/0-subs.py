#!/usr/bin/python3
"""Module to query the Reddit API and return the number of subscribers."""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = 'https://www.reddit.com/r/{subreddit}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'my-reddit-subscriber-counter'
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data'].get('subscribers', 0)
    else:
        return 0
