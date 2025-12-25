person_0 ={'first_name': 'tamilore',
           'last_name': 'adeyemi',
           'age': 18,
           'city': 'lagos'
           }

print("Person Information:")
print(f"first name: {person_0['first_name'].title()} ")
print (f"last name: {person_0['last_name'].title()}")
print(f"age: {person_0['age']} ")
print(f"city: {person_0['city'].title()}\n")





print("Person Information:")
for key in person_0:
    if key != 'age':
        print(f"{key}: {person_0[key].title()}")
    else:
        print(f"{key}: {person_0[key]}")

