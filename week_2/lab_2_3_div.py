# lab_2_3_div.py
# Program that reads in two numbers and divides the first one by the second and give the integer result and the remainder.
# Author: Magdalena Malik

firstNumber = int(input("Enter first number: "))
divider = int(input("Enter the number you want to divide by: "))
result = firstNumber // divider
reminder = firstNumber % divider  #10 divided by 3 is 3 with remainder 1
print("{}  divided by  {}  is  {}  with remainder  {}".format(firstNumber, divider, result, reminder))