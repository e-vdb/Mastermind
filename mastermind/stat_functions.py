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
        self.stat_window = tk.Toplevel()
        self.stat_window.title("Statistics")
        self.stat_window.resizable(False, False)
        with open('stat.txt') as f:
            stat = f.read()
        lab_stat = tk.Label(self.stat_window, text=stat, fg="black", font='Helvetica 12')
        lab_stat.pack(side=tk.TOP)
        but_reset = tk.Button(self.stat_window, text='Reset', fg='white', font='Arial 10',
                              bg='red', command=self.reset_stat)
        but_reset.pack()
        self.stat_window.mainloop()

    def write_stat(self):
        with open('stat.txt', 'w') as f:
            f.write('Number of games played\t' + str(self.playNb) + '\n')
            f.write('Number of games won\t' + str(self.wonNb) + '\n')
            f.write('Number of games lost\t' + str(self.lostNb) + '\n')

    def reset_stat(self):
        self.playNb = 0
        self.wonNb = 0
        self.lostNb = 0
        self.write_stat()
        self.stat_window.destroy()
        self.show_stat()