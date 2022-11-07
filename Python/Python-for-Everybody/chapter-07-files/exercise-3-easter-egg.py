# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless 
# Easter Egg to their program Modify the program that prompts the user for the file name so that it 
# prints a funny message when the user types in the exact file name "na na boo boo". 
# The program should behave normally for all other files which exist and don't exist. 
# (see https://books.trinket.io/pfe/07-files.html#searching-through-a-file)

# Here is a sample execution of the program:
# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt

# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt

# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!

filename = input('Enter the file name: ')
try:
    fHandle = open(filename)
except:
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    
    print('File cannot be opened:', filename)
    exit()

for line in fHandle:
    line = line.rstrip().upper()
    print(line)