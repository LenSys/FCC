# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours 
# worked above 40 hours.
# 
# (see https://books.trinket.io/pfe/03-conditional.html)


# Enter Hours: 45 
# Enter Rate: 10 
# Pay: 475.0 
# Note that 475 = 40 * 10 + 5 * 15
#                 40 * 10 (normal hours * normal rate)
#               +  5 * 15 (overtime hours * overtime rate)

hours = float(input("Enter hours: "))
rate = float(input("Enter pay: "))

if hours > 40 :
    overtimeHours = hours - 40
    overtimeRate = rate * 1.5
    hours = hours - overtimeHours

    grossPay = (hours * rate) + (overtimeHours * overtimeRate)

else :
    grossPay = hours * rate

print("gross pay:", grossPay)