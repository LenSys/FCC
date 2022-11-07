# Advanced text parsing
# (see https://books.trinket.io/pfe/09-dictionaries.html#advanced-text-parsing)

# The actual romeo text has lots of punctuation, as shown below.
# But, soft! what light through yonder window breaks?
# It is the east, and Juliet is the sun.
# Arise, fair sun, and kill the envious moon,
# Who is already sick and pale with grief,

# Since the Python split function looks for spaces and treats words as tokens separated by spaces, 
# we would treat the words "soft!" and "soft" as different words and create a separate dictionary 
# entry for each word.

# Also since the file has capitalization, we would treat "who" and "Who" as different words with 
# different counts.

# We can solve both these problems by using the string methods lower, punctuation, and translate. 
# The translate is the most subtle of the methods. Here is the documentation for translate:
#
# line.translate(str.maketrans(fromstr, tostr, deletestr))
# 
# Replace the characters in fromstr with the character in the same position in tostr and delete all 
# characters that are in deletestr. The fromstr and tostr can be empty strings and the deletestr parameter 
# can be omitted.

# We will not specify the table but we will use the deletechars parameter to delete all of the punctuation. We will even let Python tell us the list of characters that it considers "punctuation":
# import string
# string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# The following is an abbreviated version of the output:
# 
# Enter the file name: romeo-full.txt
# {'swearst': 1, 'all': 6, 'afeard': 1, 'leave': 2, 'these': 2,
# 'kinsmen': 2, 'what': 11, 'thinkst': 1, 'love': 24, 'cloak': 1,
# a': 24, 'orchard': 2, 'light': 5, 'lovers': 2, 'romeo': 40,
# 'maiden': 1, 'whiteupturned': 1, 'juliet': 32, 'gentleman': 1,
# 'it': 22, 'leans': 1, 'canst': 1, 'having': 1, ...}


import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# Code: http://www.py4e.com/code3/count2.py
# Or select Download from this trinket's left-hand menu