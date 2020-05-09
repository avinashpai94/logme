def get_credentials():
    file_path = "credentials/credentials.txt"
    filep = open(file_path, "r")
    creds = filep.read().split(',')
    email = creds[0].split(':')[1][1:-1]
    accesstoken = creds[1].split(':')[1][1:-3]
    print(email, accesstoken)
    return (email, accesstoken)

get_credentials()
