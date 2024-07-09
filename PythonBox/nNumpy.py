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

