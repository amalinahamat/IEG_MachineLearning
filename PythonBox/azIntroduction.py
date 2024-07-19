age = 30
print(age)

age = 40
print(age)

maths_operation = 3 + 2 * 4 / 2 - 2
print(maths_operation)

maths_operation = 3 + 2 * 4 // 2 - 2
print(maths_operation)

float_operation = 12 / 3
print(float_operation)

integer_operation = 12 // 3
print(integer_operation)

float_operation = 8 / 3
print(float_operation)

integer_operation = 8 // 3
print(integer_operation)

reminder = 13 % 5
print(reminder)

x = 37
reminder = 37 % 2
print(reminder)


string_with_quotes = "Hello, it's me."
another_with_quotes = 'He said "You are amazing" yesterday'
another_with_same = "He said \"You are amazing\" yesterday"

print(string_with_quotes)
print(another_with_quotes)
print(another_with_same)


"""" 
this is my coding for learning process
"""

multiline = """

Aku bukanlah superman
Aku juga bisa nangis
Jika kekasih hatiku
Pergi meninggalkan aku

"""
print(multiline)


name = "Amal"
greet = "hi, " + name
print(greet)

age = "34"
print("You are, " + age)

age = 34
age_str = str(age)
print("You are " + age_str)


age = 34
print(f"You are {age}")

name = "amal"
greet = f"How are you , {name}"
print(greet)


answer = 5 * 5 + 10 / 2 * 7 - 3
print(answer)

answer = 5 * 5 + 10 // 2 * 7 - 3
print(answer)

#===

name = "Amal"
final_greet = "How are you, {}?"
amal_greet = final_greet.format(name)
print(amal_greet)

name = "Lia"
lia_greet = final_greet.format(name)
print(lia_greet)

my_name = "Amal"
your_name = input("Enter your name : ")
print(f"Hello {your_name}. My name is {my_name}") 

#===

age = input("Enter your age : ")
age_int = int(age)
print(f"You have live for {age_int * 12} months.") 

age = int(input("Enter your age: "))
print(f"You have lived for {age * 12} months.")

age = int(input("Enter you age: "))
month = age * 12
print(f"You have lived for {month} months")

#====

age = int(input("Enter your age: "))
can_learn_program = age > 0 and age < 150

print(f"You can learn programming : {can_learn_program}")

age =  int(input("Enter your age: "))
not_working = age < 18 or age > 65
print(f"At {age}, you are usually not working: {not_working}")


age = int(input("Enter your age: "))
working = age >= 18 and age <= 65
print(f"At {age}, you are usually working: {working}")

print(bool(35))
print(bool("Amal"))
print(bool(0))
print(bool(""))

x = True or False
print(f"{x}, {bool(x)}")

y = True and False
print(f"{y}, {bool(y)}")

m = 35 or 0
print(f"{m}, {bool(m)}")

n = 35 and 0
print(f"{n}, {bool(n)}")

name = (input("Enter your name: "))
surname = (input("Enter your surname: "))
greet = name or surname
print(greet)

print(not 35)

ages = 20
over_age = ages >= 18
under_Age = ages < 18
same_age = ages == 20
print (f"You are {ages}")


my_number = 9
user_number = int(input("Enter your number: "))
matches = my_number == user_number
print(f"You got it right: {matches}")  


# 7 Idesign

# 3
# The program should get the branding expenses, travel expenses, food expenses and logistics expenses as input from the user and calculate the total expenses for an event and the percentage rate of each of these expenses.
# First input is a int value that corresponds to the branding expenses.
# Second input is a int value that corresponds to the travel expenses.
# Third input is a int value that corresponds to the food expenses.
# Fourth input is a int value that corresponds to the logistics expenses.

# Output Format:
# First line of the output should display the float value that corresponds to the total expenses for the Event.
# Next four lines should display the percentage rate of each of the expenses.
# Refer sample input and output for formatting specifications.

# Sample Input and Output:
# Enter branding expenses
# 20000
# Enter travel expenses
# 40000
# Enter food expenses
# 15000
# Enter logistics expenses
# 25000
# Total expenses : Rs.100000.00
# Branding expenses percentage : 20.00%
# Travel expenses percentage : 40.00%
# Food expenses percentage : 15.00%
# Logistics expenses percentage : 25.00% 


branding_exp = int(input("Enter branding expenses\n"))
travel_exp = int(input("Enter travel expenses\n"))
food_exp = int(input("Enter food expenses\n"))
logistic_exp = int(input("Enter logistics expenses\n"))

total_exp = branding_exp + travel_exp + food_exp + logistic_exp
print("Total expenses : Rs.%.2f"%total_exp)

percent_branding_exp = branding_exp / total_exp 
print(f"Branding expenses percentage : {percent_branding_exp:.2%}")
percent_travel_exp = travel_exp / total_exp 
print(f"Travel expenses percentage : {percent_travel_exp:.2%}")
percent_food_exp = food_exp / total_exp 
print(f"Food expenses percentage : {percent_food_exp:.2%}")
percent_logistic_exp = logistic_exp / total_exp
print(f"Logistics expenses percentage : {percent_logistic_exp:.2%}")


# 4
# She sold 'X' more adult tickets than children tickets and she sold twice as many senior tickets as children tickets. Assume that an adult ticket costs $5, children ticket costs $2 and senior ticket costs $3.
# Suzanne made 'Y' dollars from ticket sales. Find the number of adult tickets, children tickets, and senior tickets sold.

 
# Input Format:
# The first input is an integer value X that corresponds to the number of adult tickets more than children tickets.
# The second input is an integer value Y that corresponds to the money in dollars made by Suzanne from ticket sales.

