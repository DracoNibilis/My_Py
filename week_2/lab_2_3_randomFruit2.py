# lab_2_3_randomFruit2.py
# Program that prints out a random fruit.
#Author: Magdalena Malik

import random
tupleOfFruits = ("Banana", "Apple","Lemon", "Strawberries", "Grapes", "Plum")
randomNumber = random.randint(0,len(tupleOfFruits)-1)
listIndex = tupleOfFruits[randomNumber]
print("A random fruit is :  {}".format(listIndex))