# product is the variable
# television is the string value/literal
# to differentiate the variables from value, we use double quote "" or single quote ''  or  """""""
product = "Television"
quantity = 2 # integer
price = 1455.25 # float
available = True # boolean value/literal (true/false)
print("Product: ", product)
print("Quantity: ", quantity)
print("Price: ", price)
print("Available: ", available)

# type is another built in function that tell us what is the
# data type of the variables (dynamically assigned by python)
print(type(product)) # inner function get executed first. function calling a function as an argument to another function. type calling product(executed first) to be an argument to to a print
print(type(quantity))
print(type(price))
print(type(available))

#((a + b) * c)

total = quantity * price
print("Total: ", total)

# in real world use cases the 10 will not be hard coded
# the 10 is coming from an input device (keyboard)
# so the input value can be a string which needs to be converted
quantity = "10"
print(type(quantity))

#print(quantity * price) => error because string/sequence cannot be multiply with the numbers 


# type casting
# convert one data type to another
# to convert string to integer, we have built in function int
# to convert string to float, we have built in function float

print(int(quantity) * price)

total = int(quantity) * float(price)
print(total)

x = 100
print(x)
# Now i want to know the address location where 100 is
# We can use a built in function called id
print(id(x))

y = 100
print(y)
print(id(y))

# However in python, the object 100 is not created first
# Python scan first and if the object 100 is already exists then
# Python will reuse the object instead of re-creating the object

a = "hello"
b = "hello"
c = "Hello"
print(id(a))
print(id(b))
print(id(c))

# So far we have seen how to assign single value to a single variable
# in one line of statement
# x = 100

# how to assign more than one value to more than one variable
# in one line of statement
x, y =  101, 102

# you can also do this
x, y = 101 + 1, 102 + 1
x, y = x + 1, y + 1
print(x, y)

# in some programming language you can assign 
# multiple variable with a single value
# x, y = 501 # however in python this is not allowed

# in other programming language, we call these as variable initialization
# but in python, there is no way for you to create a variable
# without assigning a value
y = 0 # numeric initialization
y = "" # string initialization / empty string
y = None # means no value
print(y)
print(type(y))

# functions can be treated as variable but will have side effects
# print = 10
# print(print)
# keyword cannot be treated as a variable
# if = 10






