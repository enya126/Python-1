# File: MyStringFunctions.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/29/2020
# Date Last Modified: 10/31/2020
# Description of the Program: This program used python to create
# a library of functions for manipulating instances of that data type.

#define several functions that works for strings.
def myAppend( str, ch ):
    # Return a new string that is like str but with
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count = 0
    for i in str:
        if ch == i:
            count += 1
    return count

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1 + str2

def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    if str == "":
        print("Empty string: no min value")
        return
    else:
        # assign the minimum value to the first element in string
        minValue = ord(str[0])
        for ch in range(0, len(str)):
            newValue = ord(str[ch])
            if newValue <= minValue:
                minValue = newValue
        return chr(minValue)


def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if i > len(str):
        print("Invalid index")
        return
    r1 = str[0:i]
    r2 = str[i:]
    return r1 + ch + r2

def myPop( str, i ):
    # Return two results:
    # 1. a new string that is like str but with the ith
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or
    # equal to len(str), and return str unchanged and None
    if i > len(str):
        return str, None
    else:
        r1 = str[0:i]
        r2 = str[i + 1:]
        removedElement = str[i]
        return r1 + r2, removedElement

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    if ch not in str:
        return -1
    else:
        for i in range(0, len(str)):
            if str[i] == ch:
                return i

def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    if ch not in str:
        return -1
    else:
        for i in range(len(str) - 1, 0, -1):
            if str[i] == ch:
                return i

def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch
    # removed.  If there is none, return str.
    i = 0
    while i < len(str):
        if str[i] == ch:
            return str[:i] + str[i + 1:]
        i += 1
    #if there is non, return str.
    else:
        return str

def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    i = 0
    newStr = ""
    while i < len(str):
        if str[i] != ch:
            newStr = newStr + str[i]
        i += 1
    return newStr

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.
    reverseStr = str[::-1]
    return reverseStr
