#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """ Recursive function that returns a list of titles of all hot articles for a given subreddit """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'custom-user-agent'
    }
    params = {
        'limit': 100,
        'after': after
    }
    res = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if res.status_code != 200:
        return None

    data = res.json().get('data', {})
    children = data.get('children', [])

    hot_list.extend([child['data']['title'] for child in children])

    after = data.get('after')
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
