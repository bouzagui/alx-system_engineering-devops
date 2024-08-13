#!/usr/bin/python3
import requests

url = f'https://www.reddit.com/r/{subreddit}/about.json'
headers = {
    'User-Agent': 'User_Agent_/3.0'
    }


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API """
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data'].get('subscribers')
    else:
        return 0
