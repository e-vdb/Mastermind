"""Define class Mastermind."""

import numpy as np


colors=["red", "yellow", "blue", "white", "orange", "green", "pink", "purple"]

class Mastermind():
    """
    A class to represent Mastermind game.

    """
    def __init__(self):
        self.setup_combination()

    def setup_combination(self):
        """
        Returns the Mastermind code.

        Returns a 1-D array of string containing the names of four colors
        randomly chosen from the "colors" list.

        """
        self.code = np.random.choice(colors, size=4)

    def occurenceColors(self, comb):
        """
        Returns a dictionary from a list of string
        counting the occurence of colors in the list
        (key=color and value = occurence)

        """
        dicOccurence = {}
        for color in comb:
            if color in dicOccurence:
                dicOccurence[color] += 1
            else:
                dicOccurence[color] = 1
        return dicOccurence
