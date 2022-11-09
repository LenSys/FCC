# Using Objects
# (see https://books.trinket.io/pfe/14-objects.html)

# It turns out we have been using objects all along in this class. 
# Python provides us with many built-in objects.

stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])

print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))

# Code: http://www.py4e.com/code3/party1.py