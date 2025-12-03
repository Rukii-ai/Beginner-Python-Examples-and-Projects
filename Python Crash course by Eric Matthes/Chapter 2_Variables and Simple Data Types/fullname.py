first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}!"
message = f"Hello, {full_name.title()}"
print (message)

"""To insert a variable’s value into a string, place the letter f
 immediately before the opening quotation mark ❶. Put
 braces around the name or names of any variable you want
 to use inside the string. Python will replace each variable
 with its value when the string is displayed.
 These strings are called f-strings. The f is for format,
 because Python formats the string by replacing the name of
 any variable in braces with its value.
 The .title method goes inside the curly bracket with the variable name.
 """