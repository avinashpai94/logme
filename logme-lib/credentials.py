import json
def get_credentials():
    file_path = "credentials/credentials.txt"
    filep = open(file_path, "r")
    creds = filep.read()
    creds_json = json.loads(creds)
    email, accesstoken = creds_json['email'], creds_json['accesstoken']
    return (email, accesstoken)
