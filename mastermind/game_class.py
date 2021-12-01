"""Define class for game."""

ROW_COUNT = 12
COLUMN_COUNT = 4
WIDTH = 50
LENGTH = 40

class Game:
    """
    A class to represent a game.
    """
    def __init__(self, can, lab_Message):
        self.can = can
        self.lab = lab_Message
