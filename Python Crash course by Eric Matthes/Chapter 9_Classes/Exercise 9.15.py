from random import choice

my_ticket = [3, 23, "p", 68]
codes = [3, 79, 0, 52, 23, 11, 117, 35, 44, 68, "p", "u", "j", "t", "w"]
ticket = []
ticket_count = 1

while True:
    i = 1
    
    while i < 5:
        ticket.append(choice(codes))
        i += 1

    if ticket == my_ticket:
        print("Congratulations! Your ticket is a winner!")
        break
    else:
        ticket = []
        ticket_count += 1
    
    

print(f"It took {ticket_count} tries to get your winning ticket.")