a = '''
  # domain: education
  # title: Online course manage system... 
  
  -> admin list
  -> teacher list
  -> student list 
  -> course list

  -> course enrolled list by students...
  -> student list for a course 
  -> course instructors list
'''
print(a)
# Total number or entity = 4
# how many model do i need ? 
# 4 models 

# person:
  #id
  #name
  #email
  #role

# entity 1 : (Admin <-person):
  # super()
  # type: "editor","super admin"

# entity 2 : (Teacher <-person):
  #super()
  # department
  # designation
  # course list

#entity 3: (student <- person):
  # super()
  # department
  # section
  # couse list
  # cgpa
  # batch

#entity 4: (course):
  # code 
  # name 
  # credit