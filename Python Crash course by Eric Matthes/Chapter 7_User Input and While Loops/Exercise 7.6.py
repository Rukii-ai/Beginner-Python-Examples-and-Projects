prompt = "\nBefore we grant you access to the movie theatre please supply your age"
prompt += "\nEnter 'quit' when you'd like to stop the program "

active = True

while active:
    answer = input(prompt).strip()

    # Check if the input is a number, reads false for strings, floats, and negative numbers
    if answer.isdigit(): 
        age = int(answer)

        if age < 3:
            print(f"\nFor the {age} yr old. The ticket is free!")
        elif 3 <= age <= 12:
            print(f"\nFor the {age} yr old a ticket will be $10")
        elif age > 12:
            print(f"\nFor the {age} yr old a ticket will be $15")
    
    elif answer.lower() == 'quit':
        active = False
        break

    else:
        age = answer
        print("Please enter a valid age!")