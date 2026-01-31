from pathlib import Path
import json


def get_favourite_number(path):
    """Retrieve users favourite number if stored"""
    if path.exists():
        contents = path.read_text()
        favourite_number = json.loads(contents)
        return favourite_number
    else:
        return None

def ask_favourite_number(path):
    """Ask users for their favourite number and store it"""
    favourite_number = input("Enter your favourite number? ")
    path.write_text(json.dumps(favourite_number))
    print("We'll remember your favourite number when you come back!")
    return favourite_number

def remember_favourite_number(path):
    if path.exists():
        # Read the favourite number from the file
        favourite_number = get_favourite_number(path)
        print(f"I know your favourite number! It's {favourite_number}.")
    else:
        # Ask the user for their favourite number and store it
        ask_favourite_number(path)


remember_favourite_number(Path('favourite_number.json'))