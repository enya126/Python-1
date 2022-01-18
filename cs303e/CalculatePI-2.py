# File: CalculatePI.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/22/2020
# Date Last Modified: 10/23/2020
# Description of the Program: This program used python to calculate pi using random numbers.

#import functions
import math
import random

#define first function to find value of PI
def computePI (n):
    count = 0
    for i in range (0, n):
        xPos = random.uniform(-1.0, 1.0)
        yPos = random.uniform(-1.0, 1.0)
        if math.hypot(xPos, yPos) < 1:
            count += 1
    valuePI = count*4/n
    return valuePI
#define second function to print out result
def main ():
    print("Computation of PI using Random Numbers ")
    print()
    for i in range (2, 8):
        numberInput = 10**i
        valuePI = computePI(numberInput)
        difference = valuePI - math.pi
        print("num =", format(numberInput, '<11' ), "Calculated PI =", format(valuePI, '<10.6f'), "Difference =", format(difference, '<+8.6f'))
    print()
    print("Difference = Calculated PI - math.pi")
#run main function
main()