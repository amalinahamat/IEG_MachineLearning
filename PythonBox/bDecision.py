# idesign (decision and flow control)

# 1
# Based on this, the visitors whose ticket number has the last digit as 3 or 8, are declared as lucky winners and attracting prizes are awaiting to be presented for them.
# Write a program to find if the last digit of the ticket number of visitors is 3 or 8.
# Input Format:
# First line of the input is an integer that corresponds to the ticket number.

# Output Format:
# Output should display as "Lucky Winner" if the last digit of the ticket number is 3 or 8. Otherwise print "Not a Lucky Winner".
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# 43
# Sample Output 1:
# Lucky Winner
# Sample Input 2:
# 41
# Sample Output 2:
# Not a Lucky Winner

digits = (input("Enter the digit of your ticket number: "))

reverse_digits = (digits)[::-1]
print(reverse_digits)

print(reverse_digits[0])

if reverse_digits[0] == "3" or reverse_digits[0] == "8":
    print("Lucky Winner")
else:
    print("Not a Lucky Winner")


# 2
# There are 5 types of tickets, each of which is denoted by a character (both upper case and lower case). Please find the equivalent strings for the characters.
# E or e - Early Bird Ticket
# D or d - Discount Ticket
# V or v - VIP Ticket
# S or s - Standard Ticket
# C or c - Child Ticket
# Write a piece of code for the scanning machine that will take the input of a character and print the equivalent string as given.
# Input Format:
# The first line of the input is one of the character that denotes one of ticket types.

# Output Format:
# Output should display the equivalent ticket type of the character.
# Refer sample input and output for formatting specifications.

# Sample Input 1:
# e

# Sample Output 1:
# Early Bird Ticket

# Sample Input 2:
# S

# Sample Output 2:
# Standard Ticket

ticket = str(input(""))

if ticket == "E" or ticket == "e":
    print("Early Bird Ticket")
elif ticket == "D" or ticket == "d":
    print("Discount Ticket")
elif ticket == "V" or ticket == "v":
    print("VIP Ticket")
elif ticket == "S" or ticket == "s":
    print("Standard Ticket")
elif ticket == "C" or ticket == "c":
    print("Child Ticket")
else:
    print("")


# 3
# Write a program to help the Organizers to create the portal as per the requirement given below.
# Given the ticket cost as 'X'.
# If the number of tickets purchased is less than 50, there is no discount.
# If the number of tickets purchased is between 50 and 100 (both inclusive), then 10% discount is offered.
# If the number of tickets purchased is between 101 and 200(both inclusive), 20% discount is offered.
# If the number of tickets purchased is between 201 and 400(both inclusive), 30% discount is offered.
# If the number of tickets purchased is between 401 and 500(both inclusive), 40% discount is offered.
# If the number of tickets purchased is greater than 500, then 50% discount is offered.
# Input Format:
# First line of the input is an integer that corresponds to the cost of the ticket ‘X’.
# Second line of the input is an integer that corresponds to the number of tickets purchased.
# Output Format:
# Output should display a double value, which gives the total expenses in purchasing the tickets after discounts. Display the output correct to 2 decimal places.
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# 100
# 5
# Sample Output 1:
# 500.00
# Sample Input 2:
# 100
# 300
# Sample Output 2:
# 21000.00


cost = float(input())
number_ticket = int(input())

if number_ticket < 50:
    print(f"{cost * number_ticket :.2f}")
elif number_ticket >= 50 and number_ticket <= 100:
    print(f"{cost * number_ticket * 0.9 :.2f}")
elif number_ticket >= 101 and number_ticket <= 200:
    print(f"{cost * number_ticket * 0.8 :.2f}")
elif number_ticket >= 201 and number_ticket <= 400:
    print(f"{cost * number_ticket * 0.7 :.2f}")
elif number_ticket >= 401 and number_ticket <= 500:
    print(f"{cost * number_ticket * 0.6 :.2f}")
else:
    print(f"{cost * number_ticket * 0.5 :.2f}")


