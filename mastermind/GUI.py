"""Define GUI."""

import tkinter as tk
from game_class import Game
from help_functions import printRules, about
from stat_functions import Stat

colors=["red", "yellow", "blue", "white", "orange", "green", "pink", "purple"]

window = tk.Tk()
window.title("Mastermind")
window.resizable(False, False)

############################################################################
# Frame
############################################################################
frame = tk.Frame(window)
frame.pack(side=tk.TOP)
frame2 = tk.Frame(window)
frame2.pack(side=tk.TOP)
can = tk.Canvas(window, bg='black', height=800, width=500)
can.pack(side=tk.BOTTOM)

############################################################################
# Labels
############################################################################
lab_Message=tk.Label(frame, text="Click on Game to start a new game", fg="black", font='Helvetica 14')
lab_Message.pack(side=tk.TOP)


game = Game(can, lab_Message, window)

############################################################################
# Menus
############################################################################
top = tk.Menu(window)
window.config(menu=top)
game_menu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=game_menu)
stat_menu = tk.Menu(top, tearoff=False)
top.add_command(label='Statistics', command=game.stat.show_stat)
help_menu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Help', menu=help_menu)
game_submenu=tk.Menu(game_menu, tearoff=False)
game_menu.add_cascade(label='New game', menu=game_submenu)
game_submenu.add_command(label='Junior', command=game.game_junior)
game_submenu.add_command(label='Senior', command=game.game_senior)
game_menu.add_command(label='Exit', command=game.exit_game)
help_menu.add_command(label='How to play?', command=printRules)
help_menu.add_command(label='About', command=about)
############################################################################
# Buttons
############################################################################

but_Colors=[]
for color in colors:
    but_Colors.append(tk.Button(frame2, bg=color, command=lambda x=color: game.fill_disc(x)))

for but in but_Colors:
    but.pack(side=tk.LEFT)

window.mainloop()