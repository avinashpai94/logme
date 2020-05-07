import pub
import json
import credentials
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
    data_dic['email'], data_dic['accesstoken'] = credentials.get_credentials()
    data = json.dumps(data_dic)
    print(data)
    pub.send_message(project_id, topic_name, data)

def debug(key, message):
    level = 3
    ts = datetime.now().timestamp()
    x = threading.Thread(target=log_send, args=[level, ts, key, message])
    x.start()

def alert(key, message):
    level = 2
    ts = datetime.now().timestamp()
    x = threading.Thread(target=log_send, args=[level, ts, key, message])
    x.start()

def warning(key, message):
    level = 1
    ts = datetime.now().timsetamp()
    x = threading.Thread(target=log_send, args=[level, ts, key, message])
    x.start()

def error(key, message):
    level = 0
    ts = datetime.now().timestamp()
    x = threading.Thread(target=log_send, args=[level, ts, key, message])
    x.start()


debug("DEBUG ERROR", "debug message")
