# File: Payroll.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 09/17/2020
# Date Last Modified: 09/18/2020
# Description of the Program: This program used python to compute the number of days in a month

month = eval(input("Enter a month: "))
year = eval(input("Enter a year: "))
# Is this a leap year
leapYear = (year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0))
# use selection to compute the number of days
if month == 1:
    print("January", year, "has 31 days")
elif leapYear and month == 2:
    print("February", year, "has 29 days")
elif not leapYear and month == 2:
    print("February", year, "has 28 days")
elif month == 3:
    print("March", year, "has 31 days")
elif month == 4:
    print("April", year, "has 30 days")
elif month == 5:
    print("May", year, "has 31 days")
elif month == 6:
    print("June", year, "has 30 days")
elif month == 7:
    print("July", year, "has 31 days")
elif month == 8:
    print("August", year, "has 31 days")
elif month == 9:
    print("September", year, "has 30 days")
elif month == 10:
    print("October", year, "has 31 days")
elif month == 11:
    print("November", year, "has 30 days")
elif month == 12:
    print("December", year, "has 31 days")