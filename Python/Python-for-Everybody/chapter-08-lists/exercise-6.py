# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints 
# out the maximum and minimum of the numbers at the end when the user enters "done". 
# Write the program to store the numbers the user enters in a list and use the max() 
# and min() functions to compute the maximum and minimum numbers after the loop completes.
# # (see https://books.trinket.io/pfe/08-lists.html#a-list-is-a-sequence)

# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

numbers = list()
while True:
    try:
        numberInput = input('Enter a number: ')
        if numberInput == 'done':
            break
        number = float(numberInput)

        numbers.append(number)
    except:
        print("Invalid number")
        continue

print("Maximum: %.1f" % max(numbers))
print("Minimum: %.1f" % min(numbers))