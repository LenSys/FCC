# Exercise 2: Write another program that prompts for a list of numbers as above and at the end 
# prints out both the maximum and minimum of the numbers instead of the average.
# (see https://books.trinket.io/pfe/05-iterations.html)

maxNumber = None
minNumber = None
while True:
    try:
        numberInput = input('Enter a number: ')
        if numberInput == 'done':
            break
        number = int(numberInput)
        
        if maxNumber is None or number > maxNumber:
            maxNumber = number
        
        if minNumber is None or number < minNumber:
            minNumber = number
    except:
        print("Invalid input")
        continue

print(minNumber, maxNumber)