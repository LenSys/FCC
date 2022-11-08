# Regular Expressions: Extract time of day
# (see https://books.trinket.io/pfe/11-regex.html)

# We can use regular expressions to redo an exercise from earlier in the book where we 
# were interested in the time of day of each mail message. We looked for lines of the form:

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# and wanted to extract the hour of the day for each line. Previously we did this with two 
# calls to split. First the line was split into words and then we pulled out the fifth word 
# and split it again on the colon character to pull out the two characters we were interested 
# in.

# While this worked, it actually results in pretty brittle code that is assuming the lines 
# are nicely formatted. If you were to add enough error checking (or a big try/except block) 
# to insure that your program never failed when presented with incorrectly formatted lines, 
# the code would balloon to 10-15 lines of code that was pretty hard to read.

# We can do this in a far simpler way with the following regular expression:
# ^From .* [0-9][0-9]:

# The translation of this regular expression is that we are looking for lines that start with 
# "From " (note the space), followed by any number of characters (".*"), followed by a space, 
# followed by two digits "[0-9][0-9]", followed by a colon character. This is the definition 
# of the kinds of lines we are looking for.

# In order to pull out only the hour using findall(), we add parentheses around the two digits 
# as follows:

# ^From .* ([0-9][0-9]):
# This results in the following program:

# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)

# Code: http://www.py4e.com/code3/re13.py

# When the program runs, it produces the following output:
# 
# ['09']
# ['18']
# ['16']
# ['15']
# ...
