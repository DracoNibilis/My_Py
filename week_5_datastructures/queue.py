# queue.py
# Program  that puts 10 random numbers into a queue(list),
# the program should then output all the values in the queue, 
# then take the numbers from the queue one at a time, 
# print it and the current numbers still in the queue.
# Author: Magdalena Malik

import random

list_of_numbers = []
for i in range(10):
    list_of_numbers.append(random.randint(1,100))

print("gueue is: ", list_of_numbers)

for i in range(len(list_of_numbers)-1):
    print("current number is {} and the queue is {}".format(list_of_numbers.pop(0), list_of_numbers))

print("the queue is empty now")