# pylint: disable=print-statement

s = "Score: "
g = "Your grade is "
grade = ""

def getLetterGrade():
    for val in range(0,10):
        import random
        import math
        score = math.trunc(random.random() * ((100 - 60) +1) + 60)
        if score >= 90: grade = "A"
        elif score >= 80 and score < 90: grade = "B"
        elif score >= 70 and score < 80: grade = "C"
        elif score >= 60 and score < 70: grade = "D"
        print s + str(score) + "; " + g + grade
    print "End of the program. Bye!"
getLetterGrade()