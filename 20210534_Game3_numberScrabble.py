# Game 3 (Number scrabble created by Ahmed_mohamed_Ahmed_Amer )
# players take turn an choose number by number first player collect 3 numbers their sum equal 15 win the game

from tkinter import *   # import tkinter module to make the graphics for the game
from tkinter import ttk
from tkinter import messagebox       # message box to print which player is the winner
import sys                           # import sys to exit the program when some player win the game


first_selections = []        #what player 1 selected
second_selections = []       #what player 2 selected


root = Tk()               # root or layout to show the buttons on it
root.title(": player 1")
style = ttk.Style()
style.theme_use("classic")

# 9 buttons by tkinter and make them appear in the root
bu1 = ttk.Button(root, text="1")
bu1.grid(row=0, column=0, sticky="snew", ipadx=40, ipady=40)
bu1.config(command=lambda: button_click(1))

bu2 = ttk.Button(root, text="2")
bu2.grid(row=0, column=1, sticky="snew", ipadx=40, ipady=40)
bu2.config(command=lambda: button_click(2))

bu3 = ttk.Button(root, text="3")
bu3.grid(row=0, column=2, sticky="snew", ipadx=40, ipady=40)
bu3.config(command=lambda: button_click(3))

bu4 = ttk.Button(root, text="4")
bu4.grid(row=1, column=0, sticky="snew", ipadx=40, ipady=40)
bu4.config(command=lambda: button_click(4))

bu5 = ttk.Button(root, text="5")
bu5.grid(row=1, column=1, sticky="snew", ipadx=40, ipady=40)
bu5.config(command=lambda: button_click(5))

bu6 = ttk.Button(root, text="6")
bu6.grid(row=1, column=2, sticky="snew", ipadx=40, ipady=40)
bu6.config(command=lambda: button_click(6))

bu7 = ttk.Button(root, text="7")
bu7.grid(row=2, column=0, sticky="snew", ipadx=40, ipady=40)
bu7.config(command=lambda: button_click(7))

bu8 = ttk.Button(root, text="8")
bu8.grid(row=2, column=1, sticky="snew", ipadx=40, ipady=40)
bu8.config(command=lambda: button_click(8))

bu9 = ttk.Button(root, text="9")
bu9.grid(row=2, column=2, sticky="snew", ipadx=40, ipady=40)
bu9.config(command=lambda: button_click(9))

active_player = 1

def button_click(x):                      # A Function to append the selections of the players to their empty lists
    global active_player
    if active_player == 1:
        first_selections.append(x)
        active_player = 2
        root.title(" : player 2")
        button_disable(x)
        if is_first_won(first_selections):
            messagebox.showinfo(title= "congratulation", message="Player 1 is the winner")
            sys.exit()


    elif active_player == 2:
        second_selections.append(x)
        active_player = 1
        root.title(" : player 1")
        button_disable(x)
        is_second_won(second_selections)
        if is_second_won(second_selections):
            messagebox.showinfo(title="congratulation", message="Player 2 is the winner")
            sys.exit()
    else:return False

if not button_click:
    messagebox.showinfo(title="try again!", message="Draw")
    sys.exit()



def button_disable(x):     # A function to prevent user from choose the same number again following the rules of the game
    if x == 1:
        bu1.state(["disabled"])
    elif x == 2:
        bu2.state(["disabled"])
    elif x == 3:
        bu3.state(["disabled"])
    elif x == 4:
        bu4.state(["disabled"])
    elif x == 5:
        bu5.state(["disabled"])
    elif x == 6:
        bu6.state(["disabled"])
    elif x == 7:
        bu7.state(["disabled"])
    elif x == 8:
        bu8.state(["disabled"])
    elif x == 9:
        bu9.state(["disabled"])


def is_first_won(first_selections):         # a function to check if there are 3 numbers make up 15 in the list of the first player
    for i in range(0, len(first_selections)):
        for k in range(i+1, len(first_selections)):
            for l in range(k+1, len(first_selections)):
                if first_selections[i] + first_selections[k] + first_selections[l] == 15:
                    return True


def is_second_won(second_selections):        # a function to check if there are 3 numbers make up 15 in the list of the second player
    for i in range(0, len(second_selections)):
        for k in range(i+1, len(second_selections)):
            for l in range(k+1, len(second_selections)):
                if second_selections[i] + second_selections[k] + second_selections[l] == 15:
                    return True

root.mainloop()           # to make the root appear in the layout