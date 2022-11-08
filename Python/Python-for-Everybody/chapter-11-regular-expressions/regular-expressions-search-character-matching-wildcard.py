# Regular Expressions: search()
# (see https://books.trinket.io/pfe/11-regex.html)

# Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)

# Code: http://www.py4e.com/code3/re04.py

# The search string "^From:.+@" will successfully match lines that start with "From:", 
# followed by one or more characters (".+"), followed by an at-sign.