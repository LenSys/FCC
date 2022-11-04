# Calculate celsius temperature from fahrenheit temperature
# (see https://books.trinket.io/pfe/03-conditional.html)

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')

# Code: http://www.py4e.com/code3/fahren2.py