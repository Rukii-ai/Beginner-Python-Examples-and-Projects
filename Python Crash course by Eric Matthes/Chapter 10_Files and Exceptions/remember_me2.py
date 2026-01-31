"""We need to combine these two programs, remember_me.py and greet_user.py
into one file.

When someone runs remember_me.py, we want to retrieve
their username from memory if possible; if not, we’ll prompt
for a username and store it in username.json for next time.
We could write a try-except block here to respond
appropriately if username.json doesn’t exist, but instead
we’ll use a handy method from the pathlib module:
"""

from pathlib import Path
import json

path = Path("username.json")
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
    print(f"We'll remember you when you come back, {username}!")


"""
There are many helpful methods you can use with Path
objects. The exists() method returns True if a file or folder
exists and False if it doesn’t. Here we use path.exists() to
find out if a username has already been stored 

This is the output you see if the program was already run
at least once. Even though the data in this section is just a
single string, the program would work just as well with any
data that can be converted to a JSON-formatted string.
"""