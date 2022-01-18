# File: ComparingLinearBinarySearch.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/5/2020
# Date Last Modified: 11/6/2020
# Description of the Program: This program used python to compare the performance of linear and binary search.

#import several functions
from random import shuffle
from math import log2
from random import randint
#create a list
lst = [x for x in range(1000)]
#define two functions
def linearSearch( lst, key ):
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

#linear search
print("Linear search:")
for ch in range(1, 6):
    n = 10 ** ch
    probe = 0
    for i in range(1, n+1):
        shuffle(lst)
        key = randint(0, 1000)
        #find a random number as key in the list
        count = linearSearch(lst, key)
        #probe = index + 1
        probe = probe + (count + 1)
    avgProbe = probe / n
    string = '<5.' + str(ch) + 'f'
    print("  Tests:", format(n, '<8'), "Average probes:", format(avgProbe, string))

#perform binary search 1000 times
probe2 = 0
for i in range(1, 1001):
    #same logic as linear research
    key = randint(0, 1000)
    count = binarySearch(lst, key)
    #only need count returned from binary research so count[-1]
    probe2 = probe2 + (count[-1] + 1)
avgProbe2 = probe2 / 1000
diffAvg = abs(log2(1000) - avgProbe2)
#print out statements
print("Binary search:")
print("  Average number of probes:", format(avgProbe2, '.3f'))
print("  Differs from log2(1000) by:", diffAvg)
