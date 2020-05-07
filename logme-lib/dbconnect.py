# Rename async.py to asyncn.py. Modified the file name in venv/lib/site-packages/_init_.py and firebase.py
# Rename crypto folder in venv/lib/site-packages/ to Crypto

from firebase import Firebase

# From Firebase - settings - project settings
config = {
  "apiKey": "AIzaSyA4UPj1_g5KDqMPTkVPqF4Kh7S1dnIgU0Q",
  "authDomain": "errorlogger-c8536.firebaseapp.com",
  "databaseURL": "https://errorlogger-c8536.firebaseio.com",
  "storageBucket": "errorlogger.appspot.com",
  "serviceAccount": "C:/Users/anj24/Downloads/errorlogger-d5dc9028e1af.json"
}

def save(data_dic):
    firebase = Firebase(config)
    db = firebase.database()
    email = data_dic['email'].split('@')[0]
    accesstoken = data_dic['accesstoken']
    timestamp = int(data_dic['timestamp'])
    keys_remove = ['email', 'accesstoken', 'timestamp']
    for key in keys_remove:
        del data_dic[key]
    db.child(email).child(accesstoken).child(timestamp).set(data_dic)
