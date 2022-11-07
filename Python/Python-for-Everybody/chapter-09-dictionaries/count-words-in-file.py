# We will write a Python program to read through the lines of the file, break each line into a 
# list of words, and then loop through each of the words in the line and count each word using a dictionary.
# (see https://books.trinket.io/pfe/09-dictionaries.html)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# Code: http://www.py4e.com/code3/count1.py