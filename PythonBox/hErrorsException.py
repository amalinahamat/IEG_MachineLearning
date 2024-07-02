# videos
'''
video 1 intro to error

print(my_variable)

stack traces
1. at the very bottom it gives you the error that was raised and a description
2. what line of your code raised the error
3. what function that line is in
4. what function called the function that the line is in
5. an so on... until you reach the file that you executed

how to solve the problem
1.look at your code
2.put the error and message into Google, see if something comes up in StackOverflow
3.Look at the code again, this time more slowly, and run through it as if you were a computer. Do you notice anything that could potentially be a source of the error?
4.Run only some parts of the code in isolation. that will help identify which part of your code is giving an error
5.use a debugger
6.ask question in the course q&a

video 2  built in error

1. IndexError
- like list index out of range / not exist
2. KeyError
- misuse key / key does not exist
3. NameError
- variable name is not defined // lost of ""
4. AttributeError
- list object has no attribute "intersection"
5. NotImplementedError
- not implemented yet
6. RuntimeError
- base error / happened when running a program
7. SyntaxError
- mess up in coding. missing something like "" ()
8. IndentationError
- tab error // spaces error
9. TabError
- error when switching two editors // tabs and spaces
10.TypeError
- like add string and integer together
11.ValueError
- value of the correct type but incorrect value. int and float . 25.5 is float not int
12.ImportError
- import module 
13.DeprecationWarning
- warning not an error but python treat as an error
- no longer the best way of doing

video 3 raising error

'''
'''
class Car:
    def __init__ (self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make}{self.model}>"

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self,car):
        if not isinstance(car,Car):
            raise TypeError(f'Tried to add a "{car.__class__.__name__}" to garage, but you can only')
        self.cars.append(car)
        #raise NotImplementedError("We cannot add cars to the garage yet")

ford = Garage()
#ford.add_car("Fiesta")
#print(len(ford))

car = Car("Ford","Fiesta")
ford.add_car(car)
print(len(ford))

'''
#videos 4 creating error 
'''
class MyCustomError(TypeError):
    """
    Exception raised when a specific error code is needed
    """
    def __init__(self, messsage, code):
        #super().__init__(messsage)
        super().__init__(f"Error code {code}:{messsage}")
        self.code = code
#raise MyCustomError("OUCH! AN ERROR HAPPENED.",500)

err = MyCustomError('AN ERROR HAPPENED',500)
print(err.__doc__)

'''
#video 5 dealing with python error
'''
class Car:
    def __init__ (self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make}{self.model}>"

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self,car):
        if not isinstance(car,Car):
            raise TypeError(f'Tried to add a "{car.__class__.__name__}" to garage, but you can only')
        self.cars.append(car)

ford = Garage()
fiesta = Car("Ford","Fiesta")

if isinstance(car.Car):
    ford.add_car(fiesta)
else:
    print("Ypur car was not a Car!)

try:
    ford.add_car(fiesta)
except TypeError:
    print("Your car was not a Car")  #if other error than TypeError, it will print nothing
except ValueError:
    print("Something weird happened...")
finally: # finally block will run everytime
    print("The garage now has {len(ford)} cars.)

video 6 on success block reraising exception


class User:
    def __init__(self,name,engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f"<User {self.name}>"
    
def get_user_score(user):
    try:
        user.score =  perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorrect value provided to our calculation function")
    #finally:
    else:
        if user.score > 500:
            send_engagement_notification(user)

def perform_calculation(metrics):
    return metrics["clicks"] * 5 + metrics["hits"] * 2

def send_engagement_notification(user):
    print(f"Notification sent to {user}.")

my_user = User("Rolf",{"clicks":61, "hits":100})
get_user_score(my_user)

videos 7  handling user errors

'''

'''

print("1" == 1)

# more than zero except statements for a try=except block

def foo():
    try:
        return 1
    finally:
        return 2
        
k = foo()
print(k)


try:
    if '1' != 1:
        raise "someError"
    else:
        print("someError has not occured")
except "someError":
    print ("someError has occured")

def foo():
    try:
        print(1)
    finally:
        print(2)
foo()

try:
    pass
    # Do something
except:
    pass
    # Do something
else:
    pass
    # Do something

'''
'''
valid = False
while not valid:
    try:
        n = int(input("Enter a number"))
        while n%2==0:
            print("Bye")
            valid = True
    except ValueError:
        print("Invalid")

def getMonth(m):
    if m<1 or m>12:
        raise ValueError("Invalid")
    print(m)
getMonth(6)

import math
num = int(input("Enter a number of whose factorial you want to find"))
print(math.factorial(num))

num = int(input("Enter a number of whose factorial you want to find"))
print(math.factorial(num))

'''
'''
# 1 IDESIGN
try:
    x = int(input("Enter number 1\n"))
    y = int(input("Enter number 2\n"))

    result = x / y
    print(f"{result:.1f}")

except ZeroDivisionError:
    print("Divide by zero")
'''
'''
# 2 

try:
    x_input = input("Enter number 1\n")
    y_input = input("Enter number 2\n")
    
    x = int(x_input)
    y = int(y_input)

    result = x / y
    print(f"{result:.1f}")

except ZeroDivisionError:
    print("Divide By Zero Error")
except ValueError:
    print("Invalid Value")

'''
'''
# 3

class NotEligibleException(Exception):
    pass

class Student:
    def __init__(self,mark):
        self.mark = mark

    def check_mark(self):
        if self.mark >= 90:
            return True
        else:
            raise NotEligibleException("Not Eligible")

try:   
    marks = int(input("Enter marks of student\n"))
    student = Student(marks)

    if student.check_mark():
        print("Eligible")

except NotEligibleException as e:
    print(f"Inside Except Block: {e}")
'''
'''
# 4


while True:
    try:
        user_input = input("Enter a positive integer\n")
        number = int(user_input)
        if number <= 0:
            raise ValueError("You entered a negative number. Retry!")
        else:
            print(f"Good! You entered {number}")
            break
    except ValueError as e:
        if str(e) == "You entered a negative number. Retry!":
            print(e)
        else:
            print("You entered an invalid value. Retry!")

'''

# 5

matches_number = input("Enter the number of matches\n")

matches_number = int(matches_number)

list_score = []
print("Enter the scores")

for number in range(matches_number):
    try:
        score = int(input())
        list_score.append(score)
    except ValueError:
        print("Type Error Exception")
        exit(1)

sum_score = 0

for i in list_score:
    sum_score = sum_score + i

    
average_score = sum_score / len(list_score)

print(f"Batting average: {average_score:.2f}")



        
    

