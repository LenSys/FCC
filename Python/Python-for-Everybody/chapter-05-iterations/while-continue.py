# Iterations (while) with continue
# (see https://books.trinket.io/pfe/05-iterations.html)

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# Code: http://www.py4e.com/code3/copytildone2.py


# Here is a sample run of this new program with continue added.
# > hello there
# hello there
# > # don't print this
# > print this!
# print this!
# > done
# Done!