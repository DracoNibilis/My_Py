# lab_3_3_normalise.py
# Program that reads in a string, strips it, converts it to lower case.
# Also program outputs the length of the input and output strings.
# Author: Magdalena Malik

input_string = input("Please enter a string: ")
norm_string = input_string.strip()
norm_string = norm_string.lower()
len_i_str = len(input_string)
len_n_str = len(norm_string)
print("\" {} \" normalised is: {}".format(input_string, norm_string ))
print("We reduced the input string from {} to {} characters".format(len_i_str, len_n_str))