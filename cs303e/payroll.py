# File: Payroll.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 09/17/2020
# Date Last Modified: 09/18/2020
# Description of the Program: This program used python to create a payroll for a person

# Enter info for employee
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
rate = float(input("Enter hourly pay rate: "))
grosspay = float(hours * rate)
federalTax = float(input("Enter federal tax withholding rate: "))
stateTax = float(input("Enter state tax withholding rate: "))
federalWithholding = float(grosspay * federalTax)
stateWithholding = float(grosspay * stateTax)
deduction = float(federalWithholding + stateWithholding)
total = float(grosspay - deduction)

# print the payroll
print("\nEmployee Name: ", format(name, "5s"), sep = "")
print("Hours Worked: ", format(hours,".1f"))
print("Pay Rate: $", format(rate, ".2f"), sep = "")
print("Gross Pay: $", format(grosspay, ".2f"), sep = "")
print("Deductions: ")
print("  Federal Withholding ", "(", format(federalTax, "2.1%"), "): ", "$", format(federalWithholding, ".2f"), sep = "")
print("  State Withholding ", "(", format(stateTax, "2.1%"), "): ", "$", format(stateWithholding, ".2f"), sep = "")
print("  Total Deduction: $", format(deduction, ".2f"), sep = "")
print("Net Pay: ", format(total, "5.2f"), sep = "")