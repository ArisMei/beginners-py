import os
new_directory = "C:\\Users\\User\\OneDrive - Universidad Politécnica de Madrid\\Aalto\\beginners-Py\\week_3"
os.chdir(new_directory)
os.getcwdb()


import numpy as np
import math
import time

def calc_average(grades):
    sum_grade = 0
    for grade in grades:
        sum_grade += grade
    avg = sum_grade / len(grades)
    return avg

def calc_std(grades):
    avg = calc_average(grades)
    squareSum = 0
    for grade in grades:
        gradeDiff = grade - avg
        squareSum += gradeDiff*gradeDiff
    temp = squareSum / len(grades)
    std = math.sqrt(temp)
    return(std)

# We now want to compare the time spent to calculate
# the average and the standard deviation 
# with our own functions and with the functions p
# rovided by numpy. First we fill a list with random 
# integers. As our example is about grades, we choose the 
# grades between 1 and 5.

import random
listLength = 50000000
randomlist = []
for i in range(listLength):
    randomlist.append(random.randint(1, 5))


