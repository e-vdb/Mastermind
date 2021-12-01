import tkinter as tk

class Stat:
    def __init__(self):
        self.read_stat()

    def read_stat(self):
        with open('stat.txt') as f:
            stat = f.readlines()
        self.playNb = int(stat[0].split()[-1])
        self.wonNb = int(stat[1].split()[-1])
        self.lostNb = int(stat[2].split()[-1])

    def show_stat(self):
        stat_window = tk.Toplevel()
        stat_window.title("Statistics")
        stat_window.resizable(False, False)
        with open('stat.txt') as f:
            stat = f.read()
        lab_stat = tk.Label(stat_window, text=stat, fg="black", font='Helvetica 12')
        lab_stat.pack(side=tk.TOP)

    def write_stat(self):
        pass

    def reset_stat(self):
        pass