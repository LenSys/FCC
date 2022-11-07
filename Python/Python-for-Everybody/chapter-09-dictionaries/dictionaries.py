# Dictionaries
# (see https://books.trinket.io/pfe/09-dictionaries.html)


# The function dict creates a new dictionary with no items.
eng2sp = dict()
# {}
print(eng2sp)

# To add items to the dictionary, you can use square brackets:
eng2sp['one'] = 'uno'

# {'one': 'uno'}
print(eng2sp)
print("-------------------------------------------------------------")


# The order of the key-value pairs is not the same. 
# In fact, if you type the same example on your computer, you might get a different result. 
# In general, the order of items in a dictionary is unpredictable!
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# {'one': 'uno', 'three': 'tres', 'two': 'dos'}
print(eng2sp)


# That's not a problem because the elements of a dictionary are never indexed with integer indices. 
# Instead, you use the keys to look up the corresponding values:

# 'dos'
print(eng2sp['two'])
print("-------------------------------------------------------------")


# The len function works on dictionaries; it returns the number of key-value pairs:
# 3
print(len(eng2sp))
print("-------------------------------------------------------------")


# True
print('one' in eng2sp)

# False
print('uno' in eng2sp)
print("-------------------------------------------------------------")


# To see whether something appears as a value in a dictionary, you can use the method values, 
# which returns the values as a list, and then use the in operator:
vals = list(eng2sp.values())
# True
print('uno' in vals)

# For dictionaries, Python uses an algorithm called a hash table that has a remarkable property: 
# the in operator takes about the same amount of time no matter how many items there are in a dictionary.

print("-------------------------------------------------------------")


# Dictionary as a set of counters
# Suppose you are given a string and you want to count how many times each letter appears.
word = 'brontosaurus'
d = dict()
for c in word: 
    if c not in d: 
        d[c] = 1 
    else: 
        d[c] = d[c] + 1 

# {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
print(d)

# We are effectively computing a histogram, which is a statistical term for a set of counters (or frequencies).
print("-------------------------------------------------------------")


# Dictionaries have a method called get that takes a key and a default value. 
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value. 
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# 100
print(counts.get('jan', 0))

# 0
print(counts.get('tim', 0))
print("-------------------------------------------------------------")


# We can use get to write our histogram loop more concisely. 
# Because the get method automatically handles the case where a key is not in a dictionary, 
# we can reduce four lines down to one and eliminate the if statement.

word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)
print("-------------------------------------------------------------")


# Looping and dictionaries
# If you use a dictionary as the sequence in a for statement, it traverses the keys of the dictionary. 
# This loop prints each key and the corresponding value:

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

# Here's what the output looks like:
# jan 100
# chuck 1
# annie 42
print("-------------------------------------------------------------")

# If you want to print the keys in alphabetical order, you first make a list of the keys in the 
# dictionary using the keys method available in dictionary objects, and then sort that list and 
# loop through the sorted list, looking up each key and printing out key-value pairs in sorted 
# order as follows:

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])

# Here's what the output looks like:
# ['jan', 'chuck', 'annie']
# annie 42
# chuck 1
# jan 100
print("-------------------------------------------------------------")