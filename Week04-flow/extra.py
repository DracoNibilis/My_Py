# extra.py
# Program that modifies code " grade.py" by rounding
#  percentages ie: 69.5 gets rounded to 70.
# Author: Magdalena Malik

import math

input_mark = float(input("Enter the percentage: "))
input_mark = math.ceil(input_mark)
if input_mark <= 40:
    print("Fail")
elif input_mark > 40 and input_mark <= 49:
    print("Pass")
elif input_mark >= 50  and input_mark < 59:
    print("Merit 2")
elif input_mark >= 60 and input_mark < 70:
    print("Merit 1")
else:
    print("Distinction")

