
from random import randint

class Die:
    """Class representing the die"""

    def __init__(self, num_sides=6):
        """Initializing the attributes of the die, assuming a classic 6-sided one"""
        self.num_sides = num_sides

    def roll(self):
        """Roll the die"""
        return randint(1, self.num_sides)