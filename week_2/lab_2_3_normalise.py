# lab_2_3_normalise.py
# Program that reads in a string and strips any leading 
# or trailing spaces, the program should also convert the string to lower case. 
# The program should also output the length of the input and output strings.
# Author: Magdalena Malik

someString = input("Please enter a string: ")
newString = someString.strip().lower()

print("That string normilise is: {}".format(newString))
print("We reduced the input string from  {}  to  {}  characters.".format(len(someString), len(newString)))