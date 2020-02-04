# Advent of Code Day 2 pt 1

import csv 
import numpy as np

# load input file as a list of lists
with open("input.csv", newline="") as f:
    reader = csv.reader(f)
    program = list(reader)

# flatten the list and make strings into integers
program = program[0]
program = [int(i) for i in program]

# replace values at positions 1 and 2 with 12 and 2 respectively
program[1] = 12
program[2] = 2

# define the starting position
idx = 0

# while loop to stop when index value is 99
while program[idx] != 99:
    # where the current opcode begins
    this_opcode = program[idx]
    # define the first position in the current opcode
    pos1 = (idx + 1) % len(program)
    # define the second position in the current opcode
    pos2 = (idx + 2) % len(program)
    # define the third position (answer location) in the current opcode
    ans_loc = (idx + 3) % len(program)
    # set program to add position 1 and 2 together if index value is 1
    if this_opcode == 1:
        program[ans_loc] = program[program[pos1]] + program[program[pos2]]
    # set program to multiply position 1 and 2 together if index value is 2
    elif this_opcode == 2:
        program[ans_loc] = pos1 * pos2
    # set index to the next opcode
    idx = (idx + 4) % len(program)

print(program)
