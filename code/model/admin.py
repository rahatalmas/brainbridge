from model import person

class Admin(person.Person):
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