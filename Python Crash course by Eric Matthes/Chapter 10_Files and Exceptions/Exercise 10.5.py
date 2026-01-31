from pathlib import Path

path = Path("guest_book.txt")
flag = True
list_of_guests = []
guest_string = ""

while flag == True:
    contents = input("Hello there guest! What is your name? ")
    
    if contents.lower().strip() == "quit":
        flag = False
        break

    list_of_guests.append(contents)
    


for name in list_of_guests:
    guest_string += f"{name}\n"

path.write_text(f"{guest_string.title().strip()}\n")