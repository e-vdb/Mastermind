"""Define class for game."""

from stat_functions import Stat
import tkinter as tk
from mastermind_class import Mastermind, Player

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
        self.mastermind = Mastermind()
        self.player = Player()
        self.window = window
        self.can = can
        self.lab = lab_Message
        self.cell = [[0 for col in range(COLUMN_COUNT)] for row in range(ROW_COUNT + 1)]
        self.check_cell = [[0 for col in range(COLUMN_COUNT)] for row in range(ROW_COUNT)]
        self.draw_board()
        self.draw_check_board()
        self.ongoing_game = False

    def draw_board(self):
        x0 = 70
        y0= 50
        for i in range(ROW_COUNT +1):
            for j in range(COLUMN_COUNT):
                self.cell[i][j] = self.can.create_oval(x0 + WIDTH * j,
                                                         y0 + WIDTH * i,
                                                         x0 + LENGTH + WIDTH * j,
                                                         y0 + LENGTH + WIDTH * i,
                                                         outline='white')

    def draw_check_board(self):
        x0 = 300
        y0 = 60
        width = 50
        length = 15
        self.can.create_rectangle(70, 650, 260, 650 + LENGTH, outline="white")
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                self.check_cell[i][j] = self.can.create_rectangle(x0 + width * j,
                                          y0 + width * i,
                                          x0 + length + width * j,
                                          y0 + length + width * i,
                                          outline='white')

    def fill_disc(self, color) -> None:
        """
        Displays the color chosen by the player.

        Returns
        ------------
        None
        """
        col = len(self.player.proposal)
        if self.ongoing_game and col < COLUMN_COUNT:
            self.can.itemconfig(self.cell[self.player.attempt][col], fill=color)
            self.player.proposal.append(color)

    def show_solution(self) -> None:
        """
        Displays the mastermind code.

        Returns
        ------------
        None
        """
        for col, color in enumerate(self.mastermind.code):
            self.can.itemconfig(self.cell[ROW_COUNT][col], fill=color)

    def enter(self):
        if self.ongoing_game:
            self.player.validate_proposal()

    def erase(self):
        if self.ongoing_game:
            for col in range(COLUMN_COUNT):
                self.can.itemconfig(self.cell[self.player.attempt][col], fill='black')
                self.player.reset_proposal()

    def reinit(self) -> None:
        """
        Erases all elements in canvas and redraws board game.

        Returns
        ------------
        None
        """
        self.can.delete(tk.ALL)
        self.draw_board()
        self.draw_check_board()

    def new_game(self) -> None:
        """
        Launches a new game.

        Returns
        ------------
        None
        """
        if self.ongoing_game:
            self.stat.lostNb += 1
        else:
            self.ongoing_game = True
        self.stat.write_stat()
        self.stat.playNb += 1
        self.reinit()
        self.mastermind.setup_combination()

    def exit_game(self) -> None:
        """
        Updates game statistics and closes window.

        Returns
        ------------
        None
        """
        if self.ongoing_game:
            self.stat.lostNb += 1
            self.stat.write_stat()
        self.window.destroy()

    def game_senior(self) -> None:
        """
        Launches game with senior difficulty level.

        Returns
        ------------
        None
        """
        self.level = 'senior'
        self.new_game()

    def game_junior(self) -> None:
        """
        Launches game with junior difficulty level.

        Returns
        ------------
        None
        """
        self.level = 'junior'
        self.new_game()
