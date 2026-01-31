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

    confirmation = input(f"is your username {username}? (y/n) ")

    if confirmation.lower() == 'y':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
