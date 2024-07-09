import numpy as np
a = np.array([1,2,3])
b = [1,2,3]
print(type(a))
print(type(b))

arr = np.array([15,25,35,45,55])
print(arr[4])

arr = np.array([[15,25,35,45],[55,65,75,85]])
print(arr[1,0])

a = np.array([[1,2,3],[4,5,6]])
print(a.ndim) # number of dimension

a = np.array([[1,2,3],[4,5,6]],ndmin = 3)

# i design 

# 1
'''

import numpy as np

# File path
file_path = 'sample_data.csv'

# Read data from CSV into a NumPy array
data = np.genfromtxt(file_path, delimiter=',', dtype=str)

# Print the array
print(data)

'''

# 2

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Array")
print(arr)

print("Array Type")
print(str(type(arr)).replace("<","").replace(">",""))

# 3
import numpy as np

size = int(input(("Enter the size of the list\n")))

print("Enter the elements in the list")

list_size = []
for s in range(size):
    s = int(input())
    list_size.append(s)

arr = np.array(list_size)
print(str(type(arr)).replace("<","").replace(">",""))
print(arr)

# 4

import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

iris_data = iris.data

print(iris_data[:3])

# 5

import numpy as np

a = int(input("Enter the limit\n"))
b = int(input("Enter the number of points\n"))
   
arr = np.linspace(0, a, b)

print(arr)

# 6

import numpy as np

rolls = int(input("Enter the number of dice rolls\n"))

print("Enter the value of each dice roll")

list_roll = []
for roll in range(rolls):
    each_roll = int(input())
    list_roll.append(each_roll)

dice_rolls = np.array(list_roll)

count_more_than_two = np.sum(dice_rolls > 2)

print("Dice rolls greater than 2")
print(count_more_than_two)

# 7
import numpy as np

size = int(input("Enter the size of 1-D array\n"))

arr_1d = np.arange(size)
print("1-D Array")
print(arr_1d)

m = int(input("Enter m value\n"))
n = int(input("Enter n value\n"))

arr_2d = np.reshape(arr_1d,(m,n))
print("2-D Array")
print(arr_2d)

# 8
import numpy as np

size_1st = int(input("Enter the size of 1st array\n"))

list_element_1st = []
print("Enter the elements of first array")
for size in range(size_1st):
    element_1st = float(input())
    list_element_1st.append(element_1st)

size_2nd = int(input("Enter the size of 2nd array\n"))

list_element_2nd = []
print("Enter the elements of second array\n")
for size in range(size_2nd):
    element_2nd = float(input())
    list_element_2nd.append(element_2nd)

arr_1 = np.array(list_element_1st)
arr_2 = np.array(list_element_2nd)

union_array = np.union1d(arr_1, arr_2)
intersection_array = np.intersect1d(arr_1,arr_2)
difference_array = np.setdiff1d(arr_1, arr_2)

print("Union Array")
print(union_array)

print("Intersection Array")
print(intersection_array)

print("Difference Array")
print(difference_array)

