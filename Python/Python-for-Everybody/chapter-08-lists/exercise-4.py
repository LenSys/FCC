# Exercise 4: Download a copy of the file from www.py4e.com/code3/romeo.txt
# (see https://books.trinket.io/pfe/08-lists.html#a-list-is-a-sequence)

# Write a program to open the file romeo.txt and read it line by line. For each line, split the 
# line into a list of words using the split function.

# For each word, check to see if the word is already in a list. 
# If the word is not in the list, add it to the list.

# When the program completes, sort and print the resulting words in alphabetical order.

# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']

romeoWords = list()
fHandle = open('romeo.txt')
for line in fHandle:
    words = line.split()
    for word in words:
        if word not in romeoWords:
            romeoWords.append(word)

romeoWords.sort()
print(romeoWords)