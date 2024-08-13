#!/usr/bin/python3
"""model doc"""
import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API and prints
        the titles of the first 10 hot posts """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
        'User-Agent': 'custom-user-agent'
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        posts = data['data'].get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
