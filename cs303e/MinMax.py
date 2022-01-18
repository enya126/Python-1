# File: MinMax.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/01/2020
# Date Last Modified: 10/02/2020
# Description of the Program: This program used python to find max and min of a series of integers.

#let the user enter integers
number = input("Enter an integer or 'stop' to end: ")
#stop if no integer was entered.
if number == "stop":
    print("You didn't enter any numbers")
else:
#convert number into integers
    number = int(number)
    min = number
    max = number
    while True:
        number = input("Enter an integer or 'stop' to end: ")
        if number == "stop":
            break
#assign max and min again for newly entered numbers
        number = int(number)
        if number < min:
            min = number
        if number > max:
            max = number
#print out statements
print("The maximum is", max)
print("The minimum is", min)

