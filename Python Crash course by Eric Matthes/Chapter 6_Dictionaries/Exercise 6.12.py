users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'Date of Birth': 'March 14, 1879'
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'Date of Birth': 'November 7, 1867'
        },
    'jnewton': {
        'first': 'isaac',
        'last': 'newton',
        'location': 'cambridge',
        'Date of Birth': 'January 4, 1643'
        },
    'ggalileo': {
        'first': 'galileo',
        'last': 'galilei',
        'location': 'pisa',
        'Date of Birth': 'February 15, 1564'
        },
    'ctesla': {
        'first': 'nikola',
        'last': 'tesla',
        'location': 'smiljan',
        'Date of Birth': 'July 10, 1856'
        },
    }



for username, user_info in users.items():
    print(f"\nDetailed information for user {username} is listed below:")

    print(f"\tFull name: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"\tBorn on {user_info['Date of Birth']} at {user_info['location'].title()}")

for username, user_info in users.items():
    print(f"\nDetailed information for user {username} is listed below:")

    for key, value in user_info.items():
        print(f"\t{key}: {value.title()}")
