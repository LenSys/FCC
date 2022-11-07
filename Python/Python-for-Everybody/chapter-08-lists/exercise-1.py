# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first 
# and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that contains all but 
# the first and last elements.

def chop(elements):
    del elements[len(elements) - 1]
    del elements[0]


def middle(elements):
    l = len(elements)
    return elements[1:l - 1]


elements1 = ['a', 'b', 'c', 'd', 'e']
chop(elements1)
print(elements1)
print("-------------------------------------------------------------")

elements2 = ['a', 'b', 'c', 'd', 'e']
elements3 = middle(elements2)
print(elements2)
print(elements3)