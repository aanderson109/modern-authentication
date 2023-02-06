'''
Logs user in, creates a hash of their password using argon2, and stores that into the .json
'''
import argon2
import json

json_file = 'test.json'

ph = argon2.PasswordHasher()

def login(json_file, username, password):

    with open(json_file, 'r') as file:
        user_db = json.load(file)
        if username in user_db:
            try:
                ph.verify(user_db[username], password)
                return True
            except:
                return False

def prompt_username_login():
    login_username = input("USERNAME:       ")
    return login_username

def prompt_password_login():
    login_password = input("PASSWORD:       ")
    return login_password

def main():
    user = prompt_username_login()
    password = prompt_password_login()
    login_attempt = login(json_file, user, password)
    if login_attempt == True:
        print("LOGIN SUCCESS")
        return True
    elif login_attempt == False:
        print("LOGIN FAILED")
        return False
    else:
        print("SOMETHING ELSE")
    
if __name__=="__main__":
    main()


