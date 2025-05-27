class Person:
   def __init__(self,id,name,email,role):
      self.id = id 
      self.name = name
      self.email = email 
      self.role = role

class Admin(Person):
    def __init__(self,id,name,email,role,type):
        super().__init__(id,name,email,role)
        self.type = type 
    def __str__(self):
        return f'''Id: ${self.id} \n 
        Name: {self.name}\n
        Email: {self.email}\n
        Role: {self.role}\n
        Type: {self.type}\n
        '''  
    
    def new_student_registration(self):
      pass
    def new_teacher_registration(self):
        id = input()
        name = input()
        email = input()
        role = input()
        department = input()
        designation = input()
        course_list = []
        new_teacher = Teacher(id,name,email,role,department,designation,course_list)
        teacher.append(new_teacher)

class Teacher(Person):
    def __init__(self,id,name,email,role,department,designation,course_list):
      super().__init__(id,name,email,role)
      self.department = department
      self.designation = designation
      self.course_list = course_list

    def __str__(self):
      return f'''Id:${self.id}\n
      Name: {self.name}\n
      Email: {self.email}\n
      Role: {self.role}\n
      '''
    
    def result_assign():
       pass

class Student(Person):  
    def __init__(self,id,name,email,role,department,section,course_list,cgpa,batch):
      super().__init__(id,name,email,role)
      self.department = department
      self.section = section 
      self.course_list = course_list
      self.cgpa = cgpa
      self.batch = batch

class Course:
   def __init__(self,course_code,course_name,course_credit):
      self.course_code = course_code
      self.course_name = course_name
      self.course_credit = course_credit

courses = [
      Course("1","a","1"),
      Course("2","b","2"),
      Course("3","c","3"),
      Course("4","d","1"),
      Course("4","e","2")
]
admin = [
    Admin(1,"Rial Khan","rial@gmail.com","admin","super_admin"),
    Admin(2,"Badhon","badhon@gmail.com","admin","super_admin"),
]

student = []
teacher = []

def teacher_assignment():
    rial = admin[0]
    while(1):
       rial.new_teacher_registration()

def student_assignment():
    badhon = admin[1]

if __name__ == "__main__":
   "what is my current requirement ... "
   print("choose your option: ")
   print("1. teacher assign \t")
   print("2. student assign \n")
   opt = int(input())
   if opt == 1:
      print("Teacher Assign: ")
      teacher_assignment()
      print(teacher)
   elif opt == 2:
      print("student Assign: ")
   else:
      print("...Bye...")