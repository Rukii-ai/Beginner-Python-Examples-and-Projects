"""
Handling errors correctly is especially important when the
program has more work to do after the error occurs.

This happens often in programs that prompt users for input. 

If the program responds to invalid input appropriately, it can
prompt for more valid input instead of crashing.
"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break

    second_number = input("\nSecond number: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

"""
This program prompts the user to input a first_number 
and, if the user does not enter q to quit, a second_number.
We then divide these two numbers to get an answer. This
program does nothing to handle errors, so asking it to divide
by zero causes it to crash

It’s bad that the program crashed, but it’s also not a good
idea to let users see tracebacks. 

Nontechnical users will be
confused by them, and in a malicious setting, attackers will
learn more than you want them to. 

For example, they’ll
know the name of your program file, and they’ll see a part
of your code that isn’t working properly. 

A skilled attacker
can sometimes use this information to determine which kind
of attacks to use against your code.

We can make this program more error resistant by wrapping
the line that might produce errors in a try-except block. 

The error occurs on the line that performs the division, so that’s
where we’ll put the try-except block. 

This example also
includes an else block. Any code that depends on the try
block executing successfully goes in the else block:

The only code that should go in a try block is code that
might cause an exception to be raised. 

Sometimes you’ll
have additional code that should run only if the try block
was successful; this code goes in the else block. 

The except
block tells Python what to do in case a certain exception
arises when it tries to run the code in the try block.

By anticipating likely sources of errors, you can write
robust programs that continue to run even when they
encounter invalid data and missing resources. 

Your code will
be resistant to innocent user mistakes and malicious
attacks
"""