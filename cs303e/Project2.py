# File: Project2.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/31/2020
# Date Last Modified: 11/3/2020
# Description of the Program: This program used python to create a library of functions to deal
#with primes

print("Welcome to the Prime factory!")
print()
#import math function
from math import sqrt
#define prime functions
def isPrime(num):
    if num < 2 or num % 2 == 0:
        return num == 2
    divisor = 3
    while divisor <= sqrt(num):
        if num % divisor == 0:
            return False
        else:
            divisor += 2
    return True
def findNextPrime(num):
    if num < 2:
        return 2
    if num % 2 == 0:
        num -= 1
    nextnum = num + 2
    while not isPrime (nextnum):
        nextnum += 2
    return nextnum

while True:
    usercommand = input("Enter a command (factor, isprime, end): ")
#when factor function is needed
    if usercommand.lower() == 'factor':
        enteredFactor = int(input("Enter an integer > 1: "))
#if the number entered is greater than 1
        if enteredFactor > 1:
            if isPrime(enteredFactor):
                print("The prime factorization of", enteredFactor, "is:", [enteredFactor])
                print()
            else:
                lst1 = []
                d = 2
                enteredFactor0 = enteredFactor
                while d >= 2:
                # if the number could be divided by d, add to the list
                    if isPrime(d) and enteredFactor % d == 0:
                        lst1.append(d)
                        enteredFactor = enteredFactor / d
                    else:
                #if not, find the next prime and put it back into the division
                        nextPrime = findNextPrime(d)
                        d = nextPrime
                #if the number reached to a prime, add it to the list and stop there
                    if isPrime(enteredFactor):
                        lst1.append(int(enteredFactor))
                        break
                print("The prime factorization of", enteredFactor0, "is:", lst1)
                print()
        else:
            print("Illegal input: ", enteredFactor, "; input must be an integer > 1.", sep='')
            print()
#if isprime function is needed
    elif usercommand.lower() == 'isprime':
        enteredFactor = int(input("Enter an integer > 1: "))
        if enteredFactor > 1 and isPrime(enteredFactor):
            print("The number", enteredFactor, "is prime")
            print()
        elif enteredFactor < 1:
            print("Illegal input: ", enteredFactor, "; input must be an integer > 1.", sep='')
            print()
        else:
            print("The number", enteredFactor, "is not prime")
            print()
#if the user wants to stop
    elif usercommand.lower() == 'end':
        print("Thanks for using our service! Goodbye.")
        break
#if the command is wrong
    else:
        print("Command", usercommand, "not recognized. Try again!")
        print()

