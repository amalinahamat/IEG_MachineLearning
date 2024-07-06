'''
# videos 1 intro to oop (object oriented programming)

object -> intsance of a class

Class -> blue print

class
1. characteristics / data member / state
2. functionalities / member function / behaviour

'''
'''
class Person: # start class name with capital letter
    # __init__ is also called as a constructor
    # whenever we created an object, the first method that we called is __init__ method
    # it will initialized all the values that will pass
    def __init__(self,age,gender,height,weight): # whatever followed by self, will be considered as parameter
        self.age = age # self.age is a property of the person and  = age is an argument that is passed
        self.gender = gender
        self.height = height
        self.weight = weight

    def display(self):
        print("Person Details: ")
        print("Age =", self.age)
        print("Gender =", self.gender)
        print("Height =", self.height)
        print("Weight =", self.weight)

    def __str__(self): # will return in the form of string
        return "Person Details:\n" + str(self.age) + "," + self.gender + "," + str(self.height) + "," + str(self.weight)


person1 = Person(25,"M",178,82) # this is how we created an object
person2 = Person(23,"F",155,55)
# how to access all this value
print(person1.age)
print(person2.gender)
print()

person1.display()
print()
person2.display()

print()
print(person1)
print()
print(person2)
'''
# videos 2 python classes and object access specifiers
'''
assess specifiers:
1. public => variable doesnt have any underscore _
             can be accessed by any object
2. protected => variable have 1 underscore _  eg.  self._age
             should be accessed by the inherited(parent-child) classses
3. private  => variable have 2 underscore __  eg.  self.__age
             should not be accessed anywhere except in the same class

'''
'''
class Person:
    def __init__(self,age,height,gender):
        self.age = age          # public
        self._height = height   # protected
        self.__gender = gender  # private

p = Person(25,178,"M")

print(p.age)
print(p._height)
#print(p.__gender) # will be error because cannot print private
                  # AttributeError: 'Person' object has no attribute '__gender'
print()
'''
''''
# video 3 python classes and object getters and setters

getter setter

getter =>  


'''
'''
class Person:
    def __init__(self,age):
        self.age = age          # public

    def get_age(self): # get_age => snake case
        return self.age
    
    def set_age(self,age):
        self.age = age

    def __str__ (self):
        return "age = " + str(self.age)
    
p = Person(25)

print(p)
print(p.get_age())
p.set_age(27)
# print(p.set_age()) set_age does not return anything so it will print None
print(p)
'''

# or
# using property()  => property method

class Person:
    def __init__(self,age):
        self._age = age          # public

    def get_age(self): # get_age => snake case
        print("Inside age getter\n")
        return self._age
    
    def set_age(self,age):
        print("Inside age setter\n")
        self._age = age

    def del_age(self):
        del self._age

    def __str__ (self):
        return "age = " + str(self._age)
    
    age = property(get_age,set_age,del_age)

p = Person(25)
print(p)
p.age = 27
print(p.age)
print(p)


# or
# using @property

class Person:
    def __init__(self,age):
        self._age = age          # public

    @property  #automatically become getter
    def age(self):
        print("Inside getter")
        return self._age
    
    @age.setter #automatically become setter
    def age(self,age):
        print("Inside setter")
        self._age = age

    def __str__ (self):
        return "age = " + str(self._age)


p = Person(25)
print(p)
p.age = 27
print(p.age)
print(p)
    
'''
# video 4 python relationship one to many implementation

one to many  -> book - pages

'''

class Page:
    def __init__(self,page_number, content):
        self.page_number = page_number
        self.content = content

    def __str__ (self):
        return str(self.page_number) + "-" + self.content + "\n"

class Book:
    def __init__(self,name,author,pages = []):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__ (self):
        s = self.name + ":" + self.author + "\n"
        for i in self.pages:
            s += str(i)
        return s
    
pages = []
pages.append(Page(1,"Hi Hello"))
pages.append(Page(2,"Welcome"))
pages.append(Page(3,"Python OOPS"))
pages.append(Page(4,"Life is beautiful"))

book = Book("Harry Potter","JK Rowling", pages)

print()
print(book)

'''
# video 5 python relationship one to one implementation/ learning resource

one to one => student - id card

'''

from lStudent import Student
from lIDCard import IDCard

s = Student("jk","IT")
i = IDCard("123",True)

# assign id card object to the student
s.id_card = i
print(s)

# or

i = IDCard("123",True)
s = Student("jk","IT",i)
# assign id card object to the student
print(s)

'''
# video 6 python relationship introduction

relationship between classes / called as association

1. has a
student has an id car
bottle has a car

2. has many
library has many books
faculty has many departemnt
book has many pages
bas has many seat

1. aggregation - weakly associated. if one classes deleted, the other class, does not affected
- mobile phone and cover

2. composition - strongly associated. if one class deleted, the other class affected as it cannot run wothout the deleted class

one to one -> student idcard
one to many => book-page
many to many => teacher - student

'''
'''
# video 7 relationship many to many implementations
many to many => teacher - student

T1
T2
T3
T4

S1
S2
S3
S4
S5

MAPPING 
T1 - S1
T1 - S2
T2 - S1
T2 - S3
T2 - S5
T3 - S2
T3 - S5
T4 - S4

3 class
1- teacher
2- student
3- mapping/bridge


'''

class Teacher:
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept

    def __str__(self):
        return self.name + " : " + self.dept
    
