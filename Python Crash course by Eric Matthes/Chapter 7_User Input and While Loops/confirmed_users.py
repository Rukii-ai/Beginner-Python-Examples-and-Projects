"""
A for loop is effective for looping through a list, but you
shouldn’t modify a list inside a for loop because Python will
have trouble keeping track of the items in the list. To modify
a list as you work through it, use a while loop. Using while
loops with lists and dictionaries allows you to collect, store,
and organize lots of input to examine and report on later.
"""

# Start with users that need to be verified, 
# and an empty list to hold confirmed users. 

unconfirmed_users = ['alice', 'brian', 'candace'] 
confirmed_users = [] 

# Verify each user until there are no more unconfirmed users. 
#  Move each verified user into the list of confirmed users.
# The while loop runs as long as the list unconfirmed_users is not empty
while unconfirmed_users: 
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())