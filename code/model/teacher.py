from model import person

class Teacher(person.Person):
    def __init__(self,id,name,email,role,department,designation,course_list):
      super().__init__(id,name,email,role)
      self.department = department
      self.designation = designation
      self.course_list = course_list

    def __str__(self):
      return f'''Id:{self.id}
      Name: {self.name}
      Email: {self.email}
      Role: {self.role}
      '''
    
    def result_assign():
       pass
