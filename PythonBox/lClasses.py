'''
# videos 1 intro to oop (object oriented programming)

object -> intsance of a class

Class -> blue print

class
1. characteristics / data member / state
2. functionalities / member function / behaviour

'''
class Person: # start class name with capital letter
    # __init__ is also called as constructor
    # whenever we created an object, the first method that we called is __init__ method
    # it will initialized all the values that will pass
    def __init__(self,age,gender,height,weight): # whatever followed by self, will be considered as parameter
        self.age = age # self.age is a property of the person and  = age is an argument that is passed
        self.gender = gender
        self.height = height
        self.weight = weight

person1 = Person(25,"M",178,82) # this is how we created an object
person2 = Person(23,"F",155,55)
# how to access all this value
print(person1.age)


    


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