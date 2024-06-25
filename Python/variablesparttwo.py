# so far we have learnt how to assign single value to a single
# variable. we also learn how to assign multiple values to
# multiple variables in the same line.
# fruit = "Apple"
# fruit01, fruit02 = "Apple", "Orange"

# Now we are going to learn how to assign multiple values 
# to a single variable.
# lets say we want to go shopping
# we already have list of items to buy in mind
# lets say we want to buy 10 items, doesn't mean we going to 
# create 10 variable and assign each item to each variable
# this is where we use a new data structure called "list"
# in other programming language, they call it an "array"

fruits = ["apple", "orange", "mango", "banana", "grape"]
# 1.values/objext is created first, 2.then variable wii be created
# 3.then, it assigned the address to the variable

# indexing and selection
# [] => index number
print(fruits[0]) 
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
# how many floor we have = 4
# how many house we have = 5

# how many items are they in the list
# there is a built is function called len

print("Number of items we have: ", len(fruits))

# how to find maximum index
print("Maximum index: ", len(fruits) - 1)

# does the index has to be positive number ?
# not necessary it can even be a negative number (only in python)
print(fruits[-1]) # the last item in the list
print(fruits[-2]) # the last but previous item in the list
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])
# this also enable us to retrieve value in a reverse order

# range => min value to max value
# range start_index : end_index
print(fruits[1:3])

# what if we did not mention the strat index
print(fruits[:4])
# since we never mention the start index, it will take start index as 0

# what if we did not mention the end index
print(fruits[1:])
# since we never mention the end index, it will print until the last value

# in the range we can have 3rd number which represent the step up value
fruits = ["apple","rambutan", "orange", "durian", "mango", "cempedak", "banana", "mangosteen", "grape"]
# since we want to include grape also, we use 9 as end index
print(fruits[0:9])
# however i do not want all the items but only the items in the even position
print(fruits[0:9:2])
print(fruits[0:9:3]) # this feature is very important for us to take samples
# for wxample lets say we have 1 million records 
# but we do not want to take all the data and process it
# we want to take sample of 50 items only
# and the selection must be evenly distributed then we can use this step up argument

# in the range also you can have negative numbers (place from smallest number to biggest number)
print(fruits[-5:-1]) # position -1 has grapes however it is not included
print(fruits[-1:-5]) # -1 > -5 start index is greater than end index result is empty list
# this is because by default step up is 1 -1 +1
print(fruits[-1:-5:-1]) # over here item at -5 is not included
# which means if you want to reverse the entire list
print(fruits[::-1])
print(fruits[::-5])

