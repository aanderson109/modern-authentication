# modern authentication

**Overview**: goal is to design an authentication system that utilizes best practices for cryptography. solution should let users register with a username/password combo, login, reset and change their password.

*Disclaimer*: values used in the argon2 cipher aren't very secure; you would need to change those.

**What's Here**
* `register_user.py` --> lets users create a username and password. stores that password in the .json file after using argon2.
* `user_login.py` --> lets users login using their username and password. Under the hood, it basically rehashes the password and compares it to what is in the .json file.
* `change_password.py` --> lets users change their password and stores that in the .json file. It works, but it actually won't let you choose NOT to change the password so.....there is that.
* `reset_password.py` --> lets users reset their password entirely. Super dangerous right now since it basically doesn't require anyone to authenticate themselves. Needs more work to be a real solution.
* `test.json` --> the local database-type thing for all the username:digest pairs.
