from random import choice

codes = [3, 79, 0, 52, 23, 11, 117, 35, 44, 68, "p", "u", "j", "t", "w"]

print("The winning codes are:")

i = 1
while i < 5:
    print(choice(codes))
    i += 1

print("Any ticket with these matching codes in this order" 
      "can come claim their prize at the lottery center!")