"""
The for loop takes a collection of items and executes a block
of code once for each item in the collection. In contrast, the
while loop runs as long as, or while, a certain condition is
true
"""


i = 1

while i <= 5:
    print(i)
    i += 1 #(The += operator is shorthand for i = i + 1.)


"""
The programs you use every day most likely contain while
loops. For example, a game needs a while loop to keep
running as long as you want to keep playing, and so it can
stop running as soon as you ask it to quit. Programs
wouldn’t be fun to use if they stopped running before we
told them to or kept running even after we wanted to quit,
so while loops are quite useful.
"""

"""
Rather than breaking out of a loop entirely without
executing the rest of its code, you can use the continue
statement to return to the beginning of the loop, based on
the result of a conditional test.
"""

i = 0

while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    else:
        print(i)

"""
Every while loop needs a way to stop running so it won’t
continue to run forever
"""

x = 1

while x <= 5:
    print(x)
    x += 1


"""
Every programmer accidentally writes an infinite while
loop from time to time, especially when a program’s loops
have subtle exit conditions. If your program gets stuck in an
infinite loop, press CTRL-C or just close the terminal window
displaying your program’s output.

To avoid writing infinite loops, test every while loop and
make sure the loop stops when you expect it to. If you want
your program to end when the user enters a certain input
value, run the program and enter that value. If the program
doesn’t end, scrutinize the way your program handles the
value that should cause the loop to exit.

Make sure at least
one part of the program can make the loop’s condition False
or cause it to reach a break statement

VS Code, like many editors, displays output in an
embedded terminal window. To cancel an infinite loop,
make sure you click in the output area of the editor
before pressing CTRL-C.
"""