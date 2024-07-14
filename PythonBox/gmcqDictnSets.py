# IExplore

# 1

'''What is the output of the function shown below?
import math
print abs(math.sqrt(25))
=> 5.0'''

# 2

'''Which of the following functions is a built-in function in python?
=> print()'''

# 3

'''What is the output of the function shown below?
print all([2,4,0,6])
=> False''' # False due to 0 is considered false

# 4

'''What is the output of the expression:
print round(4.576)
=> 5'''

# 5

'''What is the output of the following code?
a=(1,2,3,4)
del(a[2])
=> Error as tuple is immutable'''

'''TypeError: 'tuple' object doesn't support item deletion
tuples are immutable in Python. Tuples cannot be changed after their creation, which includes adding, 
removing, or modifying elements. Attempting to delete an element from a tuple will result in a TypeError.
To modify a tuple, you would need to convert it to a list, make the changes, and then convert it back to a tuple'''

# 6

'''Is the following piece of code valid?
a=(1,2,3)
b=('A','B','C')
c=zip(a,b)
print c
=> Yes, c will be [(1, 'A'), (2, 'B'), (3, 'C')])'''

'''This is because c is a zip object, which is an iterator, and printing it directly will display its memory address
print(list(c))  # Convert the iterator to a list to print the pairs'''
# zip is a built in function that allow to aggregate
# elemts drom multiple iterable into a single iterable


# 7

'''What is the output?
d = {"john":40, "peter":45}
print d["john"]
=> 40'''

# 8

'''What is the output of the following code?
a=(2,3,4)
sum(a,3)
=> 12''' # means initial sum = 3 => 3 +2 + 3+4 = 12

# 9

'''Read the code shown below carefully and pick out the keys?
d = {"john":40, "peter":45}
=> “john” and “peter”'''

# 10

'''Which of the following statements create a dictionary?
a) d = {}
b) d = {“john”:40, “peter”:45}
c) d = {40:”john”, 45:”peter”}
d) All of the mentioned

=> d'''

# IAnalyse

# 1

'''Is the following piece of code valid?
a=(1,2,3)
b=('A','B','C')
c=zip(a,b)
print c

=> Yes, c will be [(1, 'A'), (2, 'B'), (3, 'C')])'''

# 2

