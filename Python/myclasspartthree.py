# Encapsulation
# Encapsulate the properties inside the class
# in other languages we have keywords public , private, protected
# to protect the properties
class circle:

    def __init__(self,radius):
        self.__radius = 0 # need to initialize outside the if condition to created the self.radius
        if(isinstance(radius,int)):
            self.__radius = radius  # use _ to make it private but if the user also put _ , it does not work. use __ to make it work. juat accept int
        else:
            print("Invalid Radius")

    # getter method and setter method // secretary
    def getRadius(self):
        return self.__radius
    
    def setRadius(self,radius):
        if isinstance(radius,int):
            self.__radius = radius
        else:
            print("Invalid Radius")

    # property is a class
    # We are calling/invoking the class by passing the method as an argument
    # Please notice after getRadius there is no ()
    # the property class returns the property object which is assigned to
    # a variable radius
    # in other words radius is an instance of property class

    ###
    radius = property(getRadius,setRadius)  # property is a class. it willl return an object # create a new property called radius

    def area(self):
        return 3.14 * self.__radius * self.__radius
    
    def circumference(self):
        return 2 * 3.14 * self.__radius
    
    def __str__(self):
        return f"Radius of this circle is {self.__radius}"


mycircle = circle(20)
print(mycircle)

#mycircle = circle("abc")
#print(mycircle)

mycircle._radius = "abc" # not checking integer or not. assess directly the properties inside and accept the abc as a radius
print(mycircle)
print(mycircle.area()) # it will create error because abc is not an integer
# hence everytime we assigned value to the properties, we must check it to validate the value. it also called encapsulate
mycircle.__radius = "abc" # not checking integer or not. assess directly the properties inside and accept the abc as a radius
print(mycircle)
print(mycircle.area()) 

# my_circle._radius = 30
# you are indirectly passing the value 30 to the setter method
mycircle.radius = 30 # radius is property
print(mycircle)
mycircle.radius = "abc"
print(mycircle)



# identify the class
# identify the property in the class
# identify the  intitialize in the class