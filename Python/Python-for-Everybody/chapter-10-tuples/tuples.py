# Tuples
# (see https://books.trinket.io/pfe/10-tuples.html)

# Tuples are immutable
# A tuple is a sequence of values much like a list.
# The important difference is that tuples are immutable.

# Syntactically, a tuple is a comma-separated list of values:
# It is common to enclose tuples in parentheses to help us quickly identify tuples when we look 
# at Python code:
t = ('a', 'b', 'c', 'd', 'e')

# Another way to construct a tuple is the built-in function tuple.
t = tuple()


# If the argument is a sequence (string, list, or tuple), the result of the call to tuple is a 
# tuple with the elements of the sequence:
t = tuple('lupins')

# ('l', 'u', 'p', 'i', 'n', 's')
print(t)
print("-------------------------------------------------------------")


# Most list operators also work on tuples. The bracket operator indexes an element:
t = ('a', 'b', 'c', 'd', 'e')
# a
print(t[0])
print("-------------------------------------------------------------")


# And the slice operator selects a range of elements.
t = ('a', 'b', 'c', 'd', 'e')
# ('b', 'c')
print(t[1:3])


# You can not modify one of the elements of the tuple
# You can't modify the elements of a tuple, but you can replace one tuple with another:
t = ('a', 'b', 'c', 'd', 'e')
t = ('A',) + t[1:]
# ('A', 'b', 'c', 'd', 'e')
print(t)
print("-------------------------------------------------------------")


# Comparing tuples
# The comparison operators work with tuples and other sequences. Python starts by comparing the 
# first element from each sequence. If they are equal, it goes on to the next element, and so on, 
# until it finds elements that differ. Subsequent elements are not considered 
# (even if they are really big).

# True
print((0, 1, 2) < (0, 3, 4))
# True
print((0, 1, 2000000) < (0, 3, 4))
print("-------------------------------------------------------------")


# The sort function works the same way. It sorts primarily by first element, but in the case of a tie, 
# it sorts by second element, and so on.

# This feature lends itself to a pattern called DSU for
# -------------------------------------------------------------
# Decorate
# a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence,
# Sort
# the list of tuples using the Python built-in sort, and
# Undecorate
# by extracting the sorted elements of the sequence.
# -------------------------------------------------------------


# Tuple assignment
# One of the unique syntactic features of the Python language is the ability to have a tuple on the 
# left side of an assignment statement. This allows you to assign more than one variable at a time 
# when the left side is a sequence.

# In this example we have a two-element list (which is a sequence) and assign the first and second 
# elements of the sequence to the variables x and y in a single statement.

m = [ 'have', 'fun' ]
x, y = m
# 'have'
print(x)
# 'fun'
print(y)

# A particularly clever application of tuple assignment allows us to swap the values of two variables 
# in a single statement:
a = 1
b = 2
a, b = b, a
# 2
print(a)
# 1
print(b)
print("-------------------------------------------------------------")


addr = 'monty@python.org'
uname, domain = addr.split('@')
# monty
print(uname)
# python.org
print(domain)
print("-------------------------------------------------------------")


# Dictionaries and tuples
# Dictionaries have a method called items that returns a list of tuples, where each tuple is a key-value pair:
d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
# [('a', 10), ('b', 1), ('c', 22)]
print(t)

# As you should expect from a dictionary, the items are in no particular order.
# However, since the list of tuples is a list, and tuples are comparable, we can now sort the list 
# of tuples. 
# Converting a dictionary to a list of tuples is a way for us to output the contents of a dictionary 
# sorted by key:

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
# [('b', 1), ('a', 10), ('c', 22)]
print(t)

t.sort()

# The new list is sorted in ascending alphabetical order by the key value.
# [('a', 10), ('b', 1), ('c', 22)]
print(t)
print("-------------------------------------------------------------")

# Multiple assignment with dictionaries
# Combining items, tuple assignment, and for, you can see a nice code pattern for traversing the keys 
# and values of a dictionary in a single loop:

for key, val in list(d.items()):
    print(val, key)

# This loop has two iteration variables because items returns a list of tuples and key, val is a tuple 
# assignment that successively iterates through each of the key-value pairs in the dictionary.

# Output is:
# 10 a
# 22 c
# 1 b

# If we combine these two techniques, we can print out the contents of a dictionary sorted by the value 
# stored in each key-value pair.

# To do this, we first make a list of tuples where each tuple is (value, key). The items method would 
# give us a list of (key, value) tuples, but this time we want to sort by value, not key. Once we have 
# constructed the list with the value-key tuples, it is a simple matter to sort the list in reverse order 
# and print out the new, sorted list.

d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items() :
    l.append( (val, key) )

# [(10, 'a'), (22, 'c'), (1, 'b')]
print(l)

l.sort(reverse=True)

# [(22, 'c'), (10, 'a'), (1, 'b')]
print(l)
print("-------------------------------------------------------------")


# Because tuples are immutable, they don't provide methods like sort and reverse, which modify 
# existing lists. However Python provides the built-in functions sorted and reversed, which take 
# any sequence as a parameter and return a new sequence with the same elements in a different order.

