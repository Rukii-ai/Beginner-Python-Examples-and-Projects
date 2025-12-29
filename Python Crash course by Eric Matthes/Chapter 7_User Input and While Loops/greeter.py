"""
Each time you use the input() function, you should include a
clear, easy-to-follow prompt that tells the user exactly what
kind of information you’re looking for. Any statement that
tells the user what to enter should work

Add a space at the end of your prompts (after the colon in
the preceding example) to separate the prompt from the
user’s response and to make it clear to your user where to
enter their text
"""

name = input("Please enter your name: ")
print(f"Hello, {name}!")

"""
Sometimes you’ll want to write a prompt that’s longer
than one line. For example, you might want to tell the user
why you’re asking for certain input. You can assign your
prompt to a variable and pass that variable to the input()
function.
"""

prompt = "If you tell me who you are, I can personalize the messages I send you."
prompt += "\nWhat is your first name? "

name = input(prompt)