# Exercise 7: Rewrite the grade program from the previous chapter using a function called 
# computegrade that takes a score as its parameter and returns a grade as a string.

# (see https://books.trinket.io/pfe/04-functions.html)

# Score   Grade
# > 0.9     A
# > 0.8     B
# > 0.7     C
# > 0.6     D
# <= 0.6    F

# ------------------------------
# Program Execution:
# ------------------------------
# Enter score: 0.95
# A

# Enter score: perfect
# Bad score

# Enter score: 10.0
# Bad score

# Enter score: 0.75
# C

# Enter score: 0.5
# F
# ------------------------------


def computegrade(score):
    # check for valid score
    if score > 1.0 or score < 0.0:
        grade = "Bad score"
    elif score > 0.9 :
        grade = "A"
    elif score > 0.8 :
        grade = "B"
    elif score > 0.7 :
        grade = "C"
    elif score > 0.6 :
        grade = "D"
    elif score <= 0.6 :
        grade = "F"

    return grade

try:
    score = float(input("Enter score: "))

    grade = computegrade(score)
    print(grade)

except:
    print("Bad score")