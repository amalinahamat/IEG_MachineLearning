# videos

# video 1 intro to errors
'''
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
'''

# video 2  built-in errors
'''

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
'''

# video 3 raising errors

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


# videos 4 creating errors 

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


# video 5 dealing with python errors

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
    print("Your car was not a Car!")

try:
    ford.add_car(fiesta)
except TypeError:
    print("Your car was not a Car")  #if other error than TypeError, it will print nothing
except ValueError:
    print("Something weird happened...")
finally: # finally block will run everytime
    print("The garage now has {len(ford)} cars.")


# video 6 on-success block re-raising exception

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


# videos 7 handling user errors

def power_of_two():
    n = input("Please enter a number: ")
    n_square = n ** 2
    return n_square
# this program will break because the input() function returns a str, but the code tries to use 
# the str as a number. however we cannot calculate a str to the power of 2

def power_of_two():
    user_input = input("Please enter a number: ")
    n = float(user_input)
    n_square = n ** 2
    return n_square
# this program will work if the user does input a number. However, we can't always expect 
# users' input be valid. if the input was not a number, then we cannot convert it to 
# a float, thus the program will break

def power_of_two():
    user_input = input("Please enter a number: ")
    try:
        n = float(user_input)
    except ValueError:
        print("Your input was invalid")
    finally:
        n_square = n ** 2
        return n_square
# if input = 4, we will get 16.00
# if input = str = dan, we will get an error
# the finally blocks gets executed regardless of the occurence of ValueError. However,
# we only defined 'n' in the try block. if the input was invalid, 'n' never gets its value assigned,
# and thus will raise an error when we try to access it in the finally block

def power_of_two():
    user_input = input("Please enter a number: ")
    try:
        n = float(user_input)
    except ValueError:
        print("Your input was invalid")
        n = 0
    else:
        n_square = n ** 2
        return n_square
# the else block only gets executed if no error occurs in the try block. So if the code will finish
# after assigning n with default value 0 if it ever reaches the except block. But in this
# case, there is no return statement , thus the function returns None

def power_of_two():
    user_input = input("Please enter a number: ")
    try:
        n = float(user_input)
    except ValueError:
        print("Your input was invalid")
        n = 0
    else:
        n_square = n ** 2
        return n_square
    finally:
        return n_square
# the finally block gets executed regardless of the occurence of ValueError, while else block
# only gets executed if no error occurs in the try block. However, we only defined 'n_square' in the else block.
# if the input was invalid, 'n_square' never gets its value assigned, thus will raise an error 
# when we try to access it in the finally block

def power_of_two():
    user_input = input("Please enter a number: ")
    try:
        n = float(user_input)
    except ValueError:
        print("Your input was invalid")
        return 0
    finally:
        n_square = n ** 2
        return n_square
# if there are two return which in except and finally, the python will use return in finally
# so, if the input_user error, it will return error instead of 0
# the finally block will get executed regardless of the return statement in both try block and except block
# however, we only defined 'n' in the try block. if the input was invalid, 'n' never gets its value
# assigned, thus will raise an error when we try access it in the finally block 

def power_of_two():
    user_input = input("Please enter a number: ")
    try:
        n = float(user_input)
        n_square = n ** 2
        return n_square
    except ValueError:
        print("Your input was invalid. Using default value 0")
        return 0

print(power_of_two())
print(power_of_two())
# if the user input is number, it will return n_square.
# if the user_input is othe than number, it will return 0
