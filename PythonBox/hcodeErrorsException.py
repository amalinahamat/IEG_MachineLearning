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
'''
'''
# 6

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
'''

# iAssess
'''
# 1

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
    print()

numlist = [2,3,1,5,6,7,1]
print(numlist)

#fill your code

class CustomError(Exception):
    def __init__(self, message="Index Value out of range"):
        self.message = message
        super().__init__(self.message)

#class IndexError(Exception):
#    def __init__(self, message="Index Value out of range"):
#       self.message = message
#       super().__init__(self.message)

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

'''
# 2

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
