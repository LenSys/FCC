# Exercise 5: Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature.
# (see https://books.trinket.io/pfe/02-variables.html)

celsiusTemperature = input("celsius temperature: ")

fahrenheitTemperature = float(celsiusTemperature) * 9 / 5 + 32

print("fahrenheit temperature", fahrenheitTemperature)