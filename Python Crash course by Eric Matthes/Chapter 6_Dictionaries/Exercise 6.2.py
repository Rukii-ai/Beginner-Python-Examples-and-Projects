favorite_numbers = {
    'alice': 7,
    'bob': 4,
    'carol': 3,
    'dave': 16,
    'sam': 9,
    }


print("Everyone's favourite numbers are:")
print(f"Alice's favorite number is {favorite_numbers['alice']}.")
print(f"Bob's favorite number is {favorite_numbers['bob']}.")
print(f"Carol's favorite number is {favorite_numbers['carol']}.")
print(f"Dave's favorite number is {favorite_numbers['dave']}.")
print(f"Sam's favorite number is {favorite_numbers['sam']}\n.")



print("Everyone's favourite numbers are:")
for key in favorite_numbers:
    print(f"{key.title()}'s favorite number is {favorite_numbers[key]}.")