# lab_2_3_randomFruit.py
# Program that prints out a random fruit.
#Author: Magdalena Malik

import random
listOfFruits = ["Banana", "Apple","Lemon", "Strawberries", "Grapes", "Plum"]
randomNumber = random.randint(0,len(listOfFruits)-1)
listIndex = listOfFruits[randomNumber]
print("A random fruit is :  {}".format(listIndex))