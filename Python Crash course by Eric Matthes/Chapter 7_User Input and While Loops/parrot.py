"""
The input() function pauses your program and waits for the
user to enter some text. Once Python receives the user’s
input, it assigns that input to a variable to make it
convenient for you to work with

The input() function takes one argument: the prompt that
we want to display to the user, so they know what kind of
information to enter
"""

message = input("Tell me something, and I will repeat it back to you:")
print(message)


prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = " "

while message != "quit":
    message = input(prompt).strip().lower()
    
    if message != "quit":
        print(message)


