'''
Registers user; part of the Authentication System
'''
from random import randint
import argon2
import json

json_file = 'test.json'

# function to create digest of password using argon2
def argon2_function(password):
    ph = argon2.PasswordHasher()
    hashed_password = ph.hash(password)
    return hashed_password

# function to ask user for password, username
def prompt_username():
    username = input("USERNAME:     ")
    return username

def prompt_password():
    password = input("PASSWORD:     ")
    return password

def store_user_info(username, salted_password_digest):
    
    user_passwd_pair = {
        username:salted_password_digest
    }

    with open(json_file, 'r+') as file:
        # loads existing data into a dictionary
        user_db = json.load(file)
        if username in user_db:
            new_username = username + str(randint(0, 999))
            updated_pair = {
                new_username:salted_password_digest
            }
            user_db.update(updated_pair)
            print("ACCOUNT CREATED")
            print("YOUR USERNAME:   ", new_username)
            file.seek(0)
            json.dump(user_db, file, indent=4)
            
        else:
            print("ACCOUNT CREATED")
            user_db.update(user_passwd_pair)
            file.seek(0)
            json.dump(user_db, file, indent=4)
    
def main():
    username = prompt_username()
    password = prompt_password()
    hashed_password = argon2_function(password)
    store_user_info(username, hashed_password)

if __name__=="__main__":
    main()






'''
class register_user():

    def __init__(self):
        pass
       # self.usrname = usrname
       # self.passwd = passwd
       # self.data_store = data_store
    
    def get_username(self):
        print("\nplease enter a username:   ")
        self.usrname = input()
        return self.usrname
    
    def get_password(self):
        print("\nplease enter a password:   ")
        self.passwd = input()
        return self.passwd
    
    
user = register_user().get_username()
password = register_user().get_password()

print(user)
print(password)
'''


#def register_user(usrname, passwd):
