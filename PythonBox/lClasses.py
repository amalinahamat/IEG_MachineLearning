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
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
class WorkingStudent:
    def __init__(self,name,school,salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary

    def average(self):
        return sum(self.marks) / len(self.marks)
    
rolf = WorkingStudent("Rolf", "MIT", 15.50)
print(rolf.salary)




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

# 5
'''

from User import User

print("Enter the details of User 1")
name_1 = input("Name :\n")
username_1 = input("Username :\n")
pwd_1 = input("Password :\n")
mobile_number_1 = int(input("Mobile Number :\n"))

print("Enter the details of User 2")
name_2 = input("Name :\n")
username_2 = input("Username :\n")
pwd_2 = input("Password :\n")
mobile_number_2 = int(input("Mobile Number :\n"))

#Fill your code here

user1 = User(name_1, username_1, pwd_1, mobile_number_1)
user2 = User(name_2, username_2, pwd_2, mobile_number_2)

if user1 == user2:
    print(f"User 1 and User 2 are equal ")
else:
    print(f"User 1 and User 2 are not equal")

class User:
    def __init__(self,name,username,password,mobile_number):
        self.name = name
        self.username = username
        self.password = password
        self.mobile_number = mobile_number

    def __eq__(self,obj):
	#Fill your code here
        return self.mobile_number == obj.mobile_number
'''

# 6

import datetime,time
from Hall import Hall

d1=input("Enter Start time\n")
d2=input("Enter the End time\n")
cost=int(input("Enter the cost per day\n"))
#Fill your code here

d1 = datetime.datetime.strptime(d1,"%b %d %Y")
d2 =  datetime.datetime.strptime(d2,"%b %d %Y")
hall = Hall(d1,d2,cost)
print(hall)


class Hall:
    def __init__(self,start_date,end_date,cost_per_day):
        #Fill your code here
        self.start_date = start_date
        self.end_date = end_date
        self.cost_per_day = cost_per_day
        
    def noDays(self):
        #Fill your code here
        return (self.end_date - self.start_date).days

    def cost(self):
	#Fill your code here
        total_days = self.noDays()
        return total_days * self.cost_per_day
    
    def __str__(self):
        total_days = self.noDays()
        total_cost = self.cost()
        return f"Total number of days {total_days}\nTotal cost {total_cost}"


import datetime
from Hall import Hall

d1_str = input("Enter Start time (e.g., Jul 1 2014):\n")
d2_str = input("Enter the End time (e.g., Jul 10 2014):\n")
cost = int(input("Enter the cost per day:\n"))

d1 = datetime.datetime.strptime(d1_str, "%b %d %Y")
d2 = datetime.datetime.strptime(d2_str, "%b %d %Y")

hall = Hall(d1, d2, cost)
no_days = hall.no_days()  # Call no_days() method from Main class
print(f"Number of days: {no_days}")  # Print number of days

from datetime import timedelta

class Hall:
    def __init__(self, start_date, end_date, cost_per_day):
        self.start_date = start_date
        self.end_date = end_date
        self.cost_per_day = cost_per_day
        
    def no_days(self):
        return (self.end_date - self.start_date).days  # Calculate number of days
    
    def cost(self):
        total_days = self.no_days()  # Call no_days() to get the number of days
        return total_days * self.cost_per_day  # Calculate and return total cost

    def __str__(self):
        total_days = self.no_days()  # Call no_days() to get the number of days
        total_cost = self.cost()  # Call cost() to get the total cost
        return f"Total number of days: {total_days}\nTotal cost: {total_cost}"


# 7
from Student import Student

u_id = int(input("Enter the student id\n"))
username = input("Enter the student's username\n")
password = input("Enter the password\n")
name = input("Enter the name of the student\n")
address = input("Enter the address\n")
city = input("Enter the city\n")
pincode = int(input("Enter the pincode\n"))
contact_number = int(input("Enter the contact number\n"))
email = input("Enter the email id\n")

#Fill your code here

student = Student(u_id,username,password,name,address,city,pincode,contact_number,email)
print(student)


class Student:
    def __init__(self,__id,__username,__password,__name,__address,__city,__pincode,__contact_number,__email):
        #Fill your code here
        self.__id = __id
        self.__username = __username
        self.__password = __password
        self.__name  = __name
        self.__address = __address
        self.__city = __city
        self.__pincode = __pincode
        self.__contact_number = __contact_number
        self.__email = __email
    def __str__(self):
        # fill your code
        return f"Id : {self.__id}\nUser Name : {self.__username}\nPassword : {self.__password}\nName : {self.__name}\nAddress : {self.__address}\ncity : {self.__city}\nPincode : {self.__pincode}\nContact Number : {self.__contact_number}\nemail : {self.__email}"
    

# 8

from Employee import Employee
from Developer import Developer
from Manager import Manager
from Utility import Utility


manager_list = []
manager_list.append(Manager("Arun",80000))
manager_list.append(Manager("Babu",100000))
manager_list.append(Manager("Chandru",60000))
manager_list.append(Manager("Deva",60000))

input_obj_list = []
choice = "yes"
while choice=="yes" :
	print("Menu\n1)Employee\n2)Developer\n")
	choice1 = input("Enter choice\n")
	if choice1 == "1" :
		input_str = input("Enter Employee details in comma separated format\n")
		name, pay = input_str.split(",")
		employee = Employee(name, pay)
		input_obj_list.append(employee)
		mgr_name = input("Enter manager name\n")
		for manager in manager_list :
			if manager.name == mgr_name :
				manager.add_employee(employee)
				
	else :
		input_str = input("Enter Developer details in comma separated format\n")
		name, pay, prog_lang = input_str.split(",")
		developer = Developer(name, pay, prog_lang)
		input_obj_list.append(developer)
		mgr_name = input("Enter manager name\n")
		for manager in manager_list :
			if manager.name == mgr_name :
				manager.add_employee(developer)
	choice = input("Do you want to continue? Type yes/no\n")

print("\nManager and Employee Allocation List")	
Utility.print_employees_under_each_manager(manager_list)
print("\n")


from Employee import Employee

class Developer(Employee):
    
    def __init__(self, name, pay, prog_lang) :
        #Fill your code
        super().__init__(name, pay)
        self._prog_lang = prog_lang
        
    def __str__(self) :
        #Fill your code
        return  f"Name: {self._name}, Pay: {self,_pay}, Email: {self._email}, Programming Language: {self._prog_lang}"
        
    
from Employee import Employee
class Manager(Employee):

    def __init__(self, name, pay, employees=None):
        #Fill your code
        super().__init__(name, pay)
        if employees is None:
            self._employees = []
        else:
            self._employees = employees

    def add_employee(self, emp):
        #Fill your code
        if emp not in self._employees:
            self._employees.append(emp)

    def remove_employee(self, emp):
        #Fill your code
        if emp in self._employees:
            self._employees.remove(emp)

    def __str__(self):
        emp_names = ", ".join([emp.name for emp in self._employees])
        return f"Name: {self._name}, Pay: {self._pay}, Email: {self._email}, Employees: [{emp_names}]"

from Employee import Employee
from Developer import Developer
from Manager import Manager

class Utility:
    @staticmethod
    def print_employees_under_each_manager(manager_list):
        for manager in manager_list:
            if isinstance(manager, Manager):
                emp_names = [emp.name for emp in manager._employees]
                print(f"\nManager Name :{manager.name}")
                if emp_names:
                    print(f"Employee List :\n{' '.join(emp_names)}")
                else:
                    print("Employee List :\nNone")


			

class Employee:

    def __init__(self, name, pay,) :
        #Fill your code
        self._name = name
        self._pay  = pay
        self._email = f"{name}@gmail.com"
        
    @property
    def name(self) :
    	#Fill your code
        return self._name
	
    def __str__(self) :
        #Fill your code
        return f"Name: {self._name}, Pay: {self._pay}, Email: {self._email}"
        
    
    
    
        
        
		

    
        
   
		
		
        
     



        