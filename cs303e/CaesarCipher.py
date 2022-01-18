# File: CaesarCipher.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/05/2020
# Date Last Modified: 10/07/2020
# Description of the Program: This program used python to decrypt and encrypt.

#let upper or lower cases do not matter
want = str(input("Enter Caesar cipher command (encrypt/decrypt): "))
lowerCase = want.lower()
#verify user input option
if lowerCase == "encrypt":
    print("You’ve asked to encrypt.")
    shiftValue = eval(input("Please enter shift value (0 .. 25): " ))
#verify the range of shift value
    if shiftValue < 0 or shiftValue > 25:
        print("Illegal shift value: ", shiftValue, sep = "")
    elif 0 <= shiftValue <= 25:
        text = input("Please enter text to encrypt: ")
#find the corresponding letter
        newString = ""
        for ch in text:
            ascValue = ord(ch)
            if 65 <= ascValue <= 90:
                w = ord(ch) - ord('A')
                x = (w + shiftValue) % 26
                y = x + ord('A')
                newString = newString + chr(y)
            elif 97 <= ascValue <= 122:
                a = ord(ch) - ord('a')
                b = (a + shiftValue) % 26
                c = b + ord('a')
                newString = newString + chr(c)
            else:
                newString = newString + chr(ascValue)
        print("The encrypted text is:", newString)
elif lowerCase == "decrypt":
    print("You’ve asked to decrypt.")
    shiftValue = eval(input("Please enter shift value (0 .. 25): "))
    if shiftValue < 0 or shiftValue > 25:
        print("Illegal shift value: ", shiftValue, sep = "")
    elif 0 <= shiftValue <= 25:
        text = input("Please enter text to decrypt: ")
        newString = ""
        shiftValue = shiftValue * -1
        for ch in text:
            ascValue = ord(ch)
            if 65 <= ascValue <= 90:
                w = ord(ch) - ord('A')
                x = (w + shiftValue) % 26
                y = x + ord('A')
                newString = newString + chr(y)
            elif 97 <= ascValue <= 122:
                a = ord(ch) - ord('a')
                b = (a + shiftValue) % 26
                c = b + ord('a')
                newString = newString + chr(c)
            else:
                newString = newString + chr(ascValue)
        print("The decrypted text is:", newString)
else:
    print("Unrecognized command: ", lowerCase, sep="")

