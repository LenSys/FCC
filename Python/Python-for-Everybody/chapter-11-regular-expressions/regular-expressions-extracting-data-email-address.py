# Extracting data using regular expressions: Email address
# (see https://books.trinket.io/pfe/11-regex.html)

# Search for lines that have an at sign between characters
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

# Code: http://www.py4e.com/code3/re06.py

# We read each line and then extract all the substrings that match our regular expression. 
# Since findall() returns a list, we simply check if the number of elements in our returned 
# list is more than zero to print only lines where we found at least one substring that looks 
# like an email address.

# If we run the program on mbox.txt we get the following output:
#
# ['wagnermr@iupui.edu']
# ['cwen@iupui.edu']
# ['<postmaster@collab.sakaiproject.org>']
# ['<200801032122.m03LMFo4005148@nakamura.uits.iupui.edu>']
# ['<source@collab.sakaiproject.org>;']
# ['<source@collab.sakaiproject.org>;']
# ['<source@collab.sakaiproject.org>;']
# ['apache@localhost)']
# ['source@collab.sakaiproject.org;']

# Some of our email addresses have incorrect characters like "<" or ";" at the beginning or 
# end. Let's declare that we are only interested in the portion of the string that starts 
# and ends with a letter or a number.
