# isEven.py
# Program that asks the user to enter in a number, 
# and ther it will tell the user if the number is even or odd.
# Author: Magdalena Malik

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("{} is an even number.".format(number))
else:
    print("{} is an odd number.".format(number))