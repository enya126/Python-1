# File: ProblemsFromExam1.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/15/2020
# Date Last Modified: 10/17/2020
# Description of Program: this program use python to figure our problems from exam 1.

# 1. Write the body of the following function that accepts as parameters
# the radius and length of a cylinder and computes and prints the area
# and volume of the cylinder using the following formulas:
#
# area = radius * radius * pi
#
# volume = area * length
#
# Print two decimal places after the decimal point. Remember that pi is
# defined in the math module.  PRINT, do not return your answer.
#
# For example, a call to computeAreaVolumeForCylinder( 5.5, 12 ) would print:
# The area is 95.03
# The volume is 1140.40

def computeAreaVolumeForCylinder(r, l):
#import pi
    from math import pi
#write the formula for area and volume
    area = r * r * pi
    volume = area * l
#print the result
    print("The area is", format(area, ".2f"))
    print("The volume is", format(volume, ".2f"))


# ----------------------------------------------------------------------

# 2. Fill in the following function to take a lower case letter and return
# that letter in upper case. If the input is not a lower case letter,
# simply return the input character. You may assume that the input is a
# single character. The ASCII codes for upper case 'A' to 'Z' are 65 to
# 90, and the ASCII codes for lower case 'a' to 'z' are 97 to 122. You
# may not use any string methods except ord() and chr(). Do NOT use
# .upper(), .lower(), .islower(), etc.
#
# For example, if the input is 'q' you should return 'Q'.  Any of 'a',
# '9', '%' should be returned unchanged.
#
# Return your answer, do NOT print it.

def myUpper(ch):
#convert lower case letter to upper case letter
    if 97 <= ord(ch) <= 122:
        upperValue = ord(ch) - 32
        print(chr(upperValue))
#let other input remain the same
    else:
        print(ch)


# ----------------------------------------------------------------------

# 3. Complete the function below that sums the following series:
#
#      (1 * 2) + (2 * 3) + (3 * 4) + ... + (n-1 * n)
#
# Your function should use a for loop to compute the answer. Return,
# don't print, the answer.  You can assume that n is a positive integer
# greater than 1.  For example if n is 4, this is the series (1 * 2) +
# (2 * 3) + (3 * 4) and your function should return 20.

def sumSeries(n):
#define variables
    firstInteger = 0
    secondInteger = firstInteger + 1
    sumNumber = 0
#calculate the formula
    for secondInteger in range(1, n + 1):
        multiplyNumber = firstInteger * secondInteger
        firstInteger += 1
        sumNumber = sumNumber + multiplyNumber
    return sumNumber

# ----------------------------------------------------------------------

# 4. Complete the following program that takes as parameter a
# nonnegative integer n and prints n even integers starting with 2.  You
# can assume the input is a nonnegative integer, but don't assume it's
# nonzero. There should be 8 even integers per line, and the numbers
# should be separated by one space.  Print a newline at the end.  For
# example: printEvens( 13 ) will print the following pattern:
# 2 4 6 8 10 12 14 16
# 18 20 22 24 26
# and printEvens( 0 ) will just print a newline.

def printEvens(n):
    line = 0
    for i in range(0, n * 2 + 1):
#start a new line after 8 numbers
        if line > 8:
            print()
            line = 0
        if i == 0:
            print()
            line += 1
#find even numbers
        elif i % 2 == 0 and i > 0:
            print(i, end=" ")
            line += 1

# ----------------------------------------------------------------------


# 5. Fill in the body of the following function that takes in three
# integer parameters and displays them in non-decreasing order. You can
# assume that the numbers entered are integers. Do NOT use lists, min(),
# max(), or the sort utility.  The point is to use if tests.
#
# sortThreeIntegers( 39, 2, 5 ) should display:
# The numbers in order are: 2 5 39
#
# sortThreeIntegers( 14, -12, -1000 ) should display:
# The numbers in order are: -1000 -12 14

def sortThreeIntegers(x, y, z):
#defining variables
    x = int(x)
    y = int(y)
    z = int(z)
#comparing x, y, z.
    if x < y < z:
        print("The numbers in order are:", x, y, z)
    elif x < z < y:
        print('The numbers in order are:', x, z, y)
    elif y < x < z:
        print('The numbers in order are:', y, x, z)
    elif y < z < x:
        print("The numbers in order are:", y, z, x)
    elif z < x < y:
        print("The numbers in order are:", z, x, y)
    else:
        print("The numbers in order are:", z, y, x)

----------------------------------------------------------------------


# 6. Fill in the following function that prints out the total of a
# series of positive floating-point (FP) numbers entered by the user.  The
# user should be prompted with the message "Enter a floating-point
# number >= 0:".  You do not need to check that the input is a
# FP number. If the user correctly enters a positive FP number, handle
# it and prompt the user for the next number with the same message.  If
# the user enters a negative number, your program should print
# "Number must be >= 0.  Try again:" and wait for another number.
# Negative numbers should not be added to the total.  If the user enters
# a zero, that is an indication that the user is finished entering
# numbers.  You program should print out "The sum of the numbers is:"
# followed by the total.  You do not need to round the total.
# Below are two runs of the program:
#
# Enter a floating-point number >= 0: 3.5
# Enter a floating-point number >= 0: 2
# Enter a floating-point number >= 0: -17.9
# Number must be >= 0. Try again: 23
# Enter a floating-point number >= 0: 5
# Enter a floating-point number >= 0: 0
# The sum of the numbers is:  33.5
#
# Enter a floating-point number >= 0: 0
# The sum of the numbers is:  0

def sumPositiveFPNumbers():
    sumNumber = 0
    while True:
        numberInput = float(input("Enter a floating-point number >= 0: "))
#re-enter the input if it is negative
        if numberInput < 0:
            numberInput = float(input("Number must be >= 0. Try again: "))
            sumNumber = sumNumber + numberInput
#stop the function if the input is 0
        elif numberInput == 0:
            print("The sum of the numbers is: ", sumNumber)
            break
#calculate the sum
        else:
            sumNumber = sumNumber + numberInput


# ----------------------------------------------------------------------

# 7. Complete the following function that accepts from the user a
# three-digit integer (i.e, in the range 100 to 999), and prints the
# reverse of that integer.  You can assume that the input is an integer, but
# should not assume it's in the right range.  If it's not in the right
# range, print "Illegal input:" and the number.  Here are three sample runs:
#
# Enter a three digit decimal integer: 123
# The number in reverse is: 321
#
# Enter a three digit decimal integer: 1234
# Illegal input: 1234
#
# Enter a three digit decimal integer: 333
# The number in reverse is: 333

def printReverse():
    inputNumber = int(input("Enter a three digit decimal integer: "))
#do not accept illegal input
    if inputNumber < 100 or inputNumber > 999:
        print("Illegal input:", inputNumber)
    else:
#assign different numbers and reverse them
        firstNumber = inputNumber // 100
        secondNumber = (inputNumber % 100) // 10
        thirdNumber = (inputNumber % 100) % 10
        print("The number in reverse is: ", thirdNumber, secondNumber, firstNumber, sep = "")