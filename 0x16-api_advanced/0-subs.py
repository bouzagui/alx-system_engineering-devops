#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'custom-user-agent'
        }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data'].get('subscribers')
    else:
        return 0
