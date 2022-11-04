# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
# (see https://books.trinket.io/pfe/02-variables.html)

hours = input("Enter hours: ")
rate = input("Enter pay: ")
grossPay = float(hours) * float(rate)

print("gross pay:", grossPay)