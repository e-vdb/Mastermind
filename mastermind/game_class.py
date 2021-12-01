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
        self.draw_board()

    def draw_board(self):
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                self.can.create_oval(10 + WIDTH * j,
                                     10 + WIDTH * i,
                                     10 + LENGTH + WIDTH * j,
                                     10 + LENGTH + WIDTH * i,
                                     outline='white')