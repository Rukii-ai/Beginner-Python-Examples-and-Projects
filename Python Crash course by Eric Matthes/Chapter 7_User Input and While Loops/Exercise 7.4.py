prompt = "\nEnter the pizza toppings you'd like to have on your pizza!"
prompt += "\nEnter 'quit' when you'd like to exit the program "

toppings = ""

while toppings != "quit":
    toppings = input(prompt).strip().lower()
    if toppings != "quit":
        print (f"Adding {toppings.title()}")