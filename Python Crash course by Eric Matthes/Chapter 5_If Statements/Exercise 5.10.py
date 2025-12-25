current_users = ['admin', 'john', 'sarah', 'mike', 'anna']

new_users = ['david', 'Maria', 'JOHN', 'saraH', 'linda']

for user in new_users:
    if user.lower() in current_users:
        print(f"Sorry {user}, that username is already taken. Please enter a new username.")

    else:
        print(f"Great, {user} is still available.")