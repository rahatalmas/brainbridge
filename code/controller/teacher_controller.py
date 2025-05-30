from model import teacher
from data import data

'''
  1. show all teacher
  2. show teacher from specific department 
  3. show teacher by id

'''

def all_teacher():
    teachers = data.teachers
    for teacher in teachers:
      print(teacher)

def teacher_by_dept(dept):
    teachers = data.teachers
    for teacher in teachers:
      if teacher.department == dept:
         print(teacher)

#display teacher
def teacher_list():
  teachers = data.teachers
  if len(teachers) == 0:
     print("No teacher exist")
     return 
  print("choose option: ")
  print("1. all ")
  print("2. by dept")
  #type casting was missing .... (fixed...)
  opt = int(input())
  if opt == 1:
    all_teacher()
  if opt == 2:
    dept = input()
    teacher_by_dept(dept)
  
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


