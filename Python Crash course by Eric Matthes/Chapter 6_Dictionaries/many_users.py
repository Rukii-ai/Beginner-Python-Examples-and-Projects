"""
You can nest a dictionary inside another dictionary, but your
code can get complicated quickly when you do
"""

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")

    print(f"\tFull name: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"\tLocation: {user_info['location'].title()}")