import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.
    base_url = 'https://api.github.com/'
    user_url = base_url + 'users/'+username + '/events'  
    user_page = requests.get(user_url)
    content = json.loads(user_page.content)
    created_at = content[0]['created_at']
    print(created_at)

