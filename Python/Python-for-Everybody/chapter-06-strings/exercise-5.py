# Exercise 5: Take the following Python code that stores a string:`
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon character 
# and then use the float function to convert the extracted string into a floating point number.
# (see https://books.trinket.io/pfe/06-strings.html)

print("~~ Chapter 6 - Exercise 5 ~~")

str = 'X-DSPAM-Confidence:0.8475'
colonPos = str.find(":")
# print(colonPos)
# print(str[colonPos + 1:])

number = float(str[colonPos + 1:])
print(number)