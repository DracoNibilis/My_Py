# lab_2_3_extra.py
# Why does this expression cause an error? How can you fix it? 
# message='I have eaten'+99+'burritos.'    print(message)  
# Author: Magdalena Malik

message = 'I have eaten ' + str(99) + ' burritos.' # cannot concatenate string to integer , use method str() on 99
print(message)
