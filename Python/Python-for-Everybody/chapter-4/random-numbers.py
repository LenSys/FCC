# This program produces the following list of 10 random numbers between 0.0 and up to but not including 1.0.
# (see https://books.trinket.io/pfe/04-functions.html)

import random

for i in range(10):
    x = random.random()
    print(x)


# The random function is only one of many functions that handle random numbers. 
# The function randint takes the parameters low and high, and returns an integer 
# between low and high (including both).
print(random.randint(5, 10))


# To choose an element from a sequence at random, you can use choice:
t = [1, 2, 3]
print(random.choice(t))
