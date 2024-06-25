firstName = "Khairi"
lastName = "Abu Bakar"
# usually both sides of the operator is numbers
# if they are number we can perform addition

# if both sides are string we can perform "string concatenation"
fullName =  firstName + "" + lastName

carPlate = "JCG"
number = 6979
# however this use case we cannot add them because one is number
# another one is string
# carPlateNumber = carPlate + number
# i can only concatenate str (not "int") to str
# in this case we cannot convert carPlate to number
# so let us convert number to string using str function
carPlateNumber = carPlate + str(number)
print(carPlateNumber)

# In python you can multiply string with integer
# When we do this, it will product "times" effect
product = "book"
print(product * 5)
print("=" * 40)
print("nak balik " * 100)



# Traditionally how we handle multiline strings
# we handle it using string concatenation
# however we still miss the new line characters
# we have to introduce a special character \n
# the slash \ character is also called escape character
# the slash \ followed by t means tab key
# the slash \ followed by r means carriage return


message = "As I am not feeling well"
message = message + "I wont't be able to attend the meeting."
message = message + "Please proceed the meeting without me."

myfile = "c:\newfolder\table\read.txt"
print(myfile)
# we suppose to tell the python to ignore the sequence
# you can add extra escape sequence
myfile = "c:\\newfolder\\table\\read.txt"
print(myfile)
# however in python we also have special string called raw string
myfile = r"c:\newfolder\table\read.txt"
print(myfile)

# so far we know strings are enclosed with double quote
# or single quote
# we can also used triple double quote or triple single quote
# they are used to create multiline string
# you no need to do \n you no need to do tring concatenation
message = """As I am not feeling well
I wont't be able to attend the meeting.
Please proceed the meeting without me."""
print(message)

# relationship between string and list
# strings are nothing but list of character
mygreeting = "Hello World"
print(mygreeting[0])
print(mygreeting[0:6])
print(mygreeting[::2])
print(mygreeting[::-1])
# how many characters we have in mygreeting
print(len(mygreeting))

# reverse the given number
given_number = 97405
print(int(str(given_number)[::-1]))

# when i started this python class i said all these literals
# are objects.
# "Television" is a string literal / string value
# "Television" is also called string object
# objects have function inside 
product = "Television Cloths Vegetables Fruits"
product.split() 
print(product.split())
# this split function takes the literal
# assigned to the variable product and split them or tokenize them
# into multiple words 
# using space as separator
# since it is going to return more than 1 word, it is going to be 
# list of words
# Functions inside the object is also called "Method"
# From now you must say "print is a function"
# where as "split is a method"
# "Television".
"Television".title


