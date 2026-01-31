"""
Let’s refactor greet_user() so it’s not doing so many
different tasks. We’ll start by moving the code for retrieving
a stored username to a separate function
"""

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
    
def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        path.write_text(json.dumps(username))
        print(f"We'll remember you when you come back, {username}!")

greet_user()


"""
 This is good practice: a function
should either return the value you’re expecting, or it should
return None. This allows us to perform a simple test with the
return value of the function. 
"""