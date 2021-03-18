from tinydb import TinyDB, Query
from datetime import datetime
from auxFunc import utc_to_unix, unix_to_utc

import os
from dotenv import load_dotenv
load_dotenv()

def create_db(route):
    return TinyDB(route)

# EXTREME CAUTION WITH THIS ONE
def clear_db(db):
    are_you_really_sure_about_this = False
    if are_you_really_sure_about_this == True:
        db.truncate()

# Str username: [Int points, Date lastWatched, Int totalGain, int totalLoss, int netProfit, int percentNetProfit, date lastCommand (used as a flag), int timesUsed (one per command)]
def create_user(user_id, db):
    time_now = utc_to_unix(datetime.now())
    back_in_time = utc_to_unix(datetime(2000, 1, 1, 0, 0, 0))
    if len(db.search(Query().user_id == user_id)) == 0:
        # TO-DO: Add flags for each command
        db.insert({'user_id': user_id, 'points': 100, 'lastWatched': time_now, 'totalGain': 0, 'totalLoss': 0, 'netProfit': 0, 'percentNetProfit': 0, 'lastCommand': back_in_time})

def remove_user(user_id, db):
    if len(db.search(Query().user_id == user_id)) > 0:
        db.remove(Query().user_id == user_id)



