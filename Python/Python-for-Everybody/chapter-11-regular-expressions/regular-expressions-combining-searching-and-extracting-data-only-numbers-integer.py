# Regular Expressions: Combining searching and extracting
# (see https://books.trinket.io/pfe/11-regex.html)

# As another example of this technique, if you look at the file there are a number of lines 
# of the form:

# Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
# If we wanted to extract all of the revision numbers (the integer number at the end of 
# these lines) using the same technique as above, we could write the following program:

# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# Code: http://www.py4e.com/code3/re12.py

# Translating our regular expression, we are looking for lines that start with "Details:", 
# followed by any number of characters (".*"), followed by "rev=", and then by one or more 
# digits. We want to find lines that match the entire expression but we only want to extract 
# the integer number at the end of the line, so we surround "[0-9]+" with parentheses.

# When we run the program, we get the following output:

# ['39772']
# ['39771']
# ['39770']
# ['39769']
# ...
# Remember that the "[0-9]+" is "greedy" and it tries to make as large a string of digits as 
# possible before extracting those digits. This "greedy" behavior is why we get all five 
# digits for each number. The regular expression library expands in both directions until 
# it encounters a non-digit, or the beginning or the end of a line.

