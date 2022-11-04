# Maximum and minimum loops
# (see https://books.trinket.io/pfe/05-iterations.html)

# To find the largest value in a list or sequence, we construct the following loop:

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

# When the program executes, the output is as follows:

# Before: None
# Loop: 3 3
# Loop: 41 41
# Loop: 12 41
# Loop: 9 41
# Loop: 74 74
# Loop: 15 74
# Largest: 74
print("------------------------------------------------------")


# To compute the smallest number, the code is very similar with one small change:

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

print("------------------------------------------------------")


def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

print("Smallest: ")
print(min([3, 1, 0, -5, 11]))
print("------------------------------------------------------")