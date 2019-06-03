#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: Armin, Claudia, Baltasar, Noone
# expert of excercise block1: Claudia

import random
import time
import sys

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("Our randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


def get_colour_by_dice_roll(spots):
    colours = [
        "GREEN", "BLUE", "PURPLE", "RED", "YELLOW", "BROWN"
    ]
    return colours[spots-1]


if __name__ == "__main__":
    outputfilename = "ChangedrandomNumber"
    roll = get_colour_by_dice_roll(1, 6)
    write_log_file(outputfilename, roll)
    colour = get_colour_by_dice(roll)
    write_log_file(outputfilename, colour)
