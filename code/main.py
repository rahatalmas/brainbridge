from controller import base_controller
from controller import teacher_controller

if __name__ == "__main__":
  print("Welcome to Admin Dashboard")

  while(True):

    print("Choose Your option: ")
    print("1. Add Teacher")
    print("2. Add Student")
    print("3. Publish Result") 
    print("4. show Admin List")
    print("5. Show Course List")
    print("6. Show Teacher List")
    print("7. exit") 

    op = int(input())
    if op == 1:
      teacher_controller.add_teacher()
    elif op == 2:
      base_controller.add_student()
    elif op == 3:
      base_controller.result()
    elif op == 4:
      base_controller.admin_list()
    elif op == 5:
      base_controller.admin_list()
    elif op == 6:
      teacher_controller.teacher_list()
    elif op == 7:
      print("Exit")
      break
