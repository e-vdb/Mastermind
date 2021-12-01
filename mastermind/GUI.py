"""Define GUI."""

import tkinter as tk

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
can = tk.Canvas(window, bg='black', height=500, width=500)
can.pack(side=tk.BOTTOM)

############################################################################
# Labels
############################################################################
lab_Message=tk.Label(frame, text="Click on Game to start a new game", fg="black")
lab_Message.pack(side=tk.TOP)
############################################################################
# Buttons
############################################################################

but_Colors=[]
for color in colors:
    but_Colors.append(tk.Button(frame2, bg=color))

for but in but_Colors:
    but.pack(side=tk.LEFT)

window.mainloop()