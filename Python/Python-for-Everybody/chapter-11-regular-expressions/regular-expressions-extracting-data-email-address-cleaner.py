# Extracting data using regular expressions: Email address
# (see https://books.trinket.io/pfe/11-regex.html)

# Search for lines that have an at sign between characters
# The characters must be a letter or number
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# Code: http://www.py4e.com/code3/re07.py

# Some of our email addresses have incorrect characters like "<" or ";" at the beginning or 
# end. Let's declare that we are only interested in the portion of the string that starts 
# and ends with a letter or a number.

# To do this, we use another feature of regular expressions. Square brackets are used to 
# indicate a set of multiple acceptable characters we are willing to consider matching. 
# In a sense, the "\S" is asking to match the set of "non-whitespace characters". 
# Now we will be a little more explicit in terms of the characters we will match.

# Here is our new regular expression:
# [a-zA-Z0-9]\S*@\S*[a-zA-Z]

# This is getting a little complicated and you can begin to see why regular expressions 
# are their own little language unto themselves. Translating this regular expression, we 
# are looking for substrings that start with a single lowercase letter, uppercase letter, 
# or number "[a-zA-Z0-9]", followed by zero or more non-blank characters ("\S*"), 
# followed by an at-sign, followed by zero or more non-blank characters ("\S*"), 
# followed by an uppercase or lowercase letter. Note that we switched from "+" to "*" to 
# indicate zero or more non-blank characters since "[a-zA-Z0-9]" is already one non-blank 
# character. Remember that the "*" or "+" applies to the single character immediately to 
# the left of the plus or asterisk.

# ...
# ['wagnermr@iupui.edu']
# ['cwen@iupui.edu']
# ['postmaster@collab.sakaiproject.org']
# ['200801032122.m03LMFo4005148@nakamura.uits.iupui.edu']
# ['source@collab.sakaiproject.org']
# ['source@collab.sakaiproject.org']
# ['source@collab.sakaiproject.org']
# ['apache@localhost']

# Notice that on the "source@collab.sakaiproject.org" lines, our regular expression 
# eliminated two letters at the end of the string (">;"). This is because when we 
# append "[a-zA-Z]" to the end of our regular expression, we are demanding that 
# whatever string the regular expression parser finds must end with a letter. So 
# when it sees the ">" after "sakaiproject.org>;" it simply stops at the last "matching" 
# letter it found (i.e., the "g" was the last good match).

# Also note that the output of the program is a Python list that has a string as the 
# single element in the list.

