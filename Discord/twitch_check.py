import urllib3
import json

import os
from dotenv import load_dotenv
load_dotenv()

# Twitch Username parser DO NOT TOUCH

http = urllib3.PoolManager()

TWITCH_STREAM_API_GET_USERS = "https://api.twitch.tv/kraken/users?login={}"
TWITCH_STREAM_API_ENDPOINT = "https://api.twitch.tv/kraken/streams/{}"

API_HEADERS = {
    'Accept' : 'application/vnd.twitchtv.v5+json',
    'Client-ID' : os.getenv('CLIENT_ID')
}

def is_streaming(user):
    url = TWITCH_STREAM_API_GET_USERS.format(user)

    try:
        req = http.request('GET', url, headers = API_HEADERS)
        jsondata = json.loads(req.data.decode('utf-8'))
        return check_user(jsondata['users'][0]['_id'])

    except Exception as e:
        print("Error checking user: ", e)
        return

def check_user(user_ID):
    url = TWITCH_STREAM_API_ENDPOINT.format(user_ID)

    try:
        req = http.request('GET', url, headers=API_HEADERS)
        jsondata = json.loads(req.data.decode('utf-8'))
        if jsondata['stream'] is not None:
            return True

        else:
            return False

    except Exception as e:
        print("Error checking user: ", e)
        return False