# 1
import numpy as np
from scipy.special import exp10, sindg, cosdg

# Input the exponent value
exponent = float(input("Enter the exponent value:\n"))
    
# Calculate 10 raised to the power of the exponent
result_exp10 = exp10(exponent)
print(f"10 raised to the power of {exponent} : {result_exp10}")
    
# Input the angle in degrees
angle_deg = float(input("Enter the angle in degrees:\n"))
    
# Calculate sine and cosine of the angle in degrees
sine_value = sindg(angle_deg)
cosine_value = cosdg(angle_deg)
    
print(f"Sine of {angle_deg} degrees: {sine_value}")
print(f"Cosine of {angle_deg} degrees: {cosine_value}")