favorite_numbers = {
    'alice': [7, 12],
    'bob': [4, 8, 15, 16],
    'carol': [3],
    'dave': [16, 2, 23],
    'sam': [9, 5],
    }

for key, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"\n{key.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"\t{number}")
    else:
        print(f"\n{key.title()}'s favorite number is:")
        print(f"\t{numbers[0]}")