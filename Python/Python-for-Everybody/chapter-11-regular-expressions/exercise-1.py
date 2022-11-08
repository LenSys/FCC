# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the 
# regular expression:
# (see https://books.trinket.io/pfe/11-regex.html)

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-

# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4218 lines that matched java$

import re
filename = 'mbox.txt'
regex = input("Enter a regular expression: ")
fHandle = open(filename)

regexResultCount = 0
for line in fHandle:
    line = line.rstrip()
    regexResult = re.findall(regex, line)
    if(len(regexResult) > 0):
        regexResultCount = regexResultCount + 1

print("%s had %d lines that matched %s" % (filename, regexResultCount, regex))