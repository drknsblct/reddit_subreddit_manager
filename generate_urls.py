import re

# paste list acquired from browser in subs
# press ctrl + alt and drag mouse from left to right to select all elements
# while all elements are selected:
#   add quotes
#   add comma
# remove comma on the right of last element
subs = []

subs_with_urls = []


for sub in subs:
    if re.search('^u/', sub):
        subs_with_urls.append(f'https://www.reddit.com/{sub}')
    else:
        subs_with_urls.append(f'https://www.reddit.com/r/{sub}')
