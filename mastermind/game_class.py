"""Define class for game."""

from stat_functions import Stat
import tkinter as tk

ROW_COUNT = 12
COLUMN_COUNT = 4
WIDTH = 50
LENGTH = 40

class Game:
    """
    A class to represent a game.
    """
    def __init__(self, can, lab_Message, window):
        self.stat = Stat()
        self.window = window
        self.can = can
        self.lab = lab_Message
        self.draw_board()
        self.draw_check_board()
        self.ongoing_game = False

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
        self.can.delete(tk.ALL)
        self.draw_board()
        self.draw_check_board()

    def new_game(self):
        if self.ongoing_game:
            self.stat.lostNb += 1
        else:
            self.ongoing_game = True
        self.stat.write_stat()
        self.stat.playNb += 1
        self.reinit()

    def exit_game(self):
        if self.ongoing_game:
            self.stat.lostNb += 1
            self.stat.write_stat()
        self.window.destroy()

    def game_senior(self):
        """
        Launches game with senior difficulty level.
        """
        self.level = 'senior'
        self.new_game()

    def game_junior(self):
        """
        Launches game with junior difficulty level.
        """
        self.level = 'junior'
        self.new_game()
