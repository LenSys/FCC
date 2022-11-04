# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a 
# function called computepay which takes two parameters (hours and rate).

# (see https://books.trinket.io/pfe/04-functions.html)

def computepay(hours, rate):
    if hours > 40 :
        overtimeHours = hours - 40
        overtimeRate = rate * 1.5
        hours = hours - overtimeHours

        grossPay = (hours * rate) + (overtimeHours * overtimeRate)

    else :
        grossPay = hours * rate
    
    return grossPay


try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter pay: "))

    grossPay = computepay(hours, rate)

    print("gross pay:", grossPay)
except:
    print("Error, please enter numeric input")