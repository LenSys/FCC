# The most common words
# (see https://books.trinket.io/pfe/10-tuples.html#dictionaries-and-tuples)

# Coming back to our running example of the text from Romeo and Juliet Act 2, Scene 2, we can 
# augment our program to use this technique to print the ten most common words in the text as follows:

# The first part of the program which reads the file and computes the dictionary that maps each word 
# to the count of words in the document is unchanged. But instead of simply printing out counts and 
# ending the program, we construct a list of (val, key) tuples and then sort the list in reverse order.

# Since the value is first, it will be used for the comparisons. If there is more than one tuple with 
# the same value, it will look at the second element (the key), so tuples where the value is the same 
# will be further sorted by the alphabetical order of the key.

# At the end we write a nice for loop which does a multiple assignment iteration and prints out the 
# ten most common words by iterating through a slice of the list (lst[:10]).

# So now the output finally looks like what we want for our word frequency analysis.

# 61 i
# 42 and
# 40 romeo
# 34 to
# 34 the
# 32 thou
# 32 juliet
# 30 that
# 29 my
# 24 thee

# The fact that this complex data parsing and analysis can be done with an easy-to-understand 19-line 
# Python program is one reason why Python is a good choice as a language for exploring information.

import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

# Code: http://www.py4e.com/code3/count3.py