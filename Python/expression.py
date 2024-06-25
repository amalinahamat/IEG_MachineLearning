# Arithmetic Operator
x = 7
y = 2
# print function takes expression as an argument
# result = x + y
# print("Addition: ", result)
print("Addition: ", x + y)
print("Subtraction: ", x - y)
print("Multiplication: ", x * y)
print("Division: ", x / y)

print("Quotient: ", x // y)
print("Remainder: ", x % y)

print("Exponent: ", 10 ** 3)
print("What is the maximum number in a 64 bit env: ", (2 ** 64) - 1)

# Assignment Operators
x = 0
x += 1 # x = x + 1
# y = mx + c
# y = x ** 2 + 2 * x + 3

x += 1 # x = x + 2
x += 5 # x = x + 5

# x = 108
x += x + 1 # x = x + x + 1
# x =  108 + 109 = 217
print(x)

x -= 1 # x = x - 1


x -= 1 # x = x - 1
x *= 1 # x = x * 1
x /= 1 # x = x / 1
x //= 1 # x = x // 1
x %= 1 # x = x % 1


# Comparison operators
myheight = 5.2
yourheight = 5.3
mysisterheight = 5.2

#Let us create TRUE Statement
print(yourheight > myheight)  # greater than
print(myheight == mysisterheight) # equals to
print(mysisterheight , yourheight) # less than
print(myheight != yourheight) # not equals to

print(yourheight >= myheight) # greater than or equals to 
print(myheight >= mysisterheight) # greater than or equals to

print(myheight <= yourheight) # less than or equals to
print(mysisterheight <= myheight) # less than or equals to


a = 21
b = 14
c = 7

print(a > b and a > c) # a is the greatest number
print(c < a and c < b) # c is the smallest number
print((b > c and b < a) or ( b > a and b < c)) # b is the middle number

# Negation operator
print(not (a > c)) # False
print(not (a < c)) # True

# Truth table
# XOR => ^
print("XOR:",(a > c) ^ (a>b))