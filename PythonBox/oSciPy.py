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

# 3

from scipy.optimize import root
import numpy as np

# Define the equation function
def equation(x):
    return x**3 - 2*x - 5

    # Get initial guess from the user
x0 = float(input("Enter initial guess: "))
    
    # Find the root using scipy.optimize.root
sol = root(equation, x0)
    
    # Print the root
print(f"Root:", sol.x)


# 4

from scipy.integrate import dblquad
import numpy as np

function = input("Enter the function to be integrated in terms of x and y:\n")
min_x = int(input("Enter the lower limit for x:\n"))
max_x = int(input("Enter the upper limit for x:\n"))
min_y = int(input("Enter the lower limit for y:\n"))
max_y = int(input("Enter the upper limit for y:\n"))

funct = lambda y, x: eval(function)

result, error = dblquad(funct, min_x, max_x, lambda x: min_y, lambda x: max_y)

print(f"Result of dblquad integration: {result}")
print(f"Error estimate: {error}")


# i assess
 
# 1

import numpy as np
from scipy.fft import fft, ifft

sequences = input("Enter the sequence (comma-separated values):\n")

for seq in sequences.split(','):
    sequence = np.array(float(seq))

fft_result = fft(sequence)

ifft_result = ifft(fft_result)

print(f"Fourier Transform of the sequence: {fft_result}")
print(f"Inverse Fourier Transform of the transformed sequence: {ifft_result}")

# 1 correct
import numpy as np
from scipy.fft import fft, ifft

# Get input from the user
sequences = input("Enter the sequence (comma-separated values):\n")

# Convert input string to a list of floats
sequence = np.array([float(num) for num in sequences.split(',')])

# Compute the Fourier transform
fft_result = fft(sequence)

# Compute the inverse Fourier transform
ifft_result = ifft(fft_result)

# Print the results
print(f"Fourier Transform of the sequence: {fft_result}")
print(f"Inverse Fourier Transform of the transformed sequence: {ifft_result}")
