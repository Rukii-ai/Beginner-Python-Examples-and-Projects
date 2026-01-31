from pathlib import Path
import json

def retrieve_user_data(path):
    """Retrieve stored user data"""
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return None
    
def display_user_data(path):
    """Display stored user data"""
    user_data = retrieve_user_data(path)
    if user_data:
        print(f"Welcome back, {user_data['Username']}!")
        print("Here's what we know about you:")
        for key, value in user_data.items():
            print(f"{key}: {value}")
    else:
        store_user_data(path)
        
def store_user_data(path):
    """Ask new users for their data and store it"""
    username = input("Enter your username: ")
    age = input("Enter your age: ")
    school = input("Enter your school name: ")
    user_data = {
        'Username': username,
        'Age': age,
        'School': school
    }
    path.write_text(json.dumps(user_data))
    print("Your data has been stored!")

def greet_user(path=Path("user_data.json")):
    """Greet the user and display a summary of all we know about the user."""
    display_user_data(path)


greet_user()