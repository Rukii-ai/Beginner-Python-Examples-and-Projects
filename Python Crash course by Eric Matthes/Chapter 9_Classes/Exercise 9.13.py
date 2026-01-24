from random import randint as rnt

class Die:
    """A class to model a 6-faced die"""

    def __init__(self, sides=6):
        """Initialize instances of the die"""
        self.sides = sides

    def roll_die(self):
        """Simulate the rolling of a die"""
        print(f"You rolled a {rnt(1, self.sides)}!")

# Make a 6-sided die and roll it 10 times
six_sided_die = Die()
x = 1
while x < 11:
    six_sided_die.roll_die()
    x += 1

# Make a 10-sided die and roll it 10 times
ten_sided_die = Die(sides=10)
y = 1
while y < 11:
    ten_sided_die.roll_die()
    y += 1

# Make a 20-sided die and roll it 10 times
twenty_sided_die = Die(sides=20)
z = 1
while z < 11:
    twenty_sided_die.roll_die()
    z += 1