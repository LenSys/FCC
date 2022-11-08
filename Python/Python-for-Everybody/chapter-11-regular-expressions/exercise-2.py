# Exercise 2: Write a program to look for lines of the form
# `New Revision: 39772`
# and extract the number from each of the lines using a regular expression and the 
# findall() method. Compute the average of the numbers and print out the average.
# (see https://books.trinket.io/pfe/11-regex.html)

# Enter file:mbox.txt
# 38549.7949721
# 
# Enter file:mbox-short.txt
# 39756.9259259

import re

filename = input("Enter file: ")
if len(filename) == 0:
    filename = 'mbox-short.txt'

try:
    fHandle = open(filename)
except:
    print("File '%s' could not be opened!" % filename)
    exit()

revisionNumberSum = 0
revisionNumberCount = 0
for line in fHandle:
    line = line.strip()
    regexResult = re.findall("New Revision: ([0-9]+)", line)
    if len(regexResult) == 0: continue
    revisionNumber = int(regexResult[0])
    # count sum of revision numbers
    revisionNumberSum = revisionNumberSum + revisionNumber
    # count amount of revision numbers
    revisionNumberCount = revisionNumberCount + 1
    
if revisionNumberCount > 0:
    print("%.7f" % (revisionNumberSum / revisionNumberCount))