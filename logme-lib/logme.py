import pub
import json
import credentials
from datetime import datetime
import threading
import hashlib
from uuid import uuid4

project_id = "errorlogger"
topic_name = "log-message"

def log_send(level, timestamp, key, message):
    data_dic = {}
    data_dic['level'] = level
    ts_md5 = hashlib.md5((str(timestamp) + str(uuid4().hex[:8])).encode()).hexdigest()
    data_dic['timestamp'] = [ts_md5, timestamp]
    data_dic['key'] = key
    data_dic['message'] = message
    data_dic['email'], data_dic['accesstoken'] = credentials.get_credentials()
    data = json.dumps(data_dic)
    print(data)
    pub.send_message(project_id, topic_name, data)

def debug(key, message):
    level = "debug"
    ts = datetime.now().timestamp()
    x = threading.Thread(target=log_send, args=[level, ts, key, message])
    x.start()

def alert(key, message):
    level = "alert"
    ts = datetime.now().timestamp()
    x = threading.Thread(target=log_send, args=[level, ts, key, message])
    x.start()

def warning(key, message):
    level = "warning"
    ts = datetime.now().timestamp()
    x = threading.Thread(target=log_send, args=[level, ts, key, message])
    x.start()

def error(key, message):
    level = "error"
    ts = datetime.now().timestamp()
    x = threading.Thread(target=log_send, args=[level, ts, key, message])
    x.start()


debug("DEBUG ERROR", "debug message")
alert("ALERT", "alert message")
warning("WARNING", "warning message")
error("ERROR", "error message")
