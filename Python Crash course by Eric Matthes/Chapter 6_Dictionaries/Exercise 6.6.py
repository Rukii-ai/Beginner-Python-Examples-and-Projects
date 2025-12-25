favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

poll_list = ['jen', 'sarah','erin', 'mike', 'edward', 'anna', 'phil', 'tom']

for name in poll_list:
    if name in favorite_languages:
        print(f"Thank you {name.title()} for taking the poll.")
    else:
        print(f"{name.title()}, please take our poll.")


for name in sorted(poll_list):
    if name in favorite_languages:
        print(f"Thank you {name.title()} for taking the poll.")
    else:
        print(f"{name.title()}, please take our poll.")


