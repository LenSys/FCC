# Regular Expressions: Combining searching and extracting
# (see https://books.trinket.io/pfe/11-regex.html)

# Now we have to solve the problem of extracting the numbers. While it would be simple enough 
# to use split, we can use another feature of regular expressions to both search and parse 
# the line at the same time.

# Parentheses are another special character in regular expressions. When you add parentheses 
# to a regular expression, they are ignored when matching the string. But when you are using 
# findall(), parentheses indicate that while you want the whole expression to match, you 
# only are interested in extracting a portion of the substring that matches the regular 
# expression.

# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# Code: http://www.py4e.com/code3/re11.py

# Instead of calling search(), we add parentheses around the part of the regular expression 
# that represents the floating-point number to indicate we only want findall() to give us 
# back the floating-point number portion of the matching string.

# The output from this program is as follows:

# ['0.8475']
# ['0.0000']
# ['0.6178']
# ['0.0000']
# ['0.6961']
# ['0.0000']
# ..

# The numbers are still in a list and need to be converted from strings to floating point, 
# but we have used the power of regular expressions to both search and extract the 
# information we found interesting.
