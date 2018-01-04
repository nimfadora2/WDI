# Rain
# 23.10.2017 r.
# lab3

from random import randint, seed
from time import sleep
import os

# Input
height = int(input('Height: '))
width = int(input('Width: '))

# Table init
tab = []
for x in range(0,height):
    tab.append(width*[0])
clear = lambda: os.system('cls')

# Main program
for x in range(0,15):
    seed()
    los = randint(0,width-1)
    small_tab = width*[0]
    small_tab[los]=1
    tab[1:height] =tab[0:height-1]
    tab[0] = small_tab
    for x in range(0,height):
        for y in range(0,width):
            if tab[x][y]==1: print('X', end='')
            else: print('O', end='')
        print('')
    sleep(1)
    clear()

#tab = small_tab + tab[0:height-1]

