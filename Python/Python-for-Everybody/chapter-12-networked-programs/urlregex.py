# Parsing HTML using regular expressions
# (see https://books.trinket.io/pfe/12-network.html)

# One simple way to parse HTML is to use regular expressions to repeatedly search for 
# and extract substrings that match a particular pattern.

# Here is a simple web page:
# 
# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <a href="http://www.dr-chuck.com/page2.htm">
# Second Page</a>.
# </p>

# We can construct a well-formed regular expression to match and extract the link values 
# from the above text as follows:
# href="http://.+?"

# Search for lines that start with From and have an at sign
import urllib.request, urllib.parse, urllib.error
import re

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())

# Code: http://www.py4e.com/code3/urlregex.py

# python urlregex.py
# Enter - http://www.dr-chuck.com/page1.htm
# http://www.dr-chuck.com/page2.htm