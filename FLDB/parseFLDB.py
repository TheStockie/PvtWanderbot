import sys
from dbFactory import create_user, remove_user
from tinydb import TinyDB, Query

import os
from dotenv import load_dotenv
load_dotenv()

fldb = TinyDB('../FLDB/test.json')
User = Query()

user_id = sys.argv[2]

def parse_command():
    commandList[sys.argv[1]]()

def join():
    if not fldb.contains(Query().user_id == user_id):
        sys.stdout.write('1')
        create_user(user_id, fldb)

    else:
        sys.stdout.write('0')

    exit()

def balance():
    if fldb.contains(Query().user_id == user_id):
        result = [fldb.search(User.user_id == user_id)[0]['points'], 1]
        sys.stdout.write(str(result))

    else:
        sys.stdout.write('0')

commandList = {
    "join": join,
    "balance": balance
}

parse_command()