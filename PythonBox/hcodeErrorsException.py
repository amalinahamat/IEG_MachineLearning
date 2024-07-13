# IDesign

# 1
# Write a Python program that accepts two numbers as input (say x and y) and finds x/y.
# When the denominator is 0, the program should raise a ZeroDivisionError Exception and 
# print the message shown in the sample output.
# Enter number 1
# 5
# Enter number 2
# 0
# Divide By Zero Error
# Enter number 1
# 6
# Enter number 2
# 3
# 2.0
try:
    x = int(input("Enter number 1\n"))
    y = int(input("Enter number 2\n"))

    result = x / y
    print(f"{result:.1f}")

except ZeroDivisionError:
    print("Divide by zero")


# 2 
# Write a Python program that accepts two numbers as input (say x and y) and finds x/y.
# When the denominator is 0, the program should raise a ZeroDivisionError Exception and 
# print the message shown in the sample output.
# When there is an error in value in any of the 2 input arguments, the program should 
# raise a ValueError Exception and print the message shown in the sample output.
# Check for ValueError Exception while performing the division
# Enter number 1
# 5
# Enter number 2
# 0
# Divide By Zero Error
# Enter number 1
# t
# Enter number 2
# 5
# Invalid Value
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


# 3
# Create a class named Student with a single attribute – marks.
# Include a method named check_marks in the Student Class.
# This method checks whether the marks is greater than  or equal to 90 
# and if it is greater than or equal to 90, the method returns True.
# If the marks is less than 90, a custom Exception named NotEligibleException 
# is raised and an appropriate message as shown in the sample output is displayed.
# Create a custom Exception class named NotEligibleException.
# Create an object of the student class and test the above methods
# Enter marks of student
# 56
# Inside Except Block : Not Eligible
# Enter marks of student
# 98
# Eligible

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


# 4
# Write a program that prompts users to enter numbers till he enters one positive number. 
# Whenever the user enters a negative number or a string , raise a ValueError exception and 
# handle it appropriately and display the message shown in the sample output.
# Enter a positive integer
# 5
# Good! You entered 5
# Enter a positive integer
# -6
# You entered a negative number. Retry!
# Enter a positive integer
# -9
# You entered a negative number. Retry!
# Enter a positive integer
# 3
# Good! You entered 3
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


# 5
# Thus, write a program to find the batting average of his captain, for given 'n' matches.
# This program may generate Type Error exception, if there is a type mismatch when rating 
# is got as input. Use exception handling mechanisms to handle this exception.
# Enter the number of matches
# 4 
# Enter the scores
# 34
# 12
# 24
# 20
# Batting average: 22.50
# Enter the number of matches
# 2 
# Enter the scores
# 10
# r 
# Type Error Exception

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


# 6
# If people is eligible to vote only after 18 and above.
# This program may generate:
# 1. InvalidAgeRange Custom Exception when the People's age is below 18
#  Use exception handling mechanisms to handle these exceptions
# Create a class called CustomException which extends Exception 
# and it includes constructor to initialize the message.
# Use appropriate exception handling mechanisms to handle these exceptions
# Enter the Name
# naveen
# Enter the age
# 25
# Voter name: naveen
# Voter age: 25
# Enter the Name
# shilpa
# Enter the age
# 12
# CustomException: InvalidAgeRangeException
class CustomError(Exception):
    def __init__(self, message="InvalidAgeRangeException"):
        self.message = message
        super().__init__(self.message)

try:
    name = input("Enter the Name\n")
    age = int(input("Enter the age\n"))

    if age >= 18:
        print(f"Voter name: {name}\nVoter age: {age}")
    else:
        raise CustomError()

except CustomError as InvalidAgeRange :
    print(f"CustomException: {InvalidAgeRange}")



# iAssess

# 1
# An input list is given in the code template.
# Write a program to find the sum of first n values from the given list.
# For invalid ‘n’ values, raise an IndexError Exception and display the message shown in the sample output.
# [2, 3, 1, 5, 6, 7, 1]
# Enter n
# 5
# Sum = 17
# [2, 3, 1, 5, 6, 7, 1]
# Enter n
# 10
# Index Value out of range

numlist = [2,3,1,5,6,7,1]
print(numlist)

#fill your code
class CustomError(Exception):
    def __init__(self, message="Index Value out of range"):
        self.message = message
        super().__init__(self.message)

try: 
    n = int(input("Enter n\n"))

    if n > len(numlist):
        raise CustomError ()
    
    sum = 0

    for num in numlist:
        if n > 0:
            sum = sum + num
            n = n - 1

    print(f"Sum = {sum}")

except CustomError as e:
    print(e)


# 2
# During account creation he has enter the username and password, in which the password should be 
# contain atleast one lowercase letter, one upper case letter and a number, otherwise exception occured.
# So write a program to check the password is valid or invalid.
# Conditions for a valid password: 
# Password should contain atleast one lowercase letter, one upper case letter and a number. 
# Use exception handling mechanisms to handle these exceptions 
# Sample Input and Output 1 : 
# Enter the username
# Vikram
# Enter the password 
# 1samudrA
# Employee Username: Vikram
# Password: 1samudrA
# Sample Input and Output 2 : 
# Enter the username 
# Rashmi
# Enter the password 
# hawai
# CustomException: Invalid Password Exception
class CustomError(Exception):
    def __init__(self, message="Invalid Password Exception"):
        self.message = message
        super().__init__(self.message)

def validate_password(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if not (has_lower and has_upper and has_digit):
        raise CustomError()

username = input("Enter the username\n")
password = input("Enter the password\n")

try:
    validate_password(password)
    print(f"Employee Username: {username}\nPassword: {password}")

except CustomError as e:
    print(f"CustomException: {e}")
