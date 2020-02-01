# Advent of Code Day #1
import numpy as np
import math
from tkinter import messagebox 

# Function to calculate fuel for each line in 'input'
def fun(x):
    return math.floor(x / 3) - 2

# loop to append each line in 'input' to an array
with open('input') as f: 
    array = []
    for line in f: 
        num = line.split()
        i = int(line)
        array.append(i)

# loop to apply function to each instance in array
array2 = [fun(i) for i in array]

# print answer to the terminal
print("Answer: " + str(sum(array2)))

# create a message box with the answer in it
messagebox.showinfo('Answer', sum(array2))
