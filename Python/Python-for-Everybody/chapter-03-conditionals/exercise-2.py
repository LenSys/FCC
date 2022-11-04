# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input 
# gracefully by printing a message and exiting the program. 
# 
# The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input
# 
# (see https://books.trinket.io/pfe/03-conditional.html)


# Enter Hours: 45 
# Enter Rate: 10 
# Pay: 475.0 
# Note that 475 = 40 * 10 + 5 * 15
#                 40 * 10 (normal hours * normal rate)
#               +  5 * 15 (overtime hours * overtime rate)

try:
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
except:
    print("Error, please enter numeric input")