class Course:
   def __init__(self,course_code,course_name,course_credit):
      self.course_code = course_code
      self.course_name = course_name
      self.course_credit = course_credit

   # def __str__(self):
   #    return f''

   def display(self):
      print("Course  Code: ",self.course_code)
      print("Course Name: ",self.course_name)
      print("Course Credit: ",self.course_credit)