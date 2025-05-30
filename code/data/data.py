from model import course
from model import admin  
courses = [
      course.Course("1","a","1"),
      course.Course("2","b","2"),
      course.Course("3","c","3"),
      course.Course("4","d","1"),
      course.Course("4","e","2")
]
admins = [
      admin.Admin(1,"Rial Khan","rial@gmail.com","admin","super_admin"),
      admin.Admin(2,"Badhon","badhon@gmail.com","admin","super_admin"),
]
students = []
teachers = []