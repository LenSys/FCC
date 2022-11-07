# Print day of week using split
# (see https://books.trinket.io/pfe/08-lists.html#a-list-is-a-sequence)

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    # check for valid word length
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])