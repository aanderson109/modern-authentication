# modern authentication

**Overview**: My goal is to design an authentication system that utilizes best practices for cryptography. Ideally, the solution shouold let users register with a username/password combo, lets them login, reset their password, and change their password.

**Current Status**: It's barely in its infancy. It isn't really the most secure or even really optimized, but it does use Argon2 for storing the passwords which is fun.

*Disclaimer*: I didn't input most of the values that actually make using argon2 secure. I'll do that later (maybe), but just a heads up.

**What's Here**: The files are loosely organized and need to be blended; however, here is a rundown:
* `register_user.py` --> lets users create a username and password. Stores that password in the .json file after using argon2.
* `user_login.py` --> lets users login using their username and password. Under the hood, it basically rehashes the password and compares it to what is in the .json file.
* `change_password.py` --> lets users change their password and stores that in the .json file. It works, but it actually won't let you choose NOT to change the password so.....there is that.
* `reset_password.py` --> lets users reset their password entirely. Super dangerous right now since it basically doesn't require anyone to authenticate themselves. Needs more work to be a real solution.
* `test.json` --> the local database-type thing for all the username:digest pairs.