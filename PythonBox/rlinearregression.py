# i design

# 1
# Finding covariance
# Create two lists consists of integers,each of size 5 and then find the covariance and print.
# Input format:
# First 5 lines of input corresponds to elements of list 1.
# Next 5 lines of input corresponds to elements of list 2.
# Output format:
# Output corresponds to covariance between lists.
# Sample Input:
# 6 5 3 9 1 0 5 9 78 2
# Sample Output:
# 76.2

'''import numpy as np

input_user = input("").split(" ")

list1 = []
for element1 in input_user[0:5]:
    list1.append(int(element1))

list2 = []
for element2 in input_user[5:10]:
    list2.append(int(element2))

covariance_matrix = np.cov(list1, list2, bias = True)

covariance = covariance_matrix[0,1]

print(covariance)
'''

# or correct answer of ebox

'''import numpy as np

# Read input for list 1
first_element  = [int(input()) for element in range(5)]

# Read input for list 2
second_element = [int(input()) for element in range(5)]

# Calculate covariance
covariance = np.cov([first_element, second_element])[0, 1]

# Print covariance rounded to 1 decimal point
print(format(covariance, ".1f"))'''

# 2
# Correlation coefficient - Scattered Data
# To find the correlation coefficient for scattered data. 
# Input Format
# First line of input in an integer n that corresponds to number of points
# Next n line consists of points in the format x,y 
# Output Format 
# Output is a float value with two 2 precision that corresponds to the correlation coefficient of scattered data. 
# Sample Input 
# 3 
# 12,6 
# 13,32 
# 1,7 
# Sample Output 
# Correlation Coefficient: 0.54

import numpy as np
number = int(input())

x = []
y = []

for n in range(number):
    num_x, num_y = input("").split(",")
    x.append(float(num_x))
    y.append(float(num_y))

correlation_coef = np.corrcoef(x, y)[0, 1]

print(f"Correlation Coefficient: {correlation_coef:.2f}")


# 3

# Write a Python program that calculates the mean of a given array using the NumPy library. 
# This is a prerequisite step in the process of performing simple linear regression, 
# which is a statistical approach for modeling the relationship between a dependent variable 
# and a single independent variable.
# Prerequisites for Simple Linear Regression:
# Mean of the feature points.
# Standard Deviation.
# Correlation between X and Y.
# In this problem, find the mean of a given array.
# Note: Use the NumPy Library for calculations

import numpy as np








