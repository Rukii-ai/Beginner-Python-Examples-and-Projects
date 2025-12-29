responses = {}

poll_active = True

while poll_active:
    name = input("\nWhat is tour name? ")
    response = input("If you could visit one place in the world,"
                     "where would you go? ")
    
    responses[name.title().strip()] = response.strip().title()

    repeat = input("Would you like to let another person respond? (yes/no) ")
    
    if repeat.lower().strip() == 'no':
        poll_active = False
    
    elif repeat.lower().strip() != 'yes' and repeat.lower().strip() != 'no':
        print("Please enter a valid response: 'yes' or 'no'.")

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title().strip()} would like to visit {response.title().strip()}.")

print(responses)