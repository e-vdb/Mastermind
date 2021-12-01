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