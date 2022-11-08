# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document 
# from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of 
# characters in the document. Don't worry about the headers for this exercise, simply show 
# the first 3000 characters of the document contents.
# (see https://books.trinket.io/pfe/12-network.html)

url = input("Enter url: ")
if len(url) == 0:
    url = "http://data.pr4e.org/romeo.txt"

import urllib.request

try:
    fhand = urllib.request.urlopen(url)
except:
    print("Invalid url!")
    exit()

fileData = ""
for line in fhand:
    # print(line.decode().strip())
    # count length of file data
    fileData = fileData + line.decode().strip()

print(fileData[:3001])
print(len(fileData), "characters")

# url: http://data.pr4e.org/mbox-short.txt
# url: http://data.pr4e.org/romeo.txt