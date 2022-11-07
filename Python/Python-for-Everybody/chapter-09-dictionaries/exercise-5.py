# Exercise 5: This program records the domain name (instead of the address) where the message was 
# sent from instead of who the mail came from (i.e., the whole email address). At the end of the 
# program, print out the contents of your dictionary.
# (see https://books.trinket.io/pfe/09-dictionaries.html#advanced-text-parsing)

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
filename = input('Enter the file name: ')
try:
    fHandle = open(filename)
except:
    print('File cannot be opened:', filename)
    exit()

domains = dict()
for line in fHandle:
    words = line.split()
    # check for valid word length
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    
    email = words[1]
    domainParts = email.split("@")
    domain = domainParts[1]
    # word histogram
    domains[domain] = domains.get(domain, 0) + 1

print(domains)