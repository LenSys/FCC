# Sort words shortest to longest
# (see https://books.trinket.io/pfe/10-tuples.html)

# Suppose you have a list of words and you want to sort them from longest to shortest:
# The first loop builds a list of tuples, where each tuple is a word preceded by its length.
# sort compares the first element, length, first, and only considers the second element to break ties. 
# The keyword argument reverse=True tells sort to go in decreasing order.
# The second loop traverses the list of tuples and builds a list of words in descending order of length. 
# The four-character words are sorted in reverse alphabetical order, so "what" appears before "soft" in 
# the following list.

# The output of the program is as follows:
# 
# ['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']


txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)
# print(t)

res = list()
for length, word in t:
    res.append(word)

print(res)

# Code: http://www.py4e.com/code3/soft.py