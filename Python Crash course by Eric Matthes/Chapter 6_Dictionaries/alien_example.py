# Make an empty list for storing aliens.

aliens = []

# Make 30 green aliens. 
# Will start with alien number 0 and stop before alien number 30.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

print("...") # Indicate that there are more aliens to show

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


"""
It’s common to store a number of dictionaries in a list
when each dictionary contains many kinds of information
about one object. For example, you might create a
dictionary for each user on a website, as we did in user.py
on page 99, and store the individual dictionaries in a list
called users. All of the dictionaries in the list should have an
identical structure, so you can loop through the list and
work with each dictionary object in the same way
"""