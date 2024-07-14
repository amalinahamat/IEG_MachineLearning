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

number = input("").split(" ")

list_number = []
for num in number:
    list_number.append(int(num))

mean = np.mean(list_number)

print(mean)


# 4

# Your task is to create a Python program that calculates 
# the correlation between two given arrays using the NumPy library.
# Hence, we try to find a linear function that predicts the response value (y) 
# as accurately as possible as a function of the feature or independent variable (x).
# Prerequisites for Simple Linear Regression:
# Mean of the feature points.
# Standard Deviation.
# Correlation between X and Y.
# Use the NumPy Library for calculations
import numpy as np
first_number = input("").split(" ")

list_first = []
for num in first_number:
    list_first.append(int(num))

second_number = input("").split(" ")
list_second = []
for num in second_number:
    list_second.append(int(num))

correlation_coef = np.corrcoef(list_first, list_second)[0, 1]

print(round(correlation_coef, 2))


# 5
# Simple linear regression is an approach for predicting a response using a single feature.
# It is assumed that the two variables are linearly related. Hence, we try to find a linear function that predicts 
# the response value(y) as accurately as possible as a function of the feature or independent variable(x).
# The following are the prerequisite values.
# 1) Mean of the feature points.
# 2) Standard Deviation.
# 3) Correlation between X and Y.
# y = bx + A -----------------> Line equation using slope.
# where, b is the slope, and A is the intercept.
# Now lets suppose,
# MX - Mean of X
# MY - Mean of Y
# SX - Standard Deviation of X
# SY - Standard Deviation of Y
# r - Correlation between X and Y
# Using these values we have to find the slope(b) and intercept(A).
# The slope (b) can be calculated as follows:
# b = r * SY/SX
# and the intercept (A) can be calculated as
# A = MY - b*MX
import numpy as np

x_number = input("").split(" ")
y_number = input("").split(" ")

list_x = []
for x in x_number:
    list_x.append(float(x))

list_y = []
for y in y_number:
    list_y.append(float(y))

x = np.array(list_x)
y = np.array(list_y)

mean_x = np.mean(x)
mean_y = np.mean(y)

std_x = np.std(x)
std_y = np.std(y)

correlation_coef = np.corrcoef(x,y)[0,1]

m = correlation_coef * (std_y/std_x)
c = mean_y - m * mean_x

print(f"Mean of x = {mean_x}")
print(f"Mean of y = {mean_y}")
print(f"SD of x = {round(std_x, 3)}")
print(f"SD of y = {round(std_y, 3)}")
print(f"Correlation of x and y = {round(correlation_coef, 3)}")
print(f"Scope = {round(m, 3)}")
print(f"Intercept = {round(c, 3)}")


# i Assess

# 1
# Find Correlation Cofficient
# For a given covariance, variance of x and y, find the correlation cofficient(r).
# Input Format:
# First line of the input corresponds to the Covariance.
# Second line of the input corresponds to the variance of x.
# Third line of the input corresponds to the variance of y.
# Output Format:
# Output is an float value corresponds to the correlation cofficient(r).
# Sample Input
# -1.05
# 250.25
# 320.26
# Sample Output
# -0.004

covariance = float(input())
variance_x = float(input())
variance_y = float(input())

correlation_coef = covariance / ((variance_x ** 0.5) * (variance_y ** 0.5))

print(round(correlation_coef, 3))


# 2
# Current Task:
# In this problem, find the standard deviation of a given array.
# Note: Use the NumPy Library for calculations.
# Input Format:
# The input is a single line containing space-separated integers.
# Output Format:
# The output is a single float value representing the standard deviation of the given array. Round it off to 2 decimal places using round method.
# Sample Input:
# 3 4 5 6
# Sample Output:
# 1.12

import numpy as np

input_user = input("").split(" ")

list_number = []
for num in input_user:
    list_number.append(float(num))

std_dev = np.std(list_number)

print(round(std_dev, 2))











