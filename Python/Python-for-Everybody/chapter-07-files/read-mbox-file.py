# Reading files
# (see https://books.trinket.io/pfe/07-files.html)

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# Code: http://www.py4e.com/code3/open.py