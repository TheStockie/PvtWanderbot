import urllib3
import json
import time
from tinydb import TinyDB, Query
from dbFactory import update_parameter, get_parameter

import os
from dotenv import load_dotenv
load_dotenv()

from twitch_check import is_streaming

http = urllib3.PoolManager()
test_db = TinyDB(os.getenv('TEST_ROUTE'))

TWITCH_STREAM_API_GET_VIEWERS = 'https://tmi.twitch.tv/group/user/{}/chatters'

def get_viewer_list():
    url = TWITCH_STREAM_API_GET_VIEWERS.format(os.getenv('CHANNEL'))

    try:
        req = http.request('GET', url)
        jsondata = json.loads(req.data.decode('utf-8'))
        return jsondata['chatters']

    except Exception as e:
        print("Error checking user: ", e)
        return
    

def start_timer():
    start_time = time.time()
    timer = 5
    print('I have arrived to pay the day')

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > timer:
            payday()
            start_time = time.time()
            current_time = time.time()

def payday():
    if is_streaming(os.getenv('CHANNEL')) == True:
        print('Payday')
        viewer_list = get_viewer_list()
        for category in viewer_list:
            current_list = viewer_list[category]
            for viewer in current_list:
                if test_db.contains(Query().username == viewer) and len(current_list) > 0:
                    points = get_parameter(viewer, "points", test_db)
                    newPoints = points + 15
                    update_parameter(viewer, "points", newPoints, test_db)  
            
start_timer()
