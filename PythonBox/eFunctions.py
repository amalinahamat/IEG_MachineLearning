'''
# iExplore
# 3
def f(x, y, z):
    return (x + y + z)
print(f(2, -30, 400))
'''
'''
# 5

def printMax(a,b):
    if a > b:
        print(a,"is maximum")
    elif a == b:
        print(a, "is equal to", b)
    else:
        print(b,"is maximum")
printMax(3,4)
'''
'''
# 7

def change(one, *two):
    print(type(two))
change(1,2,3,4)
'''
'''
# 9
def writer():
    title = "Sir "
    name = (lambda x:title + "" + x)
    return name
who = writer()
print(who("Arthur"))
'''
# i analyse

'''
# 2
def sayHello():
    print("Hello World!")
sayHello()
sayHello()
'''
'''
# 4

def power(x,y =2):
    r = 1
    for i in range(y):
        r = r * x
    return r

print(power(3))
print(power(3,3))
'''
'''
# 5

def C2F(c):
    return(c * 9//5 + 32)
print(C2F(100))
print(C2F(0))
'''
'''
# 6
def cube(x):
    return x * x * x
x = cube(3)
print(x)
'''
'''
# 9
def Odd(a,b):
    if a & 1 and b & 1:
        print("Both are Odd")
    elif (a & 1):
        print("%d is Odd" %(a) )
    elif(b&1):
        print("%d is Odd" %(b))

Odd(3,4)
'''

# 10
  
'''
# iDesign 
# 1

def greet(argument1,argument2 = "Welcome to Python Programming"):
    return (f"Hello {argument1},{argument2}")

number = int(input("Menu\n1.Name and Message\n2.Name\n"))

if number == 1:
    argument1 = input("Enter the name\n")
    argument2 = input("Enter the message\n")
    result = greet(argument1,argument2)
elif number == 2:
    argument1 = input("Enter the name\n")
    result = greet(argument1)

print(result)

'''
'''
# 2
def daysInYear(argument1, argument2=False):
    if argument2:
        return f"{argument1} is a leap year"
    else:
        return f"{argument1} is not a leap year"

# Read input year
argument1 = int(input())

# Determine if the year is a leap year
argument2 = (argument1 % 4 == 0 and argument1 % 100 != 0) or (argument1 % 400 == 0)

# Call the function with the year and the leap year status
result = daysInYear(argument1, argument2)
print(result)
'''
'''
# 3
def GCD(n1,n2):
    while n2 !=0:
        temp = n2
        n2 = n1 % n2
        n1 = temp

    return n1

def LCM(n1,n2):
    gcd = GCD(n1,n2) 
    lcm = (n1 * n2) // gcd

    return lcm

print("Enter two integers")
number = 2
nums = []
for num in range(number):
    n = int(input())
    nums.append(n)

n1 = nums[0]
n2 = nums[1]

gcd_result = GCD(n1,n2)
lcm_result = LCM(n1,n2)

print(f"Greatest common divisor of {n1} and {n2} = {gcd_result}")
print(f"Least common multiple of {n1} and {n2} = {lcm_result}")

'''
'''
# 4

def addition(n1,n2):
    add = n1 + n2
    return (f"{n1} + {n2} = {add}")

def subtraction(n1,n2):
    subtract = n1 - n2
    return (f"{n1} - {n2} = {subtract}")

def multiply(n1,n2):
    mul = n1 * n2
    return (f"{n1} * {n2} = {mul}")

def divide(n1,n2):
    div = n1 // n2
    return (f"{n1} // {n2} = {div}")

def modulus(n1,n2):
    mod = n1 % n2
    return (f"{n1} % {n2} = {mod}")

print("Select the operation")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus")
number = int(input("Enter the choice(1/2/3/4/5):\n"))

if number > 0 and number < 6:
    n1 = int(input("Enter the first number\n"))
    n2 = int(input("Enter the second number\n"))
    if number == 1:
        print(addition(n1,n2))
    elif number == 2:
        print(subtraction(n1,n2))
    elif number == 3:
        print(multiply(n1,n2))
    elif number == 4:
        print(divide(n1,n2))
    elif number == 5:
        print(modulus(n1,n2))
else:
    print("Invalid Input")
    
'''
'''
# 5

list_size = int(input("Enter size of list\n"))

list_element = []
if list_size > 0 :
    print("Enter the element in list")
    for size in range(list_size):
        size_element = int(input())
        list_element.append(size_element)

else:
    print("Invalid input")


div_by_13 = lambda x: x % 13 == 0

div_number = []
for num in list_element:
    if div_by_13(num):
        div_number.append(num)

if list_size > 0:
    for num in div_number:
        print(num,end = " ")

    print()
'''
'''
# i assess 1

def multiply1(a):
    mul1 = a * 10 
    return mul1

def multiply2(a,b):
    mul2 = a * b
    return mul2

def multiply3(a,b=9):
    mul3 = a * b
    return mul3

number = 2
list_name = []

for num in range(number):
    n = int(input())
    list_name.append(n)

a = list_name[0]
b = list_name[1]

print(f"the result is {multiply1(a)}")
print(f"the result is {multiply2(a,b)}")
print(f"the result is {multiply3(a,b=9)}")

'''
# 2
def multiVarFunc(department,total_student,total_faculties):

    print("Details:")
    depart = print(f"Department:{department}")
    student = print(f"Total students:{total_student}")
    faculties = print(f"Total faculties:{total_faculties}")
    return depart,student,faculties

department = input("Enter department name:\n")
total_student = int(input("Enter the number of total students:\n"))
total_faculties = int(input("Enter the number of total faculties:\n"))

multiVarFunc(department,total_student,total_faculties)



    









            









