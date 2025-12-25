"""
Often, you’ll need to test more than two possible situations,
and to evaluate these you can use Python’s if-elif-else
syntax. Python executes only one block in an if-elif-else
chain. It runs each conditional test in order, until one
passes. When a test passes, the code following that test is
executed and Python skips the rest of the tests
"""

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif 4 < age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


age = 12
if age < 4:
    price = 0
elif 4 < age < 18:
    price = 25
elif 18 <= age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")


age = 12
if age < 4:
    price = 0
elif 4 < age < 18:
    price = 25
elif 18 <= age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")