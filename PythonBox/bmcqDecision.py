# 1
# What gets printed?

x = True
y = False
z = False
if x or y and z:
    print("Hello")
else:
    print("World")

# -> Hello
# The logical and operator has higher precedence than the logical or operator. Therefore, the expression y and z is evaluated first, and then the result is evaluated with x using the or operator.

# 2
# In a conditional statement, the boolean expression after the if or elif statement is called a ______________.
# -> condition


# 3
# What is the output ?

a = 20
if a >= 22:    
    print("if")
elif a >= 21:    
    print("elif")
# -> nothing will be printed


# 4
# What does an if control statement do?
# -> makes a decision


# 5
#  What is the output? 

a = 20 
if a >= 22:     
    print("if") 
elif a >= 21:     
    print("elif") 
else:    
    print("else")

# -> else


# 6
# What is the output of the following? 

grade = 60
if grade >= 65: 
    print("Passing grade")

# -> no output


# 8
# What keyword would you use to add an alternative condition to an if statement?
# -> elif


# 9
# What is the output of the following?

grade = 60
if grade >= 65:
    print("Passing grade")
else:
    print("Failing grade")
# -> Failling grade


# 10
# Which Python statement will check “a is greater than or equal to b”?
# a)  Both b and c
# b)  if (a >=b):
# c)  if a >= b:
# d)  if a > b:
# -> both b and c

# iAnalyse
# 1
# What gets printed?
x = 1
y = 0
z = 0
if y or x and z:
    print("yes")
else:
    print("no")
# -> no


# 2
# What is the output of the following?
x = 20
if not x == 50:
    print('the value of x different from 50')
else:
    print('the value of x is equal to 50')
# -> the value of x different from 50


# 3
# What will be the output for the following code?
i = 10
if(i>15):
    print("10 is less than 15")
print("I am Not in if")
# -> I am not in if


# 4
age = 38
if(age >= 11):
    print("You are eligible to see the Football match.", end ="")
    if(age <= 20 or age >= 60):
        print("Ticket price is $12", end = "")
    else:
        print("Tic ket price is $20", end="")
else:
    print("You are not eligible to buy a ticket.")
# -> You are eligible to see the football match, Tic ket price is $20


# 5
# What is the output for following code segment?

if (10 < 0) and (0 < -10):
    print ("A")
elif (10 > 0) or False:
    print ("B")
else:
    print ("C")
# -> B


# 6
if True or True: # True
    if False and True or False: # false and true = false, false and false = false
        print("A")
    elif False and False or True and True: # false and false = false, false and true = false, false or true = true.  and gets executed first 
        print("B") # Since the elif condition is True, the corresponding block is executed, and B is printed. 
    else:
        print("C")
else:
    print("D")
# -> B


# 7
# what gets printed?
x = True
y = False
z = False
# and is a highest precedende that or
if not x or y: # not true(x) = false, false or false(y) = false
    print(1)
elif not x or not y and z: # not false(y) = true, true and false = false, not true(x) = false, false pr flase = false
    print(2)
elif not x or y or not y and x: # not false(y) = true, true and true(x) = true, not true(x) = false, false or true = true, flase(y) or true = true
    print(3)
else:
    print(4)
# -> 3


# 8
# Which of the following is not a conditional statements in python?
# if
# elif
# else
# switch
# -> switch


# 9
# What will be the output for the following code?
var = 100
if var == 200:
    print("1 - Got a true expression value", end="")
    print(var,end="")
elif var == 150:
    print("2 - Got a true expression value", end="")
    print(var, end="")
elif var == 100:
    print("3 - Got a true expression value", end="")
    print(var, end="")
else:
    print("4 - Got a false expression value", end="")
    print(var, end="")
print("Good bye!")
# -> 3 - Got a true expression value 100 Good bye!


# 10
# What is the output of the following?
x = False
y = True
if x and y:
    print('Both x and y are True')
else:
    print('x is False or y is False or both x and y are False')
# -> x is False or y is False or both x and y are False


