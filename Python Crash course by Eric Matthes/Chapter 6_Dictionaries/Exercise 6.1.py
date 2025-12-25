person_0 ={'first_name': 'tamilore',
           'last_name': 'adeyemi',
           'age': 18,
           'city': 'lagos'
           }

for key in person_0:
    if key != 'age':
        print(f"{key}: {person_0[key].title()}")
    else:
        print(f"{key}: {person_0[key]}")

