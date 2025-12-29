"""You can prompt for as much input as you need in each pass
through a while loop. Let’s make a polling program in which
each pass through the loop prompts for the participant’s
name and response."""

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #  Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name.title().strip()] = response.strip().title()

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower().strip() == 'no':
        polling_active = False
        break
    elif repeat.lower().strip() != 'yes' and repeat.lower().strip() != 'no':
        print("Please enter a valid response: 'yes' or 'no'.")

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title().strip()} would like to climb {response.title().strip()}.")