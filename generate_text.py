subs = []  # add your subreddits
users = []  # add users you follow

with open('subreddits.txt', 'w') as f:
    for sub in subs:
        f.write(f'https://www.reddit.com/r/{i}\n')
    for user in users:
        f.write(f'https://www.reddit.com/{i}\n')
