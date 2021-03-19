from datetime import datetime
from tinydb import TinyDB

import auxFunc
import dbFactory

import os
from dotenv import load_dotenv
load_dotenv()

test_db = TinyDB(os.getenv('TEST_ROUTE'))

def test_time_converter():
    utc_date = datetime.now()
    unix_date = 1284105682.0
    print("UTC to UNIX: " + str(auxFunc.utc_to_unix(utc_date)))
    print("UNIX to UTC: " + auxFunc.unix_to_utc(unix_date))

    print("UTC to UNIX to UTC: " + auxFunc.unix_to_utc(auxFunc.utc_to_unix(utc_date)))

def test_db_creation():
    dbFactory.create_db(os.getenv('TEST_ROUTE'))

def test_db_clear():
    dbFactory.clear_db(test_db)

def test_user_creation():
    dbFactory.create_user('stockiestreams', test_db)
    dbFactory.create_user('tiktak12', test_db)

def test_user_removal():
    dbFactory.remove_user(122456, test_db)

def test_user_update():
    dbFactory.update_parameter('stockiestreams', 'points', 1000, test_db)

def test_get_parameter():
    print('Points: ' + str(dbFactory.get_parameter('stockiestreams', 'points', test_db)))
    #print('Last Watched: ' + str(dbFactory.get_parameter(122456, 'last_watched', test_db)))

def test_remove_parameter():
    dbFactory.remove_parameter('points', test_db)

if __name__ == "__main__":
    test_time_converter()
    test_user_creation()
    test_user_removal()
    test_db_creation()
    test_db_clear()
    test_user_update()
    test_get_parameter()
    test_remove_parameter()