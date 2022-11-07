# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit 
# was done. To do this look for lines that start with "From", then look for the third word and keep a 
# running count of each of the days of the week. At the end of the program print out the contents of 
# your dictionary (order does not matter).
# (see https://books.trinket.io/pfe/09-dictionaries.html#advanced-text-parsing)

# Sample Line:
#    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Sample Execution:
# 
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

filename = input('Enter the file name: ')
try:
    fHandle = open(filename)
except:
    print('File cannot be opened:', filename)
    exit()

days = dict()
for line in fHandle:
    words = line.split()
    # check for valid word length
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    
    # word histogram
    days[words[2]] = days.get(words[2], 0) + 1

print(days)