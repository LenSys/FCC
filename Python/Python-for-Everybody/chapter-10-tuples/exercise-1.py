# Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull 
# out the addresses from the line. Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of 
# (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the 
# person who has the most commits.


# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# 
# Enter a file name: mbox.txt
# zqian@umich.edu 195

filename = input('Enter the file name: ')
if len(filename) == 0: 
    filename = "mbox-short.txt"
try:
    fHandle = open(filename)
except:
    print('File cannot be opened:', filename)
    exit()

messages = dict()
for line in fHandle:
    words = line.split()
    # check for valid word length
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    
    email = words[1]
    # word histogram
    messages[email] = messages.get(email, 0) + 1

# print(messages)

# Sort the messages dictionary by value
messagesList = list()
for email, count in list(messages.items()):
    messagesList.append((count, email))

messagesList.sort(reverse=True)

# print the first message
for count, email in messagesList[:1]:
    print(email, count)