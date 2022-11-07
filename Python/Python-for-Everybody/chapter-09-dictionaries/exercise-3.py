# Exercise 3: Write a program to read through a mail log, build a histogram using a 
# dictionary to count how many messages have come from each email address, and print 
# the dictionary.
# (see https://books.trinket.io/pfe/09-dictionaries.html#advanced-text-parsing)

# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

filename = input('Enter the file name: ')
try:
    fHandle = open(filename)
except:
    print('File cannot be opened:', filename)
    exit()

emails = dict()
for line in fHandle:
    words = line.split()
    # check for valid word length
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    
    email = words[1]
    # word histogram
    emails[email] = emails.get(email, 0) + 1

print(emails)