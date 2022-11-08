# Retrieving web pages with urllib
# (see https://books.trinket.io/pfe/12-network.html)

# While we can manually send and receive data over HTTP using the socket library, there 
# is a much simpler way to perform this common task in Python by using the urllib library.

# Using urllib, you can treat a web page much like a file. You simply indicate which web 
# page you would like to retrieve and urllib handles all of the HTTP protocol and header 
# details.

# The equivalent code to read the romeo.txt file from the web using urllib is as follows:
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# Code: http://www.py4e.com/code3/urllib1.py

# Once the web page has been opened with urllib.urlopen, we can treat it like a file and 
# read through it using a for loop.

# When the program runs, we only see the output of the contents of the file. The headers 
# are still sent, but the urllib code consumes the headers and only returns the data to us.

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief
