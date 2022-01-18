# File: GuessingGame.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/11/2020
# Date Last Modified: 10/12/2020
# Description of the Program: This program used python to create a guessing game.

#start the guessing game
print("Welcome to the guessing game. You have ten tries to guess my number.")
correctValue = 1458
guessChance = 0
#find the valid input guessing number
for guessChance in range (0, 10):
    guessNumber = int(input("Please enter your guess: "))
    while True:
        if guessNumber <= 0 or guessNumber >= 10000:
            print("Your guess must be between 0001 and 9999.")
            guessNumber = int(input("Please enter a valid guess: "))
        else:
            break
#if the guessed number is too small
    if 0 < guessNumber < correctValue:
        guessChance += 1
        print("Your guess is too low.")
        print("Guesses so far:", guessChance)
#if the guessed number is too big
    elif 10000 > guessNumber > correctValue:
        guessChance += 1
        print("Your guess is too high.")
        print("Guesses so far:", guessChance)
#if he/she is correct
    elif guessNumber == correctValue:
        if guessChance == 0:
            print("That’s correct!")
            print("Congratulations! You guessed it on the first try!")
            break
        else:
            guessChance += 1
            print("That’s correct!")
            print("Congratulations! You guessed it in", guessChance, "guesses.")
            break
#if 10 chances were used up
else:
    print("Game over: you ran out of guesses.")