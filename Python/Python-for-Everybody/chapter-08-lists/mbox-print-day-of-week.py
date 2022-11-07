# Print day of week
# (see https://books.trinket.io/pfe/08-lists.html#a-list-is-a-sequence)

# What if we wanted to print out the day of the week from those lines that start with "From "?
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# The split method is very effective when faced with this kind of problem. 
# We can write a small program that looks for lines where the line starts with "From ", 
# split those lines, and then print out the third word in the line:

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])

# Code: http://www.py4e.com/code3/search5.py