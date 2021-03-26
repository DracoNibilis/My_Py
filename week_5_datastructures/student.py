# student.py
# Program that stores a student name and a list of her courses and grades in a dict,
# the program should then print out her data.
# Author: Magdalena Malik

student_data = {"Student:": "Mary",
                "Courses":  [
                    {"Course name": "Programming",
                    "Course grade": 45},
                    {"Course name": "History",
                     "Course grade": 99}
                            ]
                }


print("Student:  {}".format(student_data["Student:"]))
for item in student_data["Courses"]:
    print(item["Course name"],"\t", item["Course grade"], sep=" ")


