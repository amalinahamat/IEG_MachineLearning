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

# 4

def addition(n1,n2):
    add = n1 + n2
    return add

def subtraction(n1,n2):
    subtract = n1 - n2
    return subtract

def multipl





            









