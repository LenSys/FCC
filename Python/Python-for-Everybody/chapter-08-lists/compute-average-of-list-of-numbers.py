# Compute the average of a list of numbers
# (see https://books.trinket.io/pfe/08-lists.html#a-list-is-a-sequence)


# We could simply remember each number as the user entered it and use built-in functions 
# to compute the sum and count at the end.

# We make an empty list before the loop starts, and then each time we have a number, we 
# append it to the list. At the end of the program, we simply compute the sum of the 
# numbers in the list and divide it by the count of the numbers in the list to come up 
# with the average.


numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

# Code: http://www.py4e.com/code3/avelist.py