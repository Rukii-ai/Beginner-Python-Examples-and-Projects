dog = {
    'kind': 'canine',
    'owner': 'Alice',
    }

cat = {
    'kind': 'feline',
    'owner': 'Bob',
    }

parrot = {
    'kind': 'avian',
    'owner': 'Carol',
    }

rabbit = {
    'kind': 'lagomorph',
    'owner': 'Dave',
    }

pets = [dog, cat, parrot, rabbit]

for pet in pets:
    print(f"\nPet details:")

    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")