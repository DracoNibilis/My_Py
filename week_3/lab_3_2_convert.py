# lab_3_2_convert.py
# Program that takes in a float amount of dollars, and returns that absolute amount in cent.
# Author: Magdalena Malik

dollar_input = float(input("Please enter an amount: "))
cent_output = abs(dollar_input) * 100
print("That amount in cent is: {}".format(int(cent_output)))