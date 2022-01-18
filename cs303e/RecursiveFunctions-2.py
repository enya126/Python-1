# File: RecursiveFunctions.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/19/2020
# Date Last Modified: 11/20/2020
# Description of Program: This allowed me use python to use recursive functions

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        #use recursive here to find key simutaneously
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   """ Add up the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
   if n == 0:
       return 0
   else:
       return n + addToN(n-1)

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. """
   if n == 0:
        return 0
   else:
       #divide the integer by 10 to separate each digit
        return n % 10 + findSumOfDigits(n // 10)

def decimalToBinary( n ):
   """ Given a nonnegative decimal n, return the
   binary representation as a string. """
   if n == 0:
       return 0
   else:
       binary = str(decimalToBinary(n // 2)) + str(n % 2)
       intN = int(binary)
       strN = str(intN)
       return strN

def decimalToList( n ):
   """ Given a positive decimal integer, return a list of the
   digits (as strings). """
   #create an empty list
   lst = []
   if n < 10:
       #put n into the list
       return [str(n)]
   else:
       return (decimalToList(n // 10)) + [str(n % 10)]

def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
   if s == "":
       return True
   #judge the first one and the last one of the str
   elif s[0] == s[-1]:
       #use recursive here to judge these two insides
       return isPalindrome(s[1:-1])
   else:
       return False


def findFirstUppercase( s ):
   """ Return the first uppercase letter in
   string s, if any.  Return None if there
   is none. """
   if s == "":
       return None
   else:
       if s[0].isupper():
           return s[0]
       else:
           findFirstUppercase(s[1:])


def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex. """
   strS = str(s)
   if strS != "":
       if strS[0].isupper():
           return index
       else:
           return findFirstUppercaseIndexHelper(strS[1:], index + 1)
   else:
       #if the str is empty or no upper case letter
       return -1

# The following function is already completed for you.  But
# make sure you understand what it's doing.

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in
   string s, if any.  Return -1 if there is none.  This one
   requires a helper function, which is the recursive
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )