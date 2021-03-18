from datetime import timezone, datetime
from tinydb import Query

def utc_to_unix(utc_date):
    return utc_date.replace(tzinfo=timezone.utc).timestamp()

def unix_to_utc(unix_date):
    return datetime.fromtimestamp(unix_date).strftime('%Y-%m-%d %H:%M:%S')
