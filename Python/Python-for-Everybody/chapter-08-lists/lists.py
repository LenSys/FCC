# Lists
# (see https://books.trinket.io/pfe/08-lists.html#a-list-is-a-sequence)


# A list is a sequence
numbers = [10, 20, 30, 40]
items = ['crunchy frog', 'ram bladder', 'lark vomit']
print("-------------------------------------------------------------")

# Lists are mutable
# Unlike strings, lists are mutable because you can change the order of items in a list or 
# reassign an item in a list.
cheeses = ["Cheddar", "Edam", "Gouda"]
print(cheeses[0])

# Traversing a list
for cheese in cheeses:
    print(cheese)


# This loop traverses the list and updates each element. 
# len returns the number of elements in the list. 
# range returns a list of indices from 0 to n − 1, where n is the length of the list. 
# Each time through the loop, i gets the index of the next element. 
# The assignment statement in the body uses i to read the old value of the element and to assign the new value.
numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print("-------------------------------------------------------------")


# The + operator concatenates lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# [1, 2, 3, 4, 5, 6]
print(c)
print("-------------------------------------------------------------")


# Similarly, the * operator repeats a list a given number of times:
# [0, 0, 0, 0]
print([0] * 4)
print("-------------------------------------------------------------")


# List slices
# The slice operator also works on lists:
t = ['a', 'b', 'c', 'd', 'e', 'f']
# ['b', 'c']
print(t[1:3])

# ['a', 'b', 'c', 'd']
print(t[:4])

# ['d', 'e', 'f']
print(t[3:])
print("-------------------------------------------------------------")


# A slice operator on the left side of an assignment can update multiple elements:
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']

# ['a', 'x', 'y', 'd', 'e', 'f']
print(t)
print("-------------------------------------------------------------")


# List methods
# Python provides methods that operate on lists. 
# For example, append adds a new element to the end of a list:
t = ['a', 'b', 'c']
t.append('d')

# ['a', 'b', 'c', 'd']
print(t)
print("-------------------------------------------------------------")


# extend takes a list as an argument and appends all of the elements:
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)

# ['a', 'b', 'c', 'd', 'e']
print(t1)
print("-------------------------------------------------------------")


# sort arranges the elements of the list from low to high:
t = ['d', 'c', 'e', 'b', 'a']
t.sort()

# ['a', 'b', 'c', 'd', 'e']
print(t)
print("-------------------------------------------------------------")


# Deleting elements
# There are several ways to delete elements from a list. 
# If you know the index of the element you want, you can use pop:
t = ['a', 'b', 'c']
x = t.pop(1)

# ['a', 'c']
print(t)

# b
print(x)

# pop modifies the list and returns the element that was removed. 
# If you don't provide an index, it deletes and returns the last element.


# If you don't need the removed value, you can use the del operator:
t = ['a', 'b', 'c']
del t[1]

# ['a', 'c']
print(t)


# If you know the element you want to remove (but not the index), you can use remove:
t = ['a', 'b', 'c']
t.remove('b')

# ['a', 'c']
print(t)


# To remove more than one element, you can use del with a slice index:
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]

# ['a', 'f']
print(t)
print("-------------------------------------------------------------")


# Lists and functions
# There are a number of built-in functions that can be used on lists that allow you 
# to quickly look through a list without writing your own loops:
nums = [3, 41, 12, 9, 74, 15]

# 6
print(len(nums))

# 74
print(max(nums))

# 3
print(min(nums))

# 154
print(sum(nums))

# 25.666666666666668
print(sum(nums)/len(nums))

# The sum() function only works when the list elements are numbers. 
# The other functions (max(), len(), etc.) work with lists of strings and 
# other types that can be comparable.

print("-------------------------------------------------------------")


# Lists and strings
# A string is a sequence of characters and a list is a sequence of values, but a list of 
# characters is not the same as a string. 
# To convert from a string to a list of characters, you can use list:

s = 'spam'
t = list(s)

# ['s', 'p', 'a', 'm']
print(t)
print("-------------------------------------------------------------")


# The list function breaks a string into individual letters. 
# If you want to break a string into words, you can use the split method:

s = 'pining for the fjords'
t = s.split()

# ['pining', 'for', 'the', 'fjords']
print(t)

# the
print(t[2])


# You can call split with an optional argument called a delimiter that specifies which 
# characters to use as word boundaries. 
# The following example uses a hyphen as a delimiter:
s = 'spam-spam-spam'
delimiter = '-'

# ['spam', 'spam', 'spam']
print(s.split(delimiter))
print("-------------------------------------------------------------")


# join is the inverse of split. It takes a list of strings and concatenates the elements. 
# join is a string method, so you have to invoke it on the delimiter and pass the list as a parameter:
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '

# 'pining for the fjords'
print(delimiter.join(t))

# To concatenate strings without spaces, you can use the empty string, "", as a delimiter.

print("-------------------------------------------------------------")


# In this example, Python only created one string object, and both a and b refer to it.
a = 'banana'
b = 'banana'
# True
print(a is b)


# But when you create two lists, you get two objects:
a = [1, 2, 3]
b = [1, 2, 3]

# False
print(a is b)


# Aliasing
# If a refers to an object and you assign b = a, then both variables refer to the same object:
a = [1, 2, 3]
b = a

# True
print(b is a)
print("-------------------------------------------------------------")


# List arguments
# The parameter t and the variable letters are aliases for the same object.
def delete_head(t):
    del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)

# ['b', 'c']
print(letters)
print("-------------------------------------------------------------")

# It is important to distinguish between operations that modify lists and operations that create new lists. 
# For example, the append method modifies a list, but the + operator creates a new list:
t1 = [1, 2]
t2 = t1.append(3)

# [1, 2, 3]
print(t1)

# None
print(t2)

t3 = t1 + [3]
# [1, 2, 3, 3]
print(t3)

# False
print(t1 is t3)
print("-------------------------------------------------------------")


# It is best practice to write a function that creates and returns a new list. 
# For example, tail returns all but the first element of a list:

# This function leaves the original list unmodified
def tail(t):
    return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)

# ['b', 'c']
print(rest)

print("-------------------------------------------------------------")

# If you want to use a method like sort that modifies the argument, but you need to keep the original 
# list as well, you can make a copy.
orig = t[:]
t.sort()