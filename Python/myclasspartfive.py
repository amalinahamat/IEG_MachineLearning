#is-a

class Student: 

    def __int_(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""

# -Alumni extend Student Class
class Alumni(Student):

    def __init__(self,firstname,lastname,alumninumber):
        # calling the __init__ method statically
        # you can use the keyword super
        # Student.__init__(self,firstname,lastname)
        # To create the parent object inside the child object
        # you can use super class
        # which will return the object ofparent class
        super().__init__(firstname,lastname)
        self.alumninumber = alumninumber
        
        

    def __str__(self):
        return f"First Name:{self.firstname} \
            \nLast Name: {self.lastname} \
            \nIC Number:{self.icnumber} \
            \nAlumni Number: {self.alumninumber}"
    

# we have create an object of Alumni class
alumni = Alumni("Parker", "Peter", 97489)
# alumni = Alumni
print(alumni)

