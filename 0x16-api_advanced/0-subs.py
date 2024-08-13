#!/usr/bin/python3
"""models doc"""
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'custom-user-agent'
        }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data'].get('subscribers')
    else:
        return 0
