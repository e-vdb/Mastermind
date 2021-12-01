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
lab_Message=tk.Label(frame, text="Click on Game to start a new game", fg="black")
lab_Message.pack(side=tk.TOP)


game = Game(can, lab_Message)
stat = Stat()
############################################################################
# Menus
############################################################################
top = tk.Menu(window)
window.config(menu=top)
game_menu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=game_menu)
stat_menu = tk.Menu(top, tearoff=False)
top.add_command(label='Statistics', command=stat.show_stat)
help_menu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Help', menu=help_menu)
game_menu.add_command(label='Exit', command=window.destroy)
help_menu.add_command(label='How to play?', command=printRules)
help_menu.add_command(label='About', command=about)
############################################################################
# Buttons
############################################################################

but_Colors=[]
for color in colors:
    but_Colors.append(tk.Button(frame2, bg=color))

for but in but_Colors:
    but.pack(side=tk.LEFT)

window.mainloop()