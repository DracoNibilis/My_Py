# grade.py
# Program that reads in a students percentage mark 
# and prints out corresponding the grade.
# Author: Magdalena Malik

input_mark = int(input("Enter the percentage: "))

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