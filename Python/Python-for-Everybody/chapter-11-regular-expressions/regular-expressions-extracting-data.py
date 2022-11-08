# Extracting data using regular expressions
# (see https://books.trinket.io/pfe/11-regex.html)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# Code: http://www.py4e.com/code3/re05.py

# The findall() method searches the string in the second argument and returns a list 
# of all of the strings that look like email addresses. We are using a two-character 
# sequence that matches a non-whitespace character (\S).

# The output of the program is:
# ['csev@umich.edu', 'cwen@iupui.edu']

# Translating the regular expression, we are looking for substrings that have at least 
# one non-whitespace character, followed by an at-sign, followed by at least one more 
# non-whitespace character. The "\S+" matches as many non-whitespace characters as possible.

# The regular expression would match twice (csev@umich.edu and cwen@iupui.edu), but it would 
# not match the string "@2PM" because there are no non-blank characters before the at-sign.