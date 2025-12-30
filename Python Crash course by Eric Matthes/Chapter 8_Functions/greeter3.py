def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


#This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit.)")

    first_name = input("\nFirst name: ")
    if first_name.lower().strip() == 'q':
        break

    last_name = input("\nLast name: ")
    if last_name.lower().strip() == 'q':
        break
    
    print(f"\nHello! {get_formatted_name(first_name, last_name).title()}.")