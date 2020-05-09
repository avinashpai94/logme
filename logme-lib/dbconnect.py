# Rename async.py to asyncn.py. Modified the file name in venv/lib/site-packages/_init_.py and firebase.py
# Rename crypto folder in venv/lib/site-packages/ to Crypto

from firebase import Firebase
import hashlib

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
    email = data_dic['email']
    email = hashlib.md5(email.encode()).hexdigest()
    print(email)
    accesstoken = data_dic['accesstoken']
    print(accesstoken)
    if accesstoken in db.child("users").child(email).shallow().get().val():
        print("User and Access Token Exist")
        ts_md5 = data_dic['timestamp'][0]
        ts = data_dic['timestamp'][1]
        keys_remove = ['email', 'timestamp']
        for key in keys_remove:
            del data_dic[key]
        data_dic['timestamp'] = ts
        device_name = db.child("devices").child(accesstoken).shallow().get().val()
        if device_name:
            data_dic['device'] = device_name
        else:
            data_dic['device'] = "Device does not exist"
        db.child("users").child(email).child(accesstoken).child(ts_md5).set(data_dic)
    else:
        print("User and Access Token does not exist")
# firebase = Firebase(config)
# db = firebase.database()
# print(db.child("users").child("9f63c41218def117d2017a8f83d1a770").shallow().get().val())

#db.child('users').child('9f63c41218def117d2017a8f83d1a770').update({'0c50e2c77928995f8e9ac398a42168ce':0})
