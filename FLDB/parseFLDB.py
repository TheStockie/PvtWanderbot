import sys
from dbFactory import create_user, remove_user
from tinydb import TinyDB, Query
from twitch_check import is_streaming

import os
from dotenv import load_dotenv
load_dotenv()

fldb = TinyDB("test.json")
User = Query()
username = sys.argv[2]

def parse_command():
    streamingFlag = is_streaming(os.getenv('CHANNEL'))
    if streamingFlag == False:
        commandList[sys.argv[1]]()

def join():
    if not fldb.contains(Query().username == username):
        sys.stdout.write('1')
        create_user(username, fldb)

    else:
        sys.stdout.write('0')

    exit()

def balance():
    if fldb.contains(Query().username == username):
        result = [fldb.search(User.username == username)[0]['points'], 1]
        sys.stdout.write(str(result))

    else:
        sys.stdout.write('0')

commandList = {
    "join": join,
    "balance": balance
}

parse_command()