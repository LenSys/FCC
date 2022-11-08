# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the "From" line by finding the time string and then splitting that 
# string into parts using the colon character. Once you have accumulated the counts for each hour, 
# print out the counts, one per line, sorted by hour as shown below.

# Sample Execution:
# 
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

filename = input('Enter the file name: ')
if len(filename) == 0: 
    filename = "mbox-short.txt"
try:
    fHandle = open(filename)
except:
    print('File cannot be opened:', filename)
    exit()

hours = dict()
for line in fHandle:
    words = line.split()
    # check for valid word length
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    
    time = words[5]
    hour, minutes, seconds = time.split(':')
    # hours histogram
    hours[hour] = hours.get(hour, 0) + 1

# print(hours)

hoursList = list(hours.items())
# sort by hours in ascending order
hoursList.sort()

# print the first message
for key, val in hoursList:
    print(key, val)