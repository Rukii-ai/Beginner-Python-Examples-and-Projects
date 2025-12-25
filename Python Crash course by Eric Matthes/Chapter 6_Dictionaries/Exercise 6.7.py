person_0 ={'first_name': 'tamilore',
           'last_name': 'adeyemi',
           'age': 18,
           'city': 'lagos'
           }

person_1 ={'first_name': 'john',
           'last_name': 'doe',
           'age': 25,
            'city': 'new york'
            }

person_2 ={'first_name': 'jane',
            'last_name': 'smith',
            'age': 30,
            'city': 'chicago'
            }

people = [person_0, person_1, person_2]

for person in people:
    print(f"\nPerson Information of {person['first_name'].title()}:")
    
    for key in person:
        if key != 'age':
            print(f"{key}: {person[key].title()}")
        else:
            print(f"{key}: {person[key]}")
    