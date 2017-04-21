import math
import random
from tkinter import *

"""root = Tk()
w = Label(root, text='Dice Roller')
w.pack()
root.mainloop()"""

#General function for rolling dice.
def roll(sides, quantity=1, modifier=0):
    counter = 0
    summation = 0
    while counter < quantity:
        temp = random.randint(1, sides)
        if modifier == 0:
            print(repr(temp))
        else:
            print(repr(temp) + '+' + repr(modifier))
        summation += temp + modifier
        counter += 1
    return summation

#Used for the gui to remove printing.
def roller(sides, quantity=1, modifier=0):
    counter = 0
    summation = 0
    while counter < quantity:
        temp = random.randint(1, sides)
        summation += temp + modifier
        counter += 1
    return summation

#For ease of adding modifiers. Takes an unspecified amount of arguments.
def add(*args):
    summation = 0
    for arg in args:
        summation += arg
    print('Total: ' + repr(summation))
    return summation

#For character generation. Rolls 4d6, and takes the highest of the 3 for the new stat.
def make_stat():
    lst = []
    lst.append(random.randint(1,6))
    lst.append(random.randint(1,6))
    lst.append(random.randint(1,6))
    temp = random.randint(1,6)
    display = lst + [temp]
    print(display)
    for stat in lst:
        if temp > stat:
            lst[lst.index(stat)] = temp
            break
    return (sum(lst))

#For character creation. Creates 6 stats using make_stat, and returns them in a list.
def make_statlist():
    lst = []
    for i in range(6):
        lst.append(make_stat())
    return lst

#Functions for commonly used dice. Useful for simple fast calls with no modifiers.
def d20():
    return random.randint(1, 20)
def d2():
    return random.randint(1, 2)
def d3():
    return random.randint(1, 3)
def d4():
    return random.randint(1, 4)
def d6():
    return random.randint(1, 6)
def d8():
    return random.randint(1, 8)
def d10():
    return random.randint(1, 10)
def d100():
    return random.randint(1, 100)
