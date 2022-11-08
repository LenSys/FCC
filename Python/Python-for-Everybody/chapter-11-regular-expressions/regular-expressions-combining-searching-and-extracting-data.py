# Regular Expressions: Combining searching and extracting
# (see https://books.trinket.io/pfe/11-regex.html)

# If we want to find numbers on lines that start with the string "X-" such as:

# X-DSPAM-Confidence: 0.8475
# X-DSPAM-Probability: 0.0000
# we don't just want any floating-point numbers from any lines. We only want to 
# extract numbers from lines that have the above syntax.

# We can construct the following regular expression to select the lines:
# ^X-.*: [0-9.]+

# Translating this, we are saying, we want lines that start with "X-", followed by zero 
# or more characters (".*"), followed by a colon (":") and then a space. After the space 
# we are looking for one or more characters that are either a digit (0-9) or a period 
# "[0-9.]+". Note that inside the square brackets, the period matches an actual period 
# (i.e., it is not a wildcard between the square brackets).

# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

# Code: http://www.py4e.com/code3/re10.py

# When we run the program, we see the data nicely filtered to show only the lines we are looking for.
# X-DSPAM-Confidence: 0.8475
# X-DSPAM-Probability: 0.0000
# X-DSPAM-Confidence: 0.6178
# X-DSPAM-Probability: 0.0000