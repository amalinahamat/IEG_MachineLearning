
# 1
# Write a Python program that does the following:
# Prompts the user to enter two numbers. Stores these numbers in two variables. 
# Performs and prints the results of addition, subtraction, multiplication, and 
# division of these two numbers.

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

addition = int(first_number) + int(second_number)
print(addition)

subtraction = int(first_number) - int(second_number)
print(subtraction)

multiplication  = int(first_number) * int(second_number)
print(multiplication)

division =  int(first_number) / int(second_number)
print("%.2f"%division)

# 2
# Write a Python program that:
# Prompts the user to enter a temperature in Celsius. Converts the temperature
# to Fahrenheit. Prints the temperature in Fahrenheit. (Hint: The formula to convert 
# Celsius to Fahrenheit is: F = C * 9/5 + 32)

temperature_celsius = input("Enter a temperature in Celsius: ")

convert_celsiusfahrenheit = (float(temperature_celsius) * 9 / 5) + 32

print("Temperature in Fahrenheit : ", "%.2f"%convert_celsiusfahrenheit)

# 3
# Write a Python program that:
# Prompts the user to enter the length and width of a rectangle. Calculates the area 
# and perimeter of the rectangle. Prints the area and perimeter

length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")

area_rectangle = int(length) * int(width)
perimeter_rectangle =  (2 * int(length)) + (2 * int(width))

print("Area of rectangle: ", area_rectangle)
print("Perimeter of rectangle: ", perimeter_rectangle)


# 4
# Write a Python program that:
# Prompts the user to enter the principal amount, rate of interest, and time in years. 
# Calculates the simple interest. Prints the simple interest. (Hint: The formula to 
# calculate simple interest is: SI = (P * R * T) / 100)

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time_in_years = float(input("Enter the time in years: "))

sample_interest = (principal_amount * rate_of_interest * time_in_years) / 100
print("Sample interest: ", "%.2f"%sample_interest)


# 5
# Write a Python program that:
# Prompts the user to enter two numbers. Swaps the values of the two variables. 
# Prints the values before and after swapping.

first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))

print("\nfirst and second number before swapping: ", first_number, second_number)

x = second_number
second_number = first_number
first_number = x

print("\nfirst and second number after swapping: ", first_number, second_number)


# 6
# Write a Python program that:
# Prompts the user to enter a number. Calculates the square and cube of the number. 
# Prints the square and cube.

number = int(input("Enter a number: "))

# ** is the power operator
square_number = number ** 2
cube_number = number ** 3

print("square of the number: ", square_number, "\ncube of the number: ", cube_number)

# 7
# Write a Python program that:
# Prompts the user to enter their weight in kilograms and height in meters. Calculates 
# the Body Mass Index (BMI). Prints the BMI. (Hint: The formula to calculate BMI is: 
# BMI = weight / (height * height))

weight = float(input("Enter your weight in kilogram: "))
height = float(input("Enter your weight in meters: "))

body_mass_index = weight / (height * height)
print("Body Mass Index: ", "%.2f"%body_mass_index)

# 8
# Write a Python program that:
# Prompts the user to enter the principal amount, rate of interest, time in years, and 
# number of times interest is compounded per year. Calculates the compound interest. 
# Prints the compound interest.
# A=P(1+R/100n)nt where A is the amount, P is the principal amount, R is the annual interest 
# rate, t is the time the money is invested for, and n is the number of times interest is 
# compounded per year)

principal_amount = float(input("Enter a principal amount: "))
rate_of_interest = float(input("Enter a rate of interest: "))
time_in_years = float(input("Enter a time in years: "))
number_of_times_interest = float(input("Enter a number of times interest is compounded per year: "))

compound_interest = principal_amount * ((1 + rate_of_interest) / (100 * (number_of_times_interest))) * number_of_times_interest * time_in_years

print("Compound interest: ", "%.2f"%compound_interest)

# 9
# Write a Python program that:
# Converts the given integer 97409 to its binary representation. Prints the binary representation.

integer = 97409

remainder1 = integer % 2
division1 = integer // 2
print(remainder1, division1)

remainder2 = division1 % 2
division2 = division1 // 2
print(remainder2, division2)

remainder3 = division2 % 2
division3 = division2 // 2
print(remainder3, division3)

remainder4 = division3 % 2
division4 = division3 // 2
print(remainder4, division4)

remainder5 = division4 % 2
division5 = division4 // 2
print(remainder5, division5)

remainder6 = division5 % 2
division6 = division5 // 2
print(remainder6, division6)

remainder7 = division6 % 2
division7 = division6 // 2
print(remainder7, division7)

remainder8 = division7 % 2
division8 = division7 // 2
print(remainder8, division8)

remainder9 = division8 % 2
division9 = division8 // 2
print(remainder9, division9)

remainder10 = division9 % 2
division10 = division9 // 2
print(remainder10, division10)

remainder11 = division10 % 2
division11 = division10 // 2
print(remainder11, division11)

remainder12 =  division11 % 2
division12 = division11 // 2
print(remainder12, division12)

remainder13 = division12 % 2
division13 = division12 // 2
print(remainder13, division13)

remainder14 = division13 % 2
division14 = division13 // 2
print(remainder14, division14)

remainder15 = division14 % 2
division15 = division14 // 2
print(remainder15, division15)

remainder16 = division15 % 2
division16 = division15 // 2
print(remainder16, division16)

remainder17 = division16 % 2
division17 = division16 // 2
print(remainder17, division17)

print("binary representation: ", remainder17, remainder16,
      remainder15, remainder14, remainder13, remainder12,
      remainder11, remainder10, remainder9, remainder8,
      remainder7, remainder6, remainder5, remainder4,
      remainder3, remainder2, remainder1)


# or , another solution


quotient = 97409

remainder = str(quotient % 2)
quotient  = quotient // 2
print(str(remainder), quotient)

result = str(remainder)
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(
remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
#print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print("binary representation: ",result)


# 10
# Write a Python program that:
# Converts the given binary 1011 to its decimal representation. 
# Prints the decimal representation.

binary = 1011

division1 = (binary // 1000 ) * (2 ** 3)
print(division1)
division2 = ((binary // 100) % 10) * (2 ** 2)
print(division2)
division3 = ((binary // 10) % 100) * (2 ** 1)
print(division3)
division4 = (binary % 10) * (2 ** 0)
print(division4)

decimal = division1 + division2 + division3 + division4
print("Decimal representation: ", decimal)

# or , another solution

number = 1011

result = ( number % 10 ) * (2 ** 0)
quotient = number // 10
print(result, quotient)

result = result + ((quotient % 10) * (2 ** 1))
quotient = quotient // 10
print(result, quotient)

result = result + ((quotient % 10) * (2 ** 2))
quotient = quotient // 10
print(result, quotient)

result = result + ((quotient % 10) * (2 ** 3))
quotient = quotient // 10
print(result, quotient)





