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

from flask import Flask,jsonify,request
import pymysql

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

db_user="root"
db_password="root"
db_name="clouddb"
db_connection_name="errorlogger:us-west4:loggerdb"

app = Flask(__name__)


@app.route('/')
def homepage():
    return(jsonify("hi"))

@app.route('/history')
def getHistory():
    # When deployed to App Engine, the `GAE_ENV` environment variable will be
    # set to `standard`
    if os.environ.get('GAE_ENV') == 'standard':
        # If deployed, use the local socket interface for accessing Cloud SQL
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
    else:
        # If running locally, use the TCP connections instead
        # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
        # so that your application can use 127.0.0.1:3306 to connect to your
        # Cloud SQL instance
        host = '127.0.0.1'
        host="34.125.50.185"
        cnx = pymysql.connect(user=db_user, password=db_password,
                              host=host, db=db_name)
    accesstokens = request.args.get('accesstokens')
    number = request.args.get('n')
    # print(username)
    # print("num",number)
    with cnx.cursor() as cursor:

        num=int(number)
        print(type(num))
        query="SELECT * FROM Notifications where accesstokens=" + accesstokens + "order by time LIMIT %s"
               # LIMIT %s"""%num
        data= (num)
        #query = ("SELECT * from Notifications where accesstokens='"+ username +"'order by time;")
        #print(query)
        cursor.execute(query,data)
        print(query)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        dict_results={}

        for result in rv:

          dict_results=dict(zip(row_headers,result))
          print('dicresult',dict_results)
          dict_results['sent']=dict_results['sent'].decode('utf-8')

          dict_results['time']=str(dict_results['time'])
          print('dicresult',dict_results)
          if dict_results['sent'] =='\x00':
            dict_results['sent']='False'
          else:
            dict_results['sent']='True'
          json_data.append(dict_results)
          #print(json_data)

    cnx.close()
    return (jsonify(json_data))

@app.route('/recent')
def getRecent():
    # When deployed to App Engine, the `GAE_ENV` environment variable will be
    # set to `standard`
    if os.environ.get('GAE_ENV') == 'standard':
        # If deployed, use the local socket interface for accessing Cloud SQL
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
    else:
        # If running locally, use the TCP connections instead
        # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
        # so that your application can use 127.0.0.1:3306 to connect to your
        # Cloud SQL instance
        host = '127.0.0.1'
        host="34.125.50.185"
        cnx = pymysql.connect(user=db_user, password=db_password,
                              host=host, db=db_name)
    accesstokens = request.args.get('accesstokens')
    #number = request.args.get('n')
    # print(username)
    # print("num",number)
    with cnx.cursor() as cursor:

        # num=int(number)
        # print(type(num))
        query="SELECT * FROM Notifications where accesstokens=" + accesstokens + "and sent=0 order by time"
               # LIMIT %s"""%num
        #data= (num)
        #query = ("SELECT * from Notifications where accesstokens='"+ username +"'order by time;")
        #print(query)
        cursor.execute(query)
        print(query)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        dict_results={}

        for result in rv:

          dict_results=dict(zip(row_headers,result))
          print('dicresult',dict_results)
          dict_results['sent']=dict_results['sent'].decode('utf-8')

          dict_results['time']=str(dict_results['time'])
          print('dicresult',dict_results)
          if dict_results['sent'] =='\x00':
            dict_results['sent']='False'
          else:
            dict_results['sent']='True'
          json_data.append(dict_results)
          #print(json_data)

    cnx.close()
    return (jsonify(json_data))

# [END gae_python37_cloudsql_mysql]


if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
    #app.run(debug=True)
