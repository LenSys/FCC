# Exercise 5: Write a program to read through the mail box data and when you find line that 
# starts with "From", you will split the line into words using the split function. 
# We are interested in who sent the message, which is the second word on the From line.
# # (see https://books.trinket.io/pfe/08-lists.html#a-list-is-a-sequence)

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# You will parse the From line and print out the second word for each From line, then you will 
# also count the number of From (not From:) lines and print out a count at the end.

# This is a good sample output with a few lines removed:
# python fromcount.py
# Enter a file name: mbox-short.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# 
# [...some output removed...]
# 
# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word

filename = input('Enter the file name: ')
try:
    fHandle = open(filename)
except:
    print('File cannot be opened:', filename)
    exit()

countFromLines = 0
for line in fHandle:
    words = line.split()

    # check for valid words length
    if len(words) == 0: 
        continue
    
    # check if first word is "From"
    if words[0] == "From":
        # print second word
        print(words[1])
        # count from lines
        countFromLines = countFromLines + 1

print("There were %d lines in the file with From as the first word" % countFromLines)