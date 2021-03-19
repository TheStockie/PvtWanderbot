from tinydb import TinyDB, Query
from tinydb.operations import delete
from datetime import datetime
from auxFunc import utc_to_unix, unix_to_utc

import os
from dotenv import load_dotenv
load_dotenv()

# Create db
def create_db(route):
    return TinyDB(route)

# Delete ALL values in db
# EXTREME CAUTION WITH THIS ONE
def clear_db(db):
    are_you_really_sure_about_this = False
    if are_you_really_sure_about_this == True:
        db.truncate()

# Give user_id; create default user
# [Int user_id, Int points, Float lastWatched, Int totalGain, Int totalLoss, Int netProfit, Int percentNetProfit, Float lastCommand (used as a flag), Int timesUsed (one per command)]
def create_user(user_id, db):
    time_now = utc_to_unix(datetime.now())
    back_in_time = utc_to_unix(datetime(2000, 1, 1, 0, 0, 0))
    if not db.contains(Query().user_id == user_id):
        # TO-DO: Add flags for each command
        db.insert({'user_id': user_id, 'points': 100, 'last_watched': time_now, 'total_gain': 0, 'total_loss': 0, 'net_profit': 0, 'percent_net_profit': 0, 'last_command': back_in_time})

# Give user_id; remove user
def remove_user(user_id, db):
    db.remove(Query().user_id == user_id)

# Give user_id, parameter and value; update user_id's parameter with value with time parsing
def update_parameter(user_id, parameter, value, db):
    if type(parameter) is datetime:
        db.update({parameter: utc_to_unix(value)}, Query().user_id == user_id)
    else:
        db.update({parameter: value}, Query().user_id == user_id)

# Give user_id and parameter; return parameter value with time parsing (FLOATS RESERVED FOR UNIX)
def get_parameter(user_id, parameter, db):
    if db.contains(Query().user_id == user_id):
        value = db.search(Query().user_id == user_id)[0][parameter]
        if type(value) is float:
            return unix_to_utc(value)
        else:
            return value

# Deletes an entire parameter from the db
# EXTREME CAUTION WITH THIS ONE
def remove_parameter(parameter, db):
    are_you_really_sure_about_this = False
    if are_you_really_sure_about_this == True:
        db.update(delete(parameter))