# full_menu_student.py
# Program that allows a user to create new students and to view students.
# Author: Magdalena Malik


def user_menu():
    user_input= input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit \nType one letter (a/v/q): ")
    return user_input

# function do_add() when option "a" is choosen
def do_add(students):
    current_student = {}
    current_student["name"]=input("enter name: ")
    current_student["modules"]= read_modules()
    students.append(current_student)
    
def read_modules():
    modules = []
    module_name = input("Enter the first module name (blank to quit): ").strip()
    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("Enter grade: "))
        modules.append(module)
        module_name = input("Enter next module (blank to quit): ".strip())
    return modules

def display_module(modules):
    for module in modules:
        print("\t{}   \t{}".format(module["name"], module["grade"]))

    
def do_view(students):
    for current_student in students:
        print(current_student["name"])
        display_module(current_student["modules"])
    

# main program 
students = []
choice = user_menu()

while choice != "q":
    if choice == "a":
        do_add(students)
    
    elif choice == "v":
        do_view(students)
    
    choice = user_menu()

   
