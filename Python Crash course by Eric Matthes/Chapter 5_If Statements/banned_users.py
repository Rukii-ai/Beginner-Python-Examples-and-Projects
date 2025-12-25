banned_users = ['andrew', 'carolina', 'david']

users = ['david', 'maria', 'john']

for user in users:
    if user not in banned_users:
        print(f"{user.title()}, you can post a response if you wish.")
    if user in banned_users:
        print(f"{user.title()}, you are banned from posting a response.")



"""
As you learn more about programming, you’ll hear the term
Boolean expression at some point. A Boolean expression is
just another name for a conditional test. A Boolean value is
either True or False, just like the value of a conditional
expression after it has been evaluated.

Boolean values are often used to keep track of certain
conditions, such as whether a game is running or whether a
user can edit certain content on a website. Boolean values provide 
an efficient way to track the state of a program or a particular 
condition that is important in your program
""" 