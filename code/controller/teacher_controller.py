from model import teacher
from data import data

'''
  1. show all teacher
  2. show teacher from specific department 
  3. show teacher by id

'''

def all_teacher():
    teachers = data.teachers


def teacher_by_dept(dept):
    teachers = data.teachers
    for teacher in teachers:
      if teacher.department == dept:
         print(teacher)

#display teacher
def teacher_list(dept=None):
  teachers = data.teachers
  if len(teachers) == 0:
     print("No teacher exist")
     return 
  if dept!= None:
    for teacher in teachers:
      if teacher.department == dept:
         print(teacher)
  else:
    for teacher in teachers:
        print(teacher)
#      print("No teacher exist")
#      return
#   while(True):
#     print("1. all list")
#     print("2. list by department")
#     print("3. by teacher id")

#     op = input("Choose input ")
#     if op == 1:
#       print(teacher) 
#     elif op == 2:
#         dept = input("Enter Department name: ")
#         teacher_by_dept(dept)

def teacher_by_id(teacher_id):
   pass

# add teacher
def add_teacher():
    print("Add teacher menu: ")
    id = input("Enter Id: ")
    name = input("Enter Teacher Name: ")
    email = input("Enter Email: ")
    role = input("Role: ")
    department = input("Department: ")
    designation = input("Designation: ")
    course_list = []
    new_teacher = teacher.Teacher(id,name,email,role,department,designation,course_list)
    data.teachers.append(new_teacher)
    print("Return to Home")


