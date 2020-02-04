# Advent of Code Day #2
import numpy as np
import math
from tkinter import messagebox 

# Function to calculate fuel for each line in 'input'
def fun(x):
    return math.floor(x / 3) - 2

# loop to append each line in 'input' to an array
with open('input') as f: 
    module_mass_list = []
    for line in f: 
        num = line.split()
        i = int(line)
        module_mass_list.append(i)

# loop to apply function to each instance in array
# fuel_req_list = [fun(i) for i in array]
fuel_req_list = []
for i in module_mass_list:
    fuel_mass = i
    while fuel_mass > 0:
        fuel_mass = fun(fuel_mass)
        if fuel_mass < 0:
            fuel_mass = 0
        fuel_req_list.append(fuel_mass)
        print(fuel_mass)

# print answer to the terminal
print("Answer: " + str(sum(fuel_req_list)))

# create a message box with the answer in it
messagebox.showinfo('Answer', sum(fuel_req_list))
