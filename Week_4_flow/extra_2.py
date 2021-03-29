# extra_2.py
# Program that use a while loop to modify code " grade.py "
# so that it keeps prompting the user for a number until the user enters -1.
# Author: Magdalena Malik

input_mark = int(input("Enter the percentage: "))

while True:
    if input_mark >= 0 and input_mark <=40:
        print("Fail")
        input_mark = int(input("Enter the percentage: "))
    elif input_mark > 40 and input_mark <= 49:
        print("Pass")
        input_mark = int(input("Enter the percentage: "))
    elif input_mark >= 50  and input_mark < 59:
        print("Merit 2")
        input_mark = int(input("Enter the percentage: "))
    elif input_mark >= 60 and input_mark < 70:
        print("Merit 1")
        input_mark = int(input("Enter the percentage: "))
    elif input_mark > 70:
        print("Distinction")
        input_mark = int(input("Enter the percentage: "))
    else:
        print(" you enter -1, program terminated ")
        break



