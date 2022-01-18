# File: CaesarCipherFile.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/12/2020
# Date Last Modified: 11/13/2020
# Description of the Program: This program used python to write and read Caesar Cipher functions in a file
import os.path
def main():
    # let upper or lower cases do not matter
    want = str(input("Enter Caesar cipher command (encrypt/decrypt): "))
    lowerCase = want.lower()
    # verify user input option
    if lowerCase == "encrypt":
        print("You’ve asked to encrypt.")
        shiftValue = eval(input("Please enter shift value (0 .. 25): "))
        # verify the range of shift value
        if shiftValue < 0 or shiftValue > 25:
            print("Illegal shift value: ", shiftValue, sep="")
        elif 0 <= shiftValue <= 25:
            text = input("Please enter filename with text to encrypt: ")
            if not os.path.isfile(text):
                print("File does not exist")
                return
            else:
                print("The input filename is", text)
                print("The output filename is ", text, "-Enc", sep="")
                newString = ""
                #open the file that we want to encrypt
                infile = open(text, "r")
                read = infile.read()
                for ch in read:
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
                # create an outfile and write into the file
                outfile = open(text + "-Enc", "w")
                outfile.write(newString)
    elif lowerCase == "decrypt":
        print("You’ve asked to decrypt.")
        shiftValue = eval(input("Please enter shift value (0 .. 25): "))
        if shiftValue < 0 or shiftValue > 25:
            print("Illegal shift value: ", shiftValue, sep="")
        elif 0 <= shiftValue <= 25:
            text = input("Please enter filename with text to decrypt: ")
            if not os.path.isfile(text):
                print("File does not exist")
                return
            else:
                print("The input filename is", text)
                print("The output filename is ", text, "-Dec", sep="")
                newString = ""
                shiftValue = shiftValue * -1
                # #open the file that we want to decrypt
                infile = open(text, "r")
                read = infile.read()
                for ch in read:
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
                #create an outfile and write into the file
                outfile = open(text + "-Dec", "w")
                outfile.write(newString)
    else:
        print("Unrecognized command: ", lowerCase, sep="")
