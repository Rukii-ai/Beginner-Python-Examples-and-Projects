first_number = input("\n Enter first number: ")
second_number = input(" Enter second number: ")

try:
    result = int(first_number) + int(second_number)
except ValueError:
    print("One of the inputs is not a number. Please enter valid numbers.")
else:
    print(f"The result is: {result}")