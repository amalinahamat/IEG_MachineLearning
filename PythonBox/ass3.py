# 1
# Coming Sunday, he has to create a 20-liter solution that is 35% salt by mixing two available solutions.
# One solution (A) is 25% salt, and the other solution (B) is 50% salt. How many liters of each solution 
# are required to achieve the desired concentration?
# Coming Monday, he has to create an 8-liter solution that is 25% sugar by mixing two available solutions. 
# One solution (A) is 15% sugar, and the other solution (B) is 40% sugar. How many liters of each solution 
# are required to achieve the desired concentration?
# Write a simple, generic Python program to assist the laboratory technician. The program must take all 
# these numbers (20 liters, 35, 25, 50) as input and calculate the required liters of each solution and print them. 
# Please note that the same program must work for the second problem as well (8 liters, 25, 15, 40).
# The maximum stock for solution (A) and solution (B) is always 3 liter only. After calculating/printing the 
# required quantity of A and B, throw proper message. For example, required quantity of 
# solution (A) is less than 3 liter say "Solution (A) is available can proceed". If required quantity of 
# solution (B) is greater than 3 liter say "Solution (B) is not available, please order 1.3 liter now".
total_solution = int(input("Enter a total liter of solution (liters): "))
total_salt = float(input("Enter a percentage of total salt: "))
total_salt /= 100
salt_a = float(input("Enter a percentage of salt a: "))
salt_a /= 100
salt_b = float(input("Enter a percentage of salt b: "))
salt_b /= 100

solution_a = ((salt_b * total_solution) - (total_salt * total_solution)) / (salt_b - salt_a)
solution_b = (total_solution - solution_a)

print(f"solution a : {solution_a:.2f}, solution b : {solution_b:.2f}")

max_solution = 3

if(solution_a < max_solution and solution_b < max_solution):
    print("Solution (A) and Solution(B) is available can proceed.")
elif(solution_a  < max_solution and solution_b > max_solution):
    solution_b = solution_b - max_solution
    print(f"Only Solution (A) is available , please order {solution_b:.2f} liter now.")
elif(solution_a > max_solution and solution_b < max_solution):
    solution_a = solution_a - max_solution
    print(f"Only Solution (B) is available ,please order {solution_a:.2f} liter now.")
else:
    solution_a = solution_a - max_solution
    solution_b = solution_b - max_solution
    print(f"Solution (A) and Solution(B) is not available, please order solution A {solution_a:.2f} liter and solution b {solution_b:.2f} liter now.")


# 2
# Initialize two variables, x = 0b10101100 and y = 0b11011001.
# Write Python code to:
# Extract the lower 4 bits from x.
# Check if y is even or odd.
# Clear the upper 4 bits of x.
# Check if the 5th bit of y is set.
x = 0b10101100
y = 0b11011001

# 1.
mask_a = 0b00001111

print(f"1. extraction : {bin(x & mask_a)}")

# 2.

mask_b = 0b00000001

if(y & mask_b == 0):
    print("2. y is even number")
else:
    print("2. y is odd number")

# 3.
mask_c = 0b00001111

print(f"3. clearance: {bin(x & mask_c)}")

# 4.

mask_d = 0b00010000

#print(bin(y & mask_c))

if(y & mask_d != 0):
    print("4. 5th at y is set")
else:
    print("4. 5th at y is not set")

# 3
# A construction project requires two workers to complete. Worker A can complete the project in 12 hours, 
# while Worker B can complete the same project in 16 hours. How long will it take for both workers 
# to complete the project if they work together?
# Another project requires Worker C, who can complete it in 8 hours, and Worker D, who can complete it in 10 hours.
# How long will it take for both workers to complete this project if they work together?
# Write a simple, generic Python program to assist in calculating the time required for two workers to complete a 
# project when working together. The program must take all these numbers (12, 16) as input and calculate the required time. 
# Finally, print the result. Please note that the same program must work for the second problem as well (8, 10).
# 1/work_rate = 1/workera + 1/workerb
worker_a = int(input("Enter an hours complete by worker A: "))
worker_b = int(input("Enter an hours complete by worker B:  "))

work_rate = (worker_a * worker_b) / (worker_a + worker_b)

print(f"times for both workers to complete the project: {work_rate:.2f}")


# 4
# Initialize two variables, a = 0b10101000 and b = 0b01010100.
# Write Python code to:
# Set the lower 4 bits of a.
# Combine the bits of a and b using OR.
# Create a mask to set the 2nd and 6th bits of a.
a = 0b10101000
b = 0b01010100

# 1.
mask_a = 0b00001111
print(f"1. {bin(a | mask_a)}")

# 2.
print(f"2. {bin(a | b)}")

# 3.

mask_b = 0b10001010
print(f"3. {bin(a ^ mask_b)}")

# 5
# An investor decides to invest a total of RM30,000 in two different accounts.
# The first account offers a 5% annual interest rate, while the second account offers a 7% annual interest rate. 
# If the total annual interest earned is RM1,800, how much money was invested in each account?
# Another investor decides to invest a total of RM50,000 in two different accounts. 
# The first account offers a 3% annual interest rate, while the second account offers a 6% annual interest rate. 
# If the total annual interest earned is RM2,400, how much money was invested in each account?
# Write a simple, generic Python program to assist in calculating the amount of money invested in each account 
# to achieve the desired total annual interest. The program must take all these numbers (30000, 5, 7, 1800)
# as input and calculate the required amounts. Finally, print the result. 
# Please note that the same program must work for the second problem as well (50000, 3, 6, 2400).
total_money = float(input("Enter a number of total invest amount: "))
interest_rate_a = float(input("Enter a percentage of interest rate first account: "))
interest_rate_b = float(input("Enter a percentage of interest rate second account: "))
total_interest = float(input("Enter a number of total interest amount: "))

interest_rate_a = interest_rate_a / 100
interest_rate_b = interest_rate_b / 100


second_account = (total_interest - (total_money * interest_rate_a)) / (interest_rate_b - interest_rate_a)
first_account = (total_money - second_account)

print(f"first account invest:RM{first_account:.2f}\nsecond account invest:RM{second_account:.2f}")

# 6
# Initialize two variables, x = 0b10101100 and y = 0b11010010.
# Write Python code to:
# Swap the values of x and y without using a temporary variable.
# Toggle the 3rd and 5th bits of x.
# Check if two given numbers a = 29 and b = 15 are different.
x = 0b10101100
y = 0b11010010

print("1.")
print(f"value x before swap: {bin(x)}")
print(f"value y before swap: {bin(y)}")
x = x ^ y # 01111110
y = x ^ y # 10101100
x = x ^ y # 11010010
print(f"value x after swap: {bin(x)}")
print(f"value y after swap: {bin(y)}")

print("\n2.")
x = 0b10101100
mask = 0b00010100
x_toggle = x ^ mask

print(f"x : {bin(x)}\ntoggle 3rd and 5th, x : {bin(x_toggle)}")

print("\n3.")
a = 29
b = 15
print(a != b)




