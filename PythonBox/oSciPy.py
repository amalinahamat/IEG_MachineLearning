# 1
import numpy as np
from scipy.special import exp10, sindg, cosdg

# Input the exponent value
exponent = int(input("Enter the exponent value: \n"))
    
# Calculate 10 raised to the power of the exponent
result_exp10 = exp10(exponent)
print(f"10 raised to the power of {exponent} : {result_exp10}")
    
# Input the angle in degrees
angle_deg = float(input("Enter the angle in degrees: \n"))
    
# Calculate sine and cosine of the angle in degrees
sine_value = sindg(angle_deg)
cosine_value = cosdg(angle_deg)
    
print(f"Sine of {angle_deg} degrees: {sine_value}")
print(f"Cosine of {angle_deg} degrees: {cosine_value}")

# 2

import numpy as np
from scipy.stats import linregress

x_= input("Enter the values of x separated by spaces: ")
y_ = input("Enter the values of y separated by spaces: ")

x = np.array([float(number) for number in x_.split()])
y = np.array([float(number) for number in y_.split()])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Calculate R-squared value
r_squared = r_value ** 2

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_squared}")
print(f"p-value: {p_value}")
print(f"Standard error: {std_err}")   
