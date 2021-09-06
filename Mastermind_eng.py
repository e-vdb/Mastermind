#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:35:56 2021

@author: Emeline Van der Beken

Programmation d'un jeu Mastermind en version graphique 

"""


import tkinter as tk
import numpy as np

############################################################################
# Functions
############################################################################
def chooseCombination():
    '''Return a list of string containing the names of four colors
    randomly chosen from the "colors" list
    
    '''
    global colors
    return np.random.choice(colors, size=4)

def occurenceColors(comb):
    '''Returns a dictionary from a list of string 
    counting the occurence of colors in the list
    (key=color and value = occurence)
    '''
    dicOccurence={}
    for color in comb:
        if color in dicOccurence:
            dicOccurence[color]+=1
        else:
            dicOccurence[color]=1
    return dicOccurence

# Compares the combinaison chosen by the player with the actual one and displays the red/white squares
def check():
    global code,proposal,codeOK,attemptsNb,playNb,wonNb,lostNb,ongoing,level
    pionB=0
    pionR=0
    pionN=0
    colorsCode=occurenceColors(code)
    colorsProp=occurenceColors(proposal)
    for colProp,colCode in zip(proposal,code):
        colorsProp[colProp]-=1  
        if colProp==colCode:
            pionR+=1
            colorsCode[colCode]-=1 
            if level=='junior':
                draw_square("red")
        elif colProp in colorsCode and colorsCode[colProp]>0 and colorsProp[colProp]<colorsCode[colProp]:
            pionB+=1
            colorsCode[colProp]-=1 
            if level=='junior':
                draw_square("white")
        else:
            pionN+=1
            if level=='junior':
                draw_square("black")
    if pionR==4:
        codeOK=True
        lab_Message.configure(text="CONGRATULATIONS! Click on Game to start a new game")
        ongoing=False
        wonNb+=1
        writeStat()
        solution()
    else:
        lab_Message.configure(text="Set a combination of 4 colours.")
    if level=='senior':
        for count in range(pionR):
            draw_square("red")
        for count in range(pionB):
            draw_square("white")
        for count in range(pionN):
            draw_square("black")


def draw_disc(coul):
    global x_coord,y_coord,chosenColor
    can.create_oval(x_coord,y_coord,x_coord+25,y_coord+25,fill=coul)
    x_coord+=50
    chosenColor+=1

def draw_square(coul):
    global x_coord,y_coord,square_X,square_Y
    can.create_rectangle(square_X, square_Y, square_X+15, square_Y+15, fill=coul,outline='white')
    square_X+=25

def play(coul):
    global proposal,chosenColor,codeOK,ongoing
    if ongoing:
        if chosenColor<4 and attemptsNb<12 and not codeOK:
            proposal.append(coul)
            draw_disc(coul)
        if chosenColor==4:
            lab_Message.configure(text="Validation in progress")
            window.after(1500,enter)
        

def enter():
    global x_coord,y_coord,chosenColor,attemptsNb,proposal,square_X,square_Y,playNb,wonNb,lostNb,ongoing
    if chosenColor==4:
        square_X=x_coord+50
        square_Y=y_coord
        check()
        x_coord=150
        y_coord+=50
        chosenColor=0
        attemptsNb+=1
        if attemptsNb==12:
            solution()
            lab_Message.configure(text="LOST! Click on Game to start a new game.")
            ongoing=False
            lostNb+=1
            writeStat()
        proposal=[]
        
def solution():
    global x_coord,y_coord,code,colors,chosenColor,attemptsNb
    x_coord=150
    y_coord=680
    chosenColor=0
    attemptsNb=12
    can.create_rectangle(140, 660, 340, 720, fill="white")
    for color in code:
        draw_disc(color)
        
def gameSenior():   
    '''
    Launch game with senior difficulty level

    '''
    global level
    level='senior'
    game()

def gameJunior():
    '''
    Launch game with junior difficulty level

    '''
    global level
    level='junior'
    game()

    
def reset():
    global can
    can.destroy()
    can = tk.Canvas(window,bg='black',height=800,width=500)
    can.pack(side=tk.TOP)

def game():
    global attemptsNb,code,x_coord,y_coord,chosenColor,proposal,codeOK,playNb,wonNb,lostNb,ongoing
    if ongoing:
        lostNb+=1
    else:
        ongoing=True
    writeStat()
    playNb+=1
    proposal=[]
    reset()
    codeOK=False
    attemptsNb=0
    code=chooseCombination()
    chosenColor=0
    x_coord=150
    y_coord=20
    lab_Message.configure(text="Set a combination of 4 colours.")

def exitAll():
    global window,ongoing,lostNb
    if ongoing:
        lostNb+=1
        writeStat()
    window.destroy()
############################################################################
# Help menu
############################################################################     
def printRules():
    ruleWindow=tk.Toplevel()
    ruleWindow.title("How to play")
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lab_Rule=tk.Label(ruleWindow,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lab_Rule.pack(side=tk.TOP)
    ruleWindow.mainloop()


def about():
    aboutWindow=tk.Toplevel()
    aboutWindow.title("About") 
    with open('about.txt') as f:
        about=f.read()
    lbl_about=tk.Label(aboutWindow,text=about,fg="black", anchor="e", justify=tk.LEFT)
    lbl_about.pack(side=tk.TOP)
    aboutWindow.mainloop()    
############################################################################
# Statistics
############################################################################   
def readStat():
    global playNb,wonNb,lostNb
    with open('stat.txt') as f:
        stat=f.readlines()
    playNb=int(stat[0].split()[-1])
    wonNb=int(stat[1].split()[-1])
    lostNb=int(stat[2].split()[-1])


def showStat():
    global lab_Stat
    statWindow=tk.Toplevel()
    statWindow.title("Statistics")
    frameStat=tk.Canvas(statWindow,bg='white',height=500,width=500)
    frameStat.pack()  
    with open('stat.txt') as f:
        stat=f.read()
    lab_Stat=tk.Label(frameStat,text=stat,fg="black")
    lab_Stat.pack(side=tk.TOP)
    but_reset=tk.Button(frameStat,text='Reset',fg='white',bg='red',command=resetStat)
    but_reset.pack()
    statWindow.mainloop()   

def writeStat():
    with open('stat.txt','w') as f:
        f.write('Number of games played\t'+str(playNb)+'\n')
        f.write('Number of games won\t'+str(wonNb)+'\n')
        f.write('Number of games lost\t'+str(lostNb)+'\n')
    
def resetStat():
    global playNb,wonNb,lostNb,lab_Stat,ongoing
    playNb=0
    wonNb=0
    lostNb=0
    writeStat()
    with open('stat.txt') as f:
        stat=f.read()
    lab_Stat.configure(text=stat)
    if ongoing:
        playNb+=1
        

############################################################################
# Global variables
############################################################################
colors=["red", "yellow", "blue", "white", "orange", "green", "pink", "purple"]

############################################################################
# Graphics window
############################################################################
window = tk.Tk()
window.title("Mastermind")

############################################################################
# Menus
############################################################################
top = tk.Menu(window)
window.config(menu=top)
jeu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=jeu)
stat=tk.Menu(top,tearoff=False)
top.add_command(label='Statistics',command=showStat)
helpMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Help', menu=helpMenu)

submenu=tk.Menu(jeu, tearoff=False)
jeu.add_cascade(label='New game', menu=submenu)
submenu.add_command(label='Junior', command=gameJunior)
submenu.add_command(label='Senior', command=gameSenior)
jeu.add_command(label='Exit', command=exitAll)



helpMenu.add_command(label='How to play?',command=printRules)
helpMenu.add_command(label='About',command=about)

############################################################################
# Frame
############################################################################
frame=tk.Frame(window)
frame.pack(side=tk.TOP)
frame2=tk.Frame(window)
frame2.pack(side=tk.TOP)
can = tk.Canvas(window,bg='black',height=500,width=500)
can.pack(side=tk.BOTTOM)

############################################################################
# Labels
############################################################################
lab_Message=tk.Label(frame,text="Click on Game to start a new game",fg="black")
lab_Message.pack(side=tk.TOP)
############################################################################
# Buttons
############################################################################

but_Colors=[]
for color in colors:
    but_Colors.append(tk.Button(frame2,bg=color,command=lambda x=color:play(x)))

for but in but_Colors:
    but.pack(side=tk.LEFT)


############################################################################
# Start-up
############################################################################
readStat()
ongoing=False
window.mainloop()
