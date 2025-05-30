# Online course manage system... 

class Person:
    def __init__(self, id, name, email, role):
        self.id = id
        self.name = name
        self.email = email
        self.role = role
        



class Admin(Person):
    def __init__(self, id, name, email, role, type):
        super().__init__(id, name, email, role)
        self.type = type

    def __str__(self):
        return f'''
        Id: ${self.id} \n
        Name: {self.name}\n
        Email: {self.email}\n 
        Role: {self.role}\n
        Type: {self.type}\n
        '''
    

    def new_teacher_registration(self):
        id = input()
        name = input()
        email = input()
        role = input()
        department = input()
        designation = input()
        course_list = []
        new_teacher = Teacher(id, name, email, role, department, designation, course_list)
        teacher.append(new_teacher)

    def new_student_registration(self):
        pass




class Teacher(Person):
    def __init__(self, id, name, email, role, department, designation, courselist):
        super().__init__(id, name, email, role)
        self.department = department
        self.designation = designation
        self.courselist = courselist


    def __str__(self):
        return f'''
        Id: ${self.id} \n 
        Name: {self.name}\n
        Email: {self.email}\n 
        Role: {self.role}\n
        Type: {self.type}\n
        Dept: {self.department}\n  
        Designation: {self.designation}\n
        '''

       




class Student(Person):
    def __init__(self, id, name, email, role, department, section, courselist, cgpa, batch):
        super().__init__(id, name, email, role)
        self.department = department
        self.section = section
        self.courselist = courselist
        self.cgpa = cgpa
        self.batch = batch



class Course():
    def __init__(self, course_name, course_code, course_credit):
        self.course_name = course_name
        self.course_code = course_code
        self.course_credit = course_credit
        


course = [
    Course("1", "a", "1"),
    Course("2", "b", "2"),
    Course("3", "c", "3"),
    Course("4", "d", "4"),
    Course("5", "e", "5"),
    Course("6", "f", "6"),
]



admin_type = [
    Admin(1, "mahin", "mahin@gmail.com", "admin","editor"),
    Admin(2, "rafid", "rafid@gmail.com", "admin", "editor")
]

student = []
teacher = []

def teacher_assing():
    mahin = admin_type[0]
    while(1):
        mahin.new_teacher_registration()

def student_assing():
    rafid =admin_type[1]
    rafid.new_student_registration()



if __name__ == "__main__":
        print("Choose your option: ")
        print("1. Teacher Assign \t")
        print("2. Student Assign \n")

