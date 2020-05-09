# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_cloudsql_mysql]
import os
import hashlib
#from firebase import Firebase
from flask import Flask,jsonify,request,Response
from firebase import Firebase
from datetime import datetime
import time
import json

config = {
  "apiKey": "AIzaSyA4UPj1_g5KDqMPTkVPqF4Kh7S1dnIgU0Q",
  "authDomain": "errorlogger-c8536.firebaseapp.com",
  "databaseURL": "https://errorlogger-c8536.firebaseio.com",
  "storageBucket": "errorlogger.appspot.com",
  "serviceAccount": "./firebase_key/errorlogger-d5dc9028e1af.json"
}



app = Flask(__name__)
firebase = Firebase(config)
db = firebase.database()


@app.route('/')
def homepage():
    return(jsonify("Welcome"))

@app.route('/add_device',methods=['GET'])
def getkey():
    # When deployed to App Engine, the `GAE_ENV` environment variable will be
    # set to `standard`

    email = request.args.get('email')
    device= request.args.get('device')

    email_obj = hashlib.md5(email.encode())
    email_hex=email_obj.hexdigest()


    timestamp=datetime.utcnow()
    email_time=str(email)+str(timestamp)
    access_obj = hashlib.md5(email_time.encode())
    access_hex=access_obj.hexdigest()


    if not db.child('users').child(email_hex).shallow().get().val(): # if email doesn't exist

       #create email and access token
        db.child('users').update({email_hex:
                {
                   access_hex:0
                }

        })
    else:
        #create access token
        db.child('users').child(email_hex).update(
                   {
                      access_hex:0
                   }

         )


    device_data={access_hex:device}

    db.child('devices').update(device_data)

    js = json.dumps(device_data)
     # statusval=200

    # else:
    #  print("users exist")
    #  device_data={'User already exists':''}
    # js = json.dumps(device_data)
     # statusval=400

    # resp = Response(js, status=statusval, mimetype='application/json')
    # resp.headers['Link'] = 'http://127.0.0.1:5000/add_device?email='+email+'&device='+device
    return(js)



#no need to use
@app.route('/getaccesstoken')
def getaccesstoken():
    # When deployed to App Engine, the `GAE_ENV` environment variable will be
    # set to `standard`

    email = request.args.get('email')
    timestamp=datetime.utcnow()
    #timestamp=time.time()
    email_time=str(email)+str(timestamp)
    #print(type(email_time))
    hash_obj = hashlib.md5(email_time.encode())
    return(jsonify(hash_obj.hexdigest()))



def getnotifications(email_hex):
       dict_accesstokens=db.child('users').child(email_hex).get().val() #get accesstokens, will have one accesstoken fro sure
       print("dictvalues",dict_accesstokens.values())
       accessVal_List=dict_accesstokens.values() #values of accesstokens, could be [0,0,{ts:{}}]
       result_array=[]

       # for key, value in dict_accesstokens.items():
       #  for item in accessVal_List: #item--> [0,0, {ts:{}}]
       #    print("item",item)
       #    if(item!=0):                           #timestamp values exists
       #     for val in item.values():  #val--> {device:0, level:1, msgs:"warning"}
       #       result_array.append(val)

       for access_hex, values in dict_accesstokens.items():
           for item in values: #item--> [0,0, {ts:{}}]
               print("access_token",access_hex)
               if(item!=0):                           #timestamp values exists
                  for val in item.values():  #val--> {device:0, level:1, msgs:"warning"}
                    result_array.append(val)
                    db.child('users').child(email_hex).update(
                        {
                          access_hex:0
                        })


       return(result_array) #no quotes email

@app.route('/unread')
def unread():
    email = request.args.get('email')
    email_obj = hashlib.md5(email.encode())
    email_hex=email_obj.hexdigest()
    if not db.child('users').child(email_hex).shallow().get().val(): #email doesnt exist
      #db.setValue(hash_hex);
        return ("User doesn't exist")
    def event_stream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(getnotifications(email_hex))
    return flask.Response(event_stream(), mimetype="text/event-stream")



if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
    #app.run(debug=True)
