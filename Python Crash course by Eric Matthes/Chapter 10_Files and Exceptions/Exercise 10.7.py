print("Enter any two numbers, and I'll add them together.")
print("Enter 'q' to quit at any time.")

while True:
    first_number = input("\n Enter first number: ")
    if first_number.lower() == 'q':
        break
    second_number = input(" Enter second number: ")
    if second_number.lower() == 'q':
        break
    
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("One of the inputs is not a number. Please enter valid numbers.")
    else:
        print(f"The result is: {result}")