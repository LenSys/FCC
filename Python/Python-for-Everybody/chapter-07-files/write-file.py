# Writing files
# (see https://books.trinket.io/pfe/07-files.html#searching-through-a-file)

line1 = "This here's the wattle,\n"
line2 = 'the emblem of our land.\n'

fout = open('output.txt', 'w')
print(fout)

fout.write(line1)
fout.write(line2)
fout.close()