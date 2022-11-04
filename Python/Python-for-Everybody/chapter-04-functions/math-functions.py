# Different math functions
# (see https://books.trinket.io/pfe/04-functions.html)

# Python has a math module that provides most of the familiar mathematical functions. 
# Before we can use the module, we have to import it:
import math


# The first example computes the logarithm base 10 of the signal-to-noise ratio. 
# The math module also provides a function called log that computes logarithms base e.

ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)

print(decibels)
print("------------------------------")



# The second example finds the sine of radians. 
# The name of the variable is a hint that sin and the other trigonometric functions (cos, tan, etc.) 
# take arguments in radians. To convert from degrees to radians, divide by 360 and multiply by 2π:

# The expression math.pi gets the variable pi from the math module. 
# The value of this variable is an approximation of π, accurate to about 15 digits.

degrees = 45
radians = degrees / 360.0 * 2 * math.pi

print(math.sin(radians))
print("------------------------------")

