'''
allows users to change their password
has some issues at the moment
'''
import argon2
import json
from user_login import prompt_password_login, prompt_username_login, login

json_file = 'test.json'

def argon2_function(password):
    ph = argon2.PasswordHasher()
    hashed_password = ph.hash(password)
    return hashed_password

def update_user_db(db_file, username, new_digest):
    with open(db_file, 'r+') as db:
        user_db = json.load(db) # user db shows as a dict w/ only the 'user_pairs' key
        if username in user_db:
            print("CHANGING PASSWORD.....")
            updated_pair = {
                username:new_digest
            }
            user_db.update(updated_pair)
            db.seek(0)
            json.dump(user_db, db, indent=4)
        else:
            print("USER DOES NOT EXIST")

def prompt_password():
    password = input("CURRENT PASSWORD:                 ")
    return password

def prompt_username():
    username = input("USERNAME:       ")
    return username

def get_new_password():
    change_pass = input("CHANGE PASSWORD (YES/NO)?:     ")
    if change_pass == "Yes" or "YES" or "yes":
        password = input("NEW PASSWORD:                 ")
        return password
    else:
        print("OK...PASSWORD NOT CHANGING")
        return False

def main():

    username = prompt_username_login()
    password = prompt_password_login()
    login_attempt = login(json_file, username, password)

    if login_attempt == True:
        print("LOGIN SUCCESS")
        new_password = get_new_password()
        if new_password == False:
            print("GOODBYE")
        else:
            new_digest = argon2_function(new_password)
            update_user_db(json_file, username, new_digest)
            print("PASSWORD CHANGED")
    elif login_attempt == False:
        print("LOGIN FAILED")
        return False
    else:
        print("SOMETHING ELSE")

if __name__ == "__main__":
    main()



        


