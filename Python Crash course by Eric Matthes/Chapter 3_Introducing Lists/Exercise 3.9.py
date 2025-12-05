guests = ['Albert Einstein', 'Isaac Newton', 'Marie Curie']

print(f"Goodday {guests[0]}. I would like to invite you to a dinner I'm hosting this evening")
print(f"Goodday {guests[1]}. I'm hosting a dinner this evening, and I'd love you to be in attendance")
print(f"Goodday {guests[2]}. Would you like to come have dinner with me this evening")

print(f"{guests[1]} has confirmed he can not make it for the dinner this evening, so I will be inviting another guest instead.")

guests[1] = 'Galileo Galilei'

print(f"Goodday {guests[0]}. I would like to invite you to a dinner I'm hosting this evening")
print(f"Goodday {guests[1]}. I'm hosting a dinner this evening, and I'd love you to be in attendance")
print(f"Goodday {guests[2]}. Would you like to come have dinner with me this evening")

print(f"A larger dinner table has been found, so three more guests can be invited to the dinner this evening.")

guests.insert(0, 'Nikola Tesla')
guests.insert(2, 'Charles Darwin')
guests.append('Ada Lovelace')

print(f"Goodday {guests[0]}. I would like to invite you to a dinner I'm hosting this evening")
print(f"Goodday {guests[1]}. I'm hosting a dinner this evening, and I'd love you to be in attendance")
print(f"Goodday {guests[2]}. Would you like to come have dinner with me this evening")
print(f"Goodday {guests[3]}. I plan to host an amazing dinner this evening, and your presence would make it even better.")
print(f"Goodday {guests[4]}. It would be an honor to have you at the dinner I'm hosting this evening.")
print(f"Goodday {guests[5]}. I warmly invite you to join me for a special dinner this evening.")

print(f"The number of guests I can invite to dinner now with this large table is: {len(guests)}")