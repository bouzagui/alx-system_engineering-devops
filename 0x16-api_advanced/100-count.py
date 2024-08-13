#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, after='', counts={}):
    """Queries Reddit API recursively and counts keywords in hot articles."""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data')

    if not data:
        return

    for post in data.get('children', []):
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            count = title.split().count(word.lower())
            if count > 0:
                counts[word.lower()] = counts.get(word.lower(), 0) + count

    after = data.get('after')

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda item:
                               (-item[1], item[0]))
        for word, count in sorted_counts:
            print(f'{word}: {count}')
