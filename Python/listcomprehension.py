# deep copy 25/6

fruits = ["apple","orange","mango","banana","grapes"]
prices = [55,234,443]

# for loop with some statement
for fruit in fruits:
    print(fruit)

overseas_fruit = []
# for loop with list
for fruit in fruits:
    overseas_fruit.append(fruit)
print(overseas_fruit)

# using list comprehension
overseas_fruit = [fruit for fruit in fruits]
print(overseas_fruit)

# using tuple comprehension
overseas_fruit = (fruit for fruit in fruits)
print((overseas_fruit))

priceswithsst = []
for price in prices:
    pricewithsst = price + ( price * 0.06)
    priceswithsst.append(pricewithsst)

print(priceswithsst)

# using list comprehension
priceswithsst =[price + (price * 0.06) for price in prices]
print(priceswithsst)

# task which we need to do is find priceswithsst
# you need price
# now using the above information create a function

def calculateSST(price):
    pricewithsst = price + ( price * 0.06)
    return pricewithsst

# this map function takes 2 parameter
# 1st parameter is the function and second parameter is the list

priceswithsst = map(calculateSST,prices)
print(list(priceswithsst))

# what map does?
# inside map there is a for loop which pulls out the price from prices
# and pass the price to our function .Our function return the price with sst
# now map append this return value inside a list
# finally once all the prices are iterated the map functions returns the list

# def map(func,values):

fahrenheitvalues = [32, 33, 34, 35, 36, 37, 38, 39, 40]
celsiusvalues =[]
for fahrenheitvalue in fahrenheitvalues:
    celsiusvalue = (fahrenheitvalue - 32) * 5/9
    celsiusvalues.append(celsiusvalue)

print(celsiusvalues)

# using list comprehension
celsiusvalues = [((fahrenheitvalue - 32) * 5/9) for fahrenheitvalue in fahrenheitvalues]
print(celsiusvalues)

def fahreinheittocelsius(fahreheitvalue):
    return (fahreheitvalue -32) * 5/9
celsiusvalues = map(fahreinheittocelsius,fahrenheitvalues)

print("fah",list(celsiusvalues))

# all the three above exapmles are trying to create a new list
# for number of items in both list are same
# Instead of writing the traditionally for loops
# you can use something called list comprehension

multiplesofthree = []
for number in range(1,50): # list of 50 items
    if(number % 3 == 0):
        multiplesofthree.append(number)
print(multiplesofthree)

multiplesofthree = [number for number in range(1,50) if (number % 3 == 0)]
print(multiplesofthree)

# using filter class
def findmultipleofthree(number):
    return True if number % 3 == 0 else False

multiplesofthree = filter(findmultipleofthree,range(1,50))
print(list(multiplesofthree))

numbers = [2,5,7,3,4,6,10,11,15,17,24,22]
oddnumbers = []
for number in numbers:
    if number % 2 != 0:
        oddnumbers.append(number)
print(oddnumbers)

# using list comprehension
oddnumbers = [number for number in numbers if number % 2 != 0]
print(oddnumbers)


# using filter class
def isOddNumber(number):
    return True if number % 2 != 0 else False

oddnumbers = filter(isOddNumber,numbers)
print(list(oddnumbers))


# all the two above exapmles are trying to create a new list
# for number of items in the created list is less than or equal to original list 
# instead of writing the traditonaly for loops
# you can use something called list comprehension or filter class

sum = 0
for number in range(1,11):
    sum = sum + number
print("sum:", sum)

mean = 0
for number in range(1,11):
    mean = mean + number
mean = mean / len(range(1,11))
print("mean: ",mean)


# in the above 2 examples we are trying to reduce the list to a single value
# we cannot use list comprehension

#  reduce is not a built in function
# it is inside a module called itertools

from functools import reduce

numbers = [1,2,3]

def findtotal(oldvalue,currentvalue):
    return oldvalue + currentvalue

print(reduce(findtotal,numbers))
# reduce function takes another function as first parameter
# that function suppose to take 2 parameter
# reduce funtions takes list as second parameter
'''
def reduce(func, numbers):
    sum = 0
    # however the original reduce function is smart
    # it will initialize the sum variable with 1 if you use multiplication
    for number in numbers:
        sum = func(sum,number)
    return sum

'''
def factorial(oldvalue, currentvalue):
    return oldvalue * currentvalue

print(reduce(factorial, numbers))

# now we are initializing the sum variable with 5
print(reduce(factorial,numbers,5))

