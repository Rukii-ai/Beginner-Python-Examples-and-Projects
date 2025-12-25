age = 31

if age < 2:
    stage = "a baby"

elif 2 <= age < 4:
    stage = "a toddler"

elif 4 <= age < 13:
    stage = "a kid"

elif 13 <= age < 20:
    stage = "a teenager"

elif 20 <= age < 65:
    stage = "an adult"

else:
    stage = "an elder"

print(f"The person is {stage}.")