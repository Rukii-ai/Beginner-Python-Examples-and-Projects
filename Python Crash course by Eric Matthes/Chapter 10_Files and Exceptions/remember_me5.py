from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username and store it"""
    username = (input("What is your name? "))
    path.write_text(json.dumps(username))
    return username
    
def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()


"""
Each function in this final version of remember_me.py has
a single, clear purpose. 

We call greet_user(), and that
function prints an appropriate message: it either welcomes
back an existing user or greets a new user. It does this by
calling get_stored_username(), which is responsible only for
retrieving a stored username if one exists. 

Finally, if
necessary, greet_user() calls get_new_username(), which is
responsible only for getting a new username and storing it.
This compartmentalization of work is an essential part of
writing clear code that will be easy to maintain and extend
"""