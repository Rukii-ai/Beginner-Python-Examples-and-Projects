from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))



"""
Python has no inherent limit to how much data you can
work with; you can work with as much data as your
system’s memory can handle.
"""