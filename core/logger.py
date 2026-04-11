import datetime
import os

LOG_FILE = "dgp_log.txt"

def log_event(event_type, message, result=None):
    now = datetime.datetime.now()

    log_entry = f"""
==============================
Time: {now.strftime('%Y-%m-%d %H:%M:%S')}
Event: {event_type}
Message: {message}
Result: {result}
==============================
"""

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    print(log_entry)