class Student:
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno

    def __str__(self):
        return self.name + " : " + str(self.rno)
    
class TeacherStudent:
    def __init__(self,teacher,student): # teacher,stuent object
        self.teacher = teacher
        self.student = student
    
    def __str__(self):
        return str(self.teacher) + " - " + str(self.student)
    
teacher = []
student = []
tsl = []

teacher.append(Teacher("T1","Math"))
teacher.append(Teacher("T2","Science"))
teacher.append(Teacher("T3","Eng"))
teacher.append(Teacher("T4","Art"))

student.append(Student("S1",123))
student.append(Student("S2",456))
student.append(Student("S3",321))
student.append(Student("S4",654))
student.append(Student("S5",678))

tsl.append(TeacherStudent(teacher[0],student[0]))
tsl.append(TeacherStudent(teacher[1],student[2]))
tsl.append(TeacherStudent(teacher[1],student[1]))
tsl.append(TeacherStudent(teacher[3],student[3]))
tsl.append(TeacherStudent(teacher[2],student[4]))

for i in tsl:
    print(i)


'''
# video 8 oop


'''
my_student = {
    "name" : "Rolf Smith",
    "grades" : [7, 88, 90, 99],
    "average" : ""# something that can return data and have a function . use object
}

def average_grade(student):
    return sum(student["grades"]) / len(student["grades"])

print(average_grade(my_student))


"""
object -> something that can store data
self is a black object that we called before other. after that is an argumentation
"""
class Student:
    def __init__(self, new_name , new_grade):
        self.name = new_name
        self.grade = new_grade

    def average(self):
        return sum(self.grade) / len(self.grade)
    
student_one = Student('Roth Smith',[70,88,90,99])
student_two = Student('Amal',[70,100,90,100])

print(student_one.name)
print(student_two.name)

print(student_one.average())
print(student_two.average())


'''

# video 9 oop inheritance and polymorphism
'''

'''
class fruits:
    def __init__(self,price):
        self.price = price
obj = fruits(50)

obj.quantity = 10
obj.bags = 2
print(obj.quantity + len(obj.__dict__))

# Explanation: In the above code, obj.quantity has been 
# initialised to 10. There are a total of three items 
# in the dictionary, price, quantity and bags. Hence, len(obj.__dict__) is 3.
'''
'''
class change:
    def __init__(self,x,y,z):
        self.a = x + y + z
    
x = change(1,2,3)
y = getattr(x,"a")
setattr(x,"a", y + 1)
print(x.a)
'''
'''
This defines a class change with an __init__ method that takes three parameters
x, y, and z. The __init__ method initializes an instance variable a as the sum of x, y, and z.

Here, an instance x of the change class is created with x=1, y=2, and z=3. 
The __init__ method is called, setting x.a to the sum of these values, which is 1 + 2 + 3 = 6.

The getattr function retrieves the value of the attribute a from the instance x. So, y is assigned the 
value 6 (since x.a is 6).

The setattr function sets the value of the attribute a of the instance x to y + 1. Since y is 6, this sets x.a to 7.
'''
'''
class test:
    def __init__(self):
        self.variable = "Old"
        self.Change(self.variable)
    
    def Change(self, var):
        var = "New"
    
obj = test()
print(obj.variable)

The local variable var is set to "New", but this does not affect self.variable. 
The var parameter is a local variable within the Change method, and changing it 
does not change the instance variable self.variable.

'''
'''
class test:
    def __init__(self,a):
        self.a = a

    def display(self):
        print(self.a)

#obj = test(134)
obj = test() #  missing an argument 
obj.display()

'''
'''
class test:
    def __init__(self,a = "Hello World"):
        self.a = a
    
    def display(self):
        print(self.a)
    
obj = test("Hello")
obj.display()
'''
'''
class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
    def get(self):
        return self.__b
obj = Demo()
print(obj.get())
'''
'''
In the code you provided, the Demo class has a public instance variable a and 
a private instance variable __b. The double underscore prefix (__) makes __b 
a private variable, meaning it is not directly accessible from outside the class. 
However, you can access it via a method within the class.
'''
'''
class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
    def get(self):
        return self.__b
obj = Demo()
obj.a=45
print(obj.a)

'''
# iDesign
# 1

class Person:
	#Fill your code
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def get_details(self):	
		return f"Person Details\n{self.name}\n{self.age}"

#from Person import Person

#Fill your code

name = input("Enter name\n")
age = input("Enter age\n")

p = Person(name,age)
print(p.get_details())

# 2

class Person:
    def __init__(self,name, age):
        self.__name = name
        self.__age = age
		
    @classmethod
    def from_string(cls, person_str):# Assuming person_str format is "name,age"
        name, age = person_str.split(",")
        return cls(name,int(age))
    
    def get(self):
        return self.__name,self.__age
    
    def __str__(self):
        #return f"{self.__name} is {self.__age} years old"
        return self.__name  + " is " + str(self.__age) + " years old"
	

#from Person import Person

print("Creating object using __init__ method")
person_name = input("Enter name\n")
person_age = input("Enter age\n")
person1 = Person(person_name, person_age)
print("Person Details")
print(person1)
print("\n")

print("Creating object using class method")
person_str = input("Enter name and age in comma separated format\n")
person2 = Person.from_string(person_str)
print("Person Details")
print(person2)





	
	