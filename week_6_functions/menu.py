# menu.py
# Program that prints out a menu of commands we can perform,
#  ie add, view and quit. The function should return what the user chose.
# Author: Magdalena Malik

def user_menu():
    user_input= input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit \nType one letter (a/v/q): ")
    return user_input

choice = user_menu()
print("You choose: ",choice)