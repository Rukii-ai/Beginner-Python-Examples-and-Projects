number_of_diners = int(input("How many people are in your dinner group? "))

if number_of_diners > 8:
    print(f"\nUnfortunately we don't have a table of {number_of_diners} available"
          " yet. \nPlease wait here and we'll notify you as soon as one is ready!")
    
else:
    print(f"\nYes we do have a table of {number_of_diners} ready and available!"
          "\nThis way, please folllow me.")