# 4
# If his basic salary is less than Rs. 15000, then HRA = 15% of basic salary and DA = 90% of basic salary.
# If his basic salary is either equal to or above Rs. 15000, then HRA = Rs. 5000 and DA = 98% of basic salary.
# If the Danny’s salary is given as input, write a program to find his gross salary.
# Note : Gross Salary = Basic Salary+HRA+DA 
# Input Format:
# First line of the input is an integer that corresponds to the basic salary of Danny.
# Output Format:
# Output should display the double value that refers to the gross salary of Danny. Display the output correct to 2 decimal places.
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# 12000
# Sample Output 1:
# 24600.00
# Sample Input 2:
# 30000
# Sample Output 2:
# 64400.00

basic_salary = float(input())

if basic_salary < 15000:
    HRA = 0.15 * basic_salary
    DA = 0.9 * basic_salary
else:
    HRA = 5000
    DA = 0.98 * basic_salary

print(f"{basic_salary + HRA + DA :.2F}")



# 5
# Hurl Factor must be greater than 50.
# Spin Factor must be greater than 60.
# Speed factor must be greater than 100.

# The grades are as follows:
# Grade is 10 if all three conditions are met.
# Grade is 9 if conditions (i) and (ii) are met.
# Grade is 8 if conditions (ii) and (iii) are met.
# Grade is 7 if conditions (i) and (iii) are met.
# Garde is 6 if only one condition is met.
# Grade is 5 if none of three conditions are met.
# Write a program display the grade of the rides, given the values of hurl factor, spin factor and speed factor of the ride under consideration.
# Input Format:
# First line of the input consists of 3 integers that gives the Hurl Factor, Spin Factor and Speed Factor of the ride, each separated by a space.
# Output Format:
# Output should display the grade of the ride depending on Conditions.
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# 51 89 150
# Sample Output 1:
# 10
# Sample Input 2:
# 45 69 102
# Sample Output 2:
# 8


factors = (input())
print(type(factors))

factor = factors.split(" ")
print(factor)
print(type(factor))

if int(factor[0]) > 50 and int(factor[1]) > 60 and int(factor[2]) > 100:
    print("10")
elif int(factor[0]) > 50 and int(factor[1]) > 60:
    print("9")
elif int(factor[1]) > 60 and int(factor[2]) > 100:
    print("8")
elif int(factor[0]) > 50 and int(factor[2]) > 100:
    print("7")
elif int(factor[0]) > 50 or int(factor[1]) > 60 or int(factor[2]) > 100:
    print("6")
else:
    print("5")

'''    
def change(a):
    b=[x*x for x in a]
    print(b)
'''

# iAsses
# The game’s rules are:
# A player needs to pick 3 cards from a big lot of cards. There are 4 types of Cards namely Spade(S), Heart(H), Club(C) and Diamond (D). If all the 3 cards that the player picks are of the same type and same number, they get a Double Bonanza. If all the 3 cards are of the same type or if they all have the same number, they get a Bonanza. Otherwise they do not get a Bonanza. Alan has now picked 3 cards and is awaiting to know if he has got a bonanza. Please help him to know if he has won the Bonanza or not.
# Input Format:
# There are 3 lines of input.
# Each of the line consists of character and integer input, which corresponds to the type of the card and the number in it that Alan picked. The type of card and the number are separated by a single space.

# Output Format:
# Output should display "Double Bonanza" or "Bonanza" or "No Bonanza" based on the conditions given.
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# S 5
# S 5
# S 5
# Sample Output 1:
# Double Bonanza
# Sample Input 2:
# S 6
# S 5
# H 5
# Sample Output 2:
# No Bonanza

card_ones = input()
card_twos = input()
card_threes = input()

card_one = card_ones.split(" ")
card_two = card_twos.split(" ")
card_three = card_threes.split(" ")

if card_one == card_two == card_three:
    print("Double Bonanza")
elif card_one[0] == card_two[0] == card_three[0] or card_one[1] == card_two[1] == card_three[1] :
    print("Bonanza")
else:
    print("No Bonanza")