# Output Format:
# The first line of the output should display the number of children tickets sold.
# The second line of the output should display the number of adult tickets sold.
# The third line of the output should display the number of senior tickets sold.
# Refer sample input and output for formatting specifications.
# [All text in bold corresponds to input and rest corresponds to output.]

# Sample Input and Output :
# Enter the value of X
# 10
# Enter the value of Y
# 700
# Number of children tickets sold : 50
# Number of adult tickets sold : 60
# Number of senior tickets sold : 100

x = int(input("Enter the value of X\n"))
y = int(input("Enter the value of Y\n"))

children = ( y  -   (5 * x ))  // 13
adult = children + x
senior = 2 * children
y = (5*adult) + (2 * children) + (3 * senior)

print(f"Number of children tickets sold : {children}")
print(f"Number of adult tickets sold : {adult}")
print(f"Number of senior tickets sold : {senior}")

# 5
# the tile game where the kids were given 'n' square tiles of the same size and were asked to form the largest possible square using those tiles.

# Help the kids by writing a program to find the area of the largest possible square that can be formed, given the side of a square tile (in cms) and the number of square tiles available.

# Input Format:
# First line of the input is an integer that corresponds to the side of a square tile (in cms).
# Second line of the input is an integer that corresponds to the number of square tiles available.

# Output Format:
# Output should display the area of the largest possible square that can be formed (in square cms) with the available tiles.
# Refer sample input and output for formatting specifications.
# [All text in bold corresponds to input and rest corresponds to output.]

# Sample Input and Output :
# Enter the side in cm of a square tile
# 5
# Enter the number of square tiles available
# 8
# Area of the largest possible square is 100sqcm

side = float(input("Enter the side in cm of a square tile\n"))
number_tiles  = int(input("Enter the number of square tiles available\n"))

max_side_length = int(number_tiles ** 0.5)
largest_area = (side * max_side_length) ** 2

print(f"Area of the largest possible square is {int(largest_area)}sqcm")

# 6
# Weekdays --- 80 / hour
# Weekends --- 50 / hour

# Justin is a part-time employee working at the fair. Number of hours Justin has worked in the weekdays is 10 more than the number of hours he had worked during weekends. If the total salary paid to him in this month is known, write a program to estimate the number of hours he had worked during weekdays and the number of hours he had worked during weekends.

# Input Format:
# First line of the input is a double value that corresponds to the total salary paid to Justin.

# Output Format:
# First line of the output should display the number of hours Justin has worked during the weekdays.
# Second line of the output should display the number of hours Justin has worked during the weekends.
# Refer sample input and output for formatting specifications.
# [All text in bold corresponds to input and rest corresponds to output.]

# Sample Input and Output:
# Enter the total salary paid
# 2750
# Number of weekday hours is 25
# Number of weekend hours is 15

total_salary = int(input("Enter the total salary paid\n"))

weekend_rate = 50
weekday_rate = 80

# total_salary = (weekday_rate * weekday_hour) + (weekend_rate * weekend_hour)
weekend_hour = int((total_salary - 800 ) / 130)
weekday_hour = int(10 + weekend_hour)

print(f"Number of weekday hours is {weekday_hour}")
print(f"Number of weekend hours is {weekend_hour}")


# 7
# Write a program to accept strings as command line 
# argument and print the number of arguments entered.
# Sample Input (Command Line Argument) 1:
# Command Arguments

# Sample Output 1:
# Arguments :
# Command
# Arguments
# Number of arguments is 2

# Sample Input (Command Line Argument) 1:
# Commands

# Sample Output 2:
# Arguments :
# Commands
# Number of arguments is 1

import sys
arguments = sys.argv

print("Arguments :")
for argument in arguments[1:]:
    print(argument)

print(f"Number of arguments is {len(arguments) - 1} ")



# iAssess
# 1
# the audience were requested to give their feedback in a scale of 1 to 10. Number of people who watched each show and the average feedback rating of each show is known. Write a program to find the average feedback rating of the WonderWorks Magic show.
# First line of the input is an integer value that corresponds to the number of people who watched show 1.
# Second line of the input is a float value that corresponds to the average rating of show 1.
# Third line of the input is an integer value that corresponds to the number of people who watched show 2.
# Fourth line of the input is a float value that corresponds to the average rating of show 2.
# Fifth line of the input is an integer value that corresponds to the number of people who watched show 3.
# Sixth line of the input is a float value that corresponds to the average rating of show 3.
# Output Format:
# Output should display the overall average rating for the show. Display the rating correct to 2 decimal places.
# Refer sample input and output for formatting specifications.
# [All text in bold corresponds to input and rest corresponds to output.]

# Sample Input and Output:
# Enter the number of people who watched show 1
# 400
# Enter the average rating for show 1
# 9.8
# Enter the number of people who watched show 2
# 500
# Enter the average rating for show 2
# 9.6
# Enter the number of people who watched show 3
# 100
# Enter the average rating for show 3
# 5
# The overall average rating for the show is 9.22
    
show_1 = int(input("Enter the number of people who watched show 1\n"))
average_show_1 = float(input("Enter the average rating for show 1\n"))

show_2 = int(input("Enter the number of people who watched show 2\n"))
average_show_2 = float(input("Enter the average rating for show 2\n"))

show_3 = int(input("Enter the number of people who watched show 3\n"))
average_show_3 = float(input("Enter the average rating for show 3\n"))

total_average_show = ((show_1 * average_show_1) + (show_2 * average_show_2) + (show_3 * average_show_3)) / (show_1 + show_2 + show_3)
print(f"The overall average rating for show is {total_average_show:.2f}")
 