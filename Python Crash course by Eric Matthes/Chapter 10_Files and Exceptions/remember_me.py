"""
Saving data with json is useful when you’re working with
user-generated data, because if you don’t store your user’s
information somehow, you’ll lose it when the program stops
running. 

Let’s look at an example where we prompt the user
for their name the first time they run a program and then
remember their name when they run the program again
"""

from pathlib import Path
import json

username = input("What is your name? ")

path = Path("username.json")
path.write_text(json.dumps(username))

print(f"We'll remember you when you come back, {username}!")