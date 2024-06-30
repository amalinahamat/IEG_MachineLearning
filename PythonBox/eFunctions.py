#videos 1

'''
functions 
1.reusability
2.modular => easy to detect error

1.in built functions
2.user-defined function

1. start with def => definition
2. followed by a function mane (rules for name same as variable)
3. followed by (parameter/input/argument) => can also pass wothout argument
4. folloes by :
5. eg . def dum_of_two_number(a,b):


'''
'''
def mul(x,y):
    f = x * y
    return f
def sum_of_two_numbers(a,b):
    print("Inside sum function")
    add = a + b
    d = mul(add,b)
    return add # default return value is None

a = 3
b = 4
add = sum_of_two_numbers(a,b)
f = mul(add,b)
print("sum =", add)
print("mul",f)
'''
'''
recursion = a function calling (a copy) of itself
code look simple

def fun(args):
    pass

factorial 
n! = n*(n-1)
5! = 5*4*3*2*1
4! = 4*3*2*1
3! = 3*2*1
2! = 2*1
1! = 1 => BASE CASE
0! = 0

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

    n = int (input())
f = factorial(5)
print(f)

fibonacci

0 1 1 2 3 5 8 13 21....
0 1 2 3 4 5 6....

n == 0
n == 1
f(n) = f(n-1) + f(n-2)


def fib(n):
    if n == 0 or n == 1: return n
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))


combination

nCr = n!/(r!*(n-r)!)

nCr = (n-1)Cr + (n-1)C(r-1)

6C4 = 5C4 + 5C3

15 = 5 + 10

nCn = 1
nC1 = n
nC0 = 1

def comb(n,r):
    if r == n or r == 0: return 1
    if r == 1 :return n
    return comb(n-1,r) + comb(n-1,r-1)

n = int(input())
r = int(input())

print(comb(n,r))

'''
'''
stack model
Last in Fist out

1) required argument
2) keyword argument
3) default argument
4) variable-length argument

def sum(b,a):
    print("a=",a)
    print("b=",b)
    c = a + b
    return c

x = 5
y = 10
d = sum(a=x,b=y)
print(d)
'''
'''
def sum(a=5,b=10,d=20,e=30):
    c = a+b+d+e
    return c

print(sum())
x = 5
c = sum(x)
print("sum=",c)
d = sum(x,20)
print("sum=",d)

or

print(sum())
print(sum(50))
print(sum(50,100))
print(sum(50,100,200))
print(sum(50,100,200,300))

---
def sum(b,c,*a):
    print(a)
    print(type(a))
    print("b=",b)
    print("c=",c)

d = sum(1,2,3,4,5,6,7,8,9,10)
print("d = ",d)



'''
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



    









            









