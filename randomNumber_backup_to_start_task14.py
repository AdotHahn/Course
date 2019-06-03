#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: teammember 1, teammember 2, teammember 3
# expert of exercise block 1: teammember 1

import random
import time
import sys
from matplotlib import pyplot as plt

def get_random_number_with_randint(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("Our randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


def get_color_by_dice_roll(spots):
    colors = ["blue", "green", 'red', 'yellow', 'purple', 'orange']
    return colors[spots-1]


def get_color_by_dice_naive(spots):
    if spots == 1:
        color = 'blue'
    elif spots == 2:
        color = 'green'
    elif spots == 3:
        color = 'red'
    elif spots == 4:
        color = 'yellow'
    elif spots == 5:
        color = 'purple'
    else: # spots == 6:
        color = 'orange'
    return color


if __name__ == "__main__":
    outputfilename = "randomNumber"
    rolls_new = []
    for i in range(6):
        roll = get_random_number_with_randint(1, 6)
        rolls_new.append(roll)
    print(rolls_new)
    sys.stdout.flush()
    color = get_color_by_dice_roll(roll)
    write_log_file(outputfilename, color)
    plt.bar(range(6), rolls_new)
    plt.show()
    input("enter to close")
