# menu_2.py
# Program hat keeps displaying the menu until the user picks q,
# if the user chooses a then call a function called doAdd(), 
# if the user chooses v then call a function called doView().
# Author:Magdalena Malik

student_data = {"Student:": "Mary",
                "Courses":  [
                    {"Course name": "Programming",
                    "Course grade": 45},
                    {"Course name": "History",
                     "Course grade": 99}
                            ]
                }


students = []

def user_menu():
    user_input= input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit \nType one letter (a/v/q): ")
    return user_input

choice = user_menu()
print("You choose: ",choice)
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

# function do_add() when option "a" is choosen
def do_add(students):
    current_student = {}
    current_student["name"]=input("enter name: ")
    current_student["modules"]= read_modules()
    students.append(current_student)

    #probably smth has to going on here....
    print("in adding")
    return None

#function do_View() when option "v" is choosen
def do_view():
    # something here....
    print("do viewing")
    return None
while choice != "q":
    if choice == "a":
        do_add()
    
    elif choice == "v":
        do_view()
    
    choice = user_menu()

   
print("quit program")
    
do_add(students)
print(students)

     