sandwich_orders = ['tuna sandwich', 'avocado sandwich', 'turkey sandwich', 
                   'pastrami sandwich', 'grilled cheese sandwich']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Order up! {current_sandwich.title()} ready to go.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")