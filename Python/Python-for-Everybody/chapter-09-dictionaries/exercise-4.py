# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# (see https://books.trinket.io/pfe/09-dictionaries.html#advanced-text-parsing)

# After all the data has been read and the dictionary has been created, look through the dictionary 
# using a maximum loop (see Section [maximumloop]) to find who has the most messages and print how 
# many messages the person has.
# 
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# 
# Enter a file name: mbox.txt
# zqian@umich.edu 195
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

maxEmail = None
maxEmailCount = None
for email, emailCount in emails.items():
    if maxEmailCount is None or maxEmailCount < emailCount:
        maxEmail = email
        maxEmailCount = emailCount

print(maxEmail, maxEmailCount)