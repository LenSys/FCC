# Exercise 2: Write a program to prompt for a file name, and then read through the file and look 
# for lines of the form:
# (see https://books.trinket.io/pfe/07-files.html#searching-through-a-file)

# X-DSPAM-Confidence:0.8475

# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the 
# floating-point number on the line. Count these lines and then compute the total of the spam 
# confidence values from these lines. When you reach the end of the file, print out the average 
# spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.


filename = input('Enter the file name: ')
try:
    fHandle = open(filename)
except:
    print('File cannot be opened:', filename)
    exit()

countLines = 0
completeSpamConfidence = 0
for line in fHandle:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        # count lines to be able to calculate average spam confidence later
        countLines = countLines + 1

        # find colon in line
        colonPos = line.find(':')
        
        # convert spam confidence number to float
        spamConfidence = float(line[colonPos + 1:])
        
        # add current spam confidence to complete spam confidence
        completeSpamConfidence = completeSpamConfidence + spamConfidence
        
if countLines > 0:
    print("Average spam confidence: %f" % ((completeSpamConfidence / countLines)))
    