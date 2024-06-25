# tuple is nothing but readonly list
# tuple uses ()
# tuple is not modifiable (append, edit and delete)
# tuple is ordered (the items retain its position)
# tuple is indexed (0, 1, 2, 3, 4, .....)
# tuple allows duplicates

x = (10, 20, 30, 40, 50, 60, 70)
print(x)
print(type(x))

# selection and indexing
# refer to variablesparttwo.py
print(x[0])

# is not modifiable
# which means you do not have append, insert, remove
# however you can delete the entire tuple using del keyword
# del x[0] => i repeat this is not allowed
del x

fruits = ("apple", "mango", "durian", "apple")
print(fruits)
print(fruits.count("apple"))
print(type(fruits))

# tuple does not have many features as list
# why we use tuple?
# since tuple does not have many feature obviously
# 1) take less space
# 2) faster than list
# normally python handles its lists//collections using tuple
def returnFruits():
    # return keyword cannot return more than one value
    # so python must convert the values to "tuple"
    # whenever python automatically converts data collection
    return "apple", "mango"

print(type(returnFruits()))

def total(*numbers):
    print(type(numbers))
    result = 0
    for number in numbers:
        result = result + number
    return result



# as i mention earlier whenever python has to convert the data to a colelction
# it will use tuple
print(total(10, 20, 30, 40, 50, 60))
#print(type(total()))

# one last feature in tuple
# tuple can auto explode
# explose means create 1 variable for every item in the tuple
fruit = ("apple", "mango", "durian")

fruit01 = fruit[0]
fruit02 = fruit[1]
fruit03 = fruit[2]
print(fruit01, fruit02, fruit03)

# however in python you no need to explode manually
fruit1, fruit2, fruit3 = fruit
# in other words we are assigning multiple items in the tuple to multiple variables
print(fruit1, fruit2, fruit3)

# there is a problem to highlight in tuple / how to tell that this x is a object instance of tuple class . () also used for expression
x = (10)
print(type(x))
# now python really confused is it tuple or expression 
# python gives priority for expression than tuple
# automatically 10(integer) is assigned to x
# to ensure the data is in tuple format please add an extra comma
x = (10,)
print(type(x))
