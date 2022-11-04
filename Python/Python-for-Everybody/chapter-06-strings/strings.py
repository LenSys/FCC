# Strings
# (see https://books.trinket.io/pfe/06-strings.html)

# get second letter of string 'banana'
fruit = 'banana'
letter = fruit[1]
print(letter)
print("------------------------------")


# get length of string
fruit = 'banana'
length = len(fruit)
print(length)
last = fruit[length-1]
print(last)
print("------------------------------")


# Traversal through a string with a loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
print("------------------------------")


# Another way to write a traversal is with a for loop:
for char in fruit:
    print(char)
print("------------------------------")


# String slices
s = 'Monty Python'
# 'Monty'
print(s[0:5])

# 'Python'
print(s[6:12])
print("------------------------------")


# String slices
fruit = 'banana'
# 'ban'
print(fruit[:3])

# 'ana'
print(fruit[3:])
print("------------------------------")


# Looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
print("------------------------------")


# The in operator
# True
print('a' in 'banana')
print("------------------------------")


# String comparison
if word == 'banana':
    print('All right, bananas.')
print("------------------------------")


# Other comparison operations are useful for putting words in alphabetical order:
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')
print("------------------------------")


# string methods
stuff = 'Hello world'
# <class 'str'>
print(type(stuff))

# ['capitalize', 'casefold', 'center', 'count', 'encode',
# 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable',
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
# 'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
# 'title', 'translate', 'upper', 'zfill']
print(dir(stuff))
print("------------------------------")


# convert string to uppercase
word = 'banana'
new_word = word.upper()
# 'BANANA'
print(new_word)
print("------------------------------")


# find letter 'a' in string
word = 'banana'
index = word.find('a')
# 1
print(index)
print("------------------------------")


# remove spaces from string
line = '  Here we go  '
# 'Here we go'
print(line.strip())
print("------------------------------")


# check if string starts with a substring
line = 'Have a nice day'
# True
print(line.startswith('Have'))

# False
print(line.startswith('h'))
print("------------------------------")


# Parsing strings
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
# 21
print(atpos)

sppos = data.find(' ',atpos)
# 31
print(sppos)

host = data[atpos+1:sppos]
# 'uct.ac.za'
print(host)
print("------------------------------")


# Format operator
# The format operator, % allows us to construct strings, replacing parts of the strings 
# with the data stored in variables. When applied to integers, % is the modulus operator. 
# But when the first operand is a string, % is the format operator.

# the format sequence "%d" means that the second operand should be formatted as an integer 
# (d stands for "decimal")
camels = 42
# '42'
print('%d' % camels)

camels = 42
# 'I have spotted 42 camels.'
print('I have spotted %d camels.' % camels)

# 'In 3 years I have spotted 0.1 camels.'
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))
print("------------------------------")