"""This is a try it yourself exercise 9-14

The module random contains functions that generate random num-
bers in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides , which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.

"""

from random import randint

class Die():
    """Represents a die, which can be rolled"""

    def __init__(self, sides=6):
        """Initialize the die, default sides is 6"""
        self.sides = sides

    def roll_die(self):
        """Roll the die and returns the value"""
        roll_value = randint(1, self.sides)
        return roll_value


# six_side = Die(6)
# To run this code for a 10 sided die just change the instance

my_die = Die(10)
for i in range(10):
    print("The " + str(i) + " roll was: " + str(my_die.roll_die()))

# In the book answer he creates a list

results = []
for roll_num in range(10):
    result = my_die.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

