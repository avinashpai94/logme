def get_credentials():
    file_path = "credentials/credentials.txt"
    filep = open(file_path, "r")
    creds = filep.read().split(',')
    email = creds[0].split(':')[1]
    accesstoken = creds[1].split(':')[1][:-2]
    return (email, accesstoken)
