sandwich_orders = ['tuna sandwich', 'avocado sandwich', 'pastrami sandwich', 
                   'turkey sandwich', 'pastrami sandwich', 
                   'grilled cheese sandwich', 'pastrami sandwich']

print(sandwich_orders)
print ("\nSorry, we have run out of pastrami today.")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

print(sandwich_orders)
