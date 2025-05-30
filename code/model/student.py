from model import person

class Student(person.Person):
    def __init__(self,id,name,email,role,department,section,course_list,cgpa,batch):
      super().__init__(id,name,email,role)
      self.department = department
      self.section = section 
      self.course_list = course_list
      self.cgpa = cgpa
      self.batch = batch