# there are 4 different types of builtin data structure in python
# they are list, tuple, set and dictionary

# list uses []
# list is modifiable (append, edit and delete)
# list is ordered (the items retain its position)
# list is indexed (0, 1, 2, 3, 4, .....)
# list allows duplicates

fruits = ["apple", "orange", "mango", "banana", "grapes"]
# fruits is a variable assigned with multiple value(s)
# fruits is also called object
# if anything is called object, which means it is instance of a class
# Jegan, John, Peter, Khairi are objects , instance of a human class
# Jegan hay eyes(2), nose(1), legs(2) => properties
# Jegan can walk can run can eat can teach can listen => method
# fruits objects also will have its own properties and methods 
print(fruits)

# indexing and selection
# refer to variablesparttwo.py

# modifiable
fruits.append("durian")
# the item gest added as last item
print(fruits)

# insert items inside the existing list
fruits.insert(1, "rambutan")
print(fruits)
fruits.insert(3, "cempedak")
print(fruits)
fruits.insert(5, "dummy")
print(fruits)

# update items in the list
fruits[5] = "mangosteen"
print(fruits)

# how to remove an item from the list
fruits.remove("durian")
print(fruits)

# to remove the last item you can use the method pop
fruits.pop()
print(fruits)

# delete an item by index
# we can delete anything from memory permanently using the keyword del
greeting = "good morning"
del greeting
# did you notice there is no () after del so it is confirm KEYWORD
# print(greeting)
# print([1, 2, 3, 4, 5] + 5) # typeError
del fruits[3]
print(fruits)

# if you want to clear the list (remove all the items in the list)
fruits.clear()
print(fruits)

# this will delete the entire list
del fruits

fruits = ["apple", "mango", "orange", "mango", "apple", "banana", "grapes", "apple"]
print(fruits.index("mango")) # 0, 1

newfruits = fruits[2:] # 0, 1
print(fruits.index("mango") + 1)

print(fruits)

# Enumerate is an iterable object
# but print do not know how to iterate the enumerate object
# however we can typecast the enumerate object to a list using list function
print(list(enumerate(fruits)))
# Enumerate returns list of tuple
# Each tuple has 2 items, the first item is the index and the second item is the fruit
for item in enumerate(fruits):
    # print(item[0])
    # print(item[1])
    if item[1] == "mango": print("Mangi is in position:", item[0])

# you may want to know how many apples are there in the list
print("Total number of apples:", fruits.count("apple"))

# there are other functions which can help us to sort the items in the list
fruits.sort()
print(fruits)

# you can also reverse the list
fruits.reverse()
print(fruits)

for fruit in fruits:
    print(fruit)

# the following is to demonstrate shallow copy
x = [10, 20, 30, 40, 50]
y = x
print(x)
print(y)
x[2]= 35
print(x)
print(y)

# you have to perform deep copy
x = [10, 20, 30, 40, 50]
# y = x Don't do this
y = []
for i in x:
    y.append(i)
print("=" * 40)
print(x)
print(y)
x[2] = 35
print(x)
print(y)

# in fact you no need to create a for loop to copy
# rather you can just use a copy method
x = [10, 20, 30, 40, 50]
y = x.copy() # just use this
print("=" * 40)
print(x)
print(y)
x[2] = 35
print(x)
print(y) # reference data type

# fruit is an instance of a list class
# technically, the objects are created by calling the class
x = list([10, 20, 30, 40, 50])
print(x)
# however in python to create list instead of using class they let you use []
x = [12, 13, 14, 15, 16]
print(x)

# in python to invoke or call the operator we use is () => parenthesis // round bracket
# () is used in expression
# to call built in function print() sum() id()
# to create object we call the class type() int() float() list() map() tuple()
# to call function inside the module sys.path()
# to call method in a object "Television".split()
# to create a tuple also we use ()


def total(numbers):
    print(type(numbers))
    numbers[2] = 35
    result = 0
    for number in numbers:
        result = result + number
    return result


x = [10, 20, 30, 40, 50]
print(x)
print(total(x))
print(x)

# the above is the reason why you should not send list as arguments
# this is the main reason why python always convert collection to tuple

# ok understood now how to convert list to tuple
# you pass the list to tuple class it will return tuple object
x = tuple(x)
# print(total(x))

# as i mention earlier whenever python has to convert the data to a colelction
# it will use tuple
#print(total(10, 20, 30, 40, 50, 60))

#print(type(total()))

# one last feature in list
# list can auto explode
# explose means create 1 variable for every item in the list
fruit = ["apple", "mango", "durian"]

fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]

# however in python you no need to explode manually
fruit1, fruit2, fruit3 = fruit
# in other words we are assigning multiple items in the list to multiple variables
print(fruit1, fruit2, fruit3)