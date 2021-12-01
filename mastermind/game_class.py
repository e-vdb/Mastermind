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
        self.draw_check_board()

    def draw_board(self):
        x0 = 70
        y0= 50
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                self.can.create_oval(x0 + WIDTH * j,
                                     y0 + WIDTH * i,
                                     x0 + LENGTH + WIDTH * j,
                                     y0 + LENGTH + WIDTH * i,
                                     outline='white')

    def draw_check_board(self):
        x0 = 300
        y0 = 60
        width = 50
        length = 15
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                self.can.create_rectangle(x0 + width * j,
                                          y0 + width * i,
                                          x0 + length + width * j,
                                          y0 + length + width * i,
                                          outline='white')

    def reinit(self):
        pass
