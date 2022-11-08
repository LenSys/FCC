# Exercise 3: Write a program that reads a file and prints the letters in decreasing order 
# of frequency. Your program should convert all the input to lower case and only count the 
# letters a-z. Your program should not count spaces, digits, punctuation, or anything other 
# than the letters a-z. Find text samples from several different languages and see how letter 
# frequency varies between languages. Compare your results with the tables at 
# https://en.wikipedia.org/wiki/Letter_frequency.

import string

filename = input('Enter the file name: ')
if len(filename) == 0: 
    filename = "letters-en.txt"
try:
    fHandle = open(filename)
except:
    print('File cannot be opened:', filename)
    exit()

letters = dict()
for line in fHandle:
    # remove punctuation in line
    line = line.translate(line.maketrans('', '', string.punctuation))
    # set line to lowercase
    line = line.lower()

    words = line.split()
    # check for valid word length
    if len(words) == 0 : continue
    
    for word in words:
        for letter in word:
            # only count letters a to z
            if letter < 'a' or letter > 'z': 
                continue
            # letter histogram
            letters[letter] = letters.get(letter, 0) + 1
    
# print(letters)

# Sort the messages dictionary by value
lettersList = list()
for key, val in list(letters.items()):
    lettersList.append((val, key))

lettersList.sort(reverse=True)

# print the first message
for key, val in lettersList[:10]:
    print(val, key)