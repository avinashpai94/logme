import pub
import json
import uuid
from datetime import datetime
import threading

project_id = "errorlogger"
topic_name = "log-message"

def log_send(level, timestamp, key, message):
    data_dic = {}
    data_dic['level'] = level
    data_dic['timestamp'] = timestamp
    data_dic['key'] = key
    data_dic['message'] = message
    data_dic['access_token'] = uuid.uuid1().hex
    data = json.dumps(data_dic)
    print(data)
    pub.send_message(project_id, topic_name, data)

def debug(key, message):
    level = 3
    dateTime = datetime.now()
    timestamp = dateTime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    x = threading.Thread(target=log_send, args=[level, timestamp, key, message])
    x.start()

def alert(key, message):
    level = 2
    dateTime = datetime.now()
    timestampStr = dateTime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    x = threading.Thread(target=log_send, args=[level, timestamp, key, message])
    x.start()

def warning(key, message):
    level = 1
    dateTime = datetime.now()
    timestampStr = dateTime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    x = threading.Thread(target=log_send, args=[level, timestamp, key, message])
    x.start()

def error(key, message):
    level = 0
    dateTime = datetime.now()
    x = threading.Thread(target=log_send, args=[level, timestamp, key, message])
    x.start()

log_send(1, "timestamp", "key", "message")
# logme.log_send(level, timestamp, key, message)
# This is the base function. Write code here to retrieve access token from file system and merge it with all of the input and send to cloud queue as json.
#
# All below functions should call base function as a seperate thread so as to not stop execution on caller function
# logme.debug(key, message)
# User provided key, message. Set level as 3. And call log_send function with current time stamp.
#
# logme.alert(key, message)
# User provided key, message. Set level as 2. And call log_send function with current time stamp.
#
# logme.warning(key, message)
# User provided key, message. Set level as 1. And call log_send function with current time stamp.
#
# logme.error(key, message)
# User provided key, message. Set level as 0. And call log_send function with current time stamp.

#base(1, "Anjali", "ilovefood")
