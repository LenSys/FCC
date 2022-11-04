# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except 
# and print an error message and skip to the next number.
# (see https://books.trinket.io/pfe/05-iterations.html)

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

sum = 0
count = 0
while True:
    try:
        numberInput = input('Enter a number: ')
        if numberInput == 'done':
            break
        number = int(numberInput)
        sum = sum + number
        count = count + 1
    except:
        print("Invalid input")
        continue



if count > 0:
    average = sum / count
else:
    average = 0

print(sum, count, average)