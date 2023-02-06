'''
allows users to reset their password
has issues/isn't very secure right now
'''
import argon2
import json
json_file = 'test.json'

def argon2_function(password):
    ph = argon2.PasswordHasher()
    hashed_password = ph.hash(password)
    return hashed_password

def update_user_db(db_file, username, new_digest):
    with open(db_file, 'r+') as db:
        user_db = json.load(db) # user db shows as a dict w/ only the 'user_pairs' key
        if username in user_db:
            print("CHANGING PASSWORD...")
            updated_pair = {
                username:new_digest
            }
            user_db.update(updated_pair)
            db.seek(0)
            json.dump(user_db, db, indent=4)
            print("PASSWORD CHANGED")
        else:
            print("USER DOES NOT EXIST")

def prompt_password():
    password = input("ENTER NEW PASSWORD:     ")
    return password

def prompt_username():
    username = input("USERNAME:     ")
    return username

def prompt_for_reset():
    user_reset = input("RESET PASSWORD (YES/NO)?:       ")
    if user_reset == "YES" or "yes" or "Yes":
        return True
    elif user_reset == "NO" or "No" or "no":
        print("OK. NO RESET")
        return False

def main():
    username = prompt_username()
    reset_question = input("RESET PASSWORD (YES/NO)?:       ")
    print(reset_question)
    if reset_question == "YES" or "Yes" or "yes":
        password = prompt_password()
        new_digest = argon2_function(password)
        update_user_db(json_file, username, new_digest)
    elif reset_question == "NO" or "No" or "no":
        print("GOODBYE")

if __name__=="__main__":
    main()


        


