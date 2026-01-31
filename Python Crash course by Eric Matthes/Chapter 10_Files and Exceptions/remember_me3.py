"""
Often, you’ll come to a point where your code will work, but
you’ll recognize that you could improve the code by
breaking it up into a series of functions that have specific
jobs. 

This process is called refactoring. Refactoring makes
your code cleaner, easier to understand, and easier to
extend.

We can refactor remember_me.py by moving the bulk of
its logic into one or more functions. The focus of
remember_me.py is on greeting the user, so let’s move all
of our existing code into a function called greet_user()
"""

from pathlib import Path
import json

def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        path.write_text(json.dumps(username))
        print(f"We'll remember you when you come back, {username}!")

greet_user()


"""
Because we’re using a function now, we rewrite the
comments as a docstring that reflects how the program
currently works. 

This file is a little cleaner, but the
function greet_user() is doing more than just greeting the
user—it’s also retrieving a stored username if one exists and
prompting for a new username if one doesn’t.
"""
