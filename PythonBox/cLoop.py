
#idesign

# 1
# The registration is on a first come first serve basis to a maximum of N entries.

# The competition is conducted in two different galleries of the venue.  Just for the ease of their management, the Event organizers have announced to divide the children into two groups, to attend the competition in the two chosen galleries. By that note, all those children who have their registration code as an even number will be put in one gallery and those with odd number will be in another gallery.
# Help the organizers to find count of number of even registration codes and odd registration codes from the total N.

# Note: The registration code need not be unique as each child will have a unique school code.

# Input Format:
# The first line of input consists of a single integer N denoting the number of registration codes issued for the competition.
# The next n lines of input consists of integers, denoting the registration codes of each child.
# Output Format:
# Output a single with the count of even numbers and odd numbers from N, separated by a single space.
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# 3
# 1
# 4
# 10
# Sample Output 1:
# 2 1
# Sample Input 2:
# 5
# 2
# 6
# 23
# 12
# 11
# Sample Output 2:
# 3 2

com_code = int(input())

reg_code = []

for n in range(com_code):
    code = int(input())
    reg_code.append(code)

print(reg_code)

count_even = 0 
count_odd = 0

for code in reg_code:
    if code % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(count_even,count_odd, sep = " ")


# 2
# The number of clients of the company from the start day of their journey till now is recorded sensibly and is seemed to have followed a specific series like 2,3,5,7,11,13,17,19, 23,…, etc
# Write a program that takes an integer N as the input and will output the series till the Nth term.

# Note:
# The given series is prime number series.
# Input Format:
# The first line of the input is an integer N.
# Output Format:
# The output is a single line series till Nth term, each separated by a space.
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# 5
# Sample Output 1:
# 2 3 5 7 11
# Sample Input 2:
# 10
# Sample Output 2:
# 2 3 5 7 11 13 17 19 23 29

# wrong ANSWER... it is a prime number
number = int(input())

number_list = [2, 3, 5]
sum = 5
count = 0

if number == 0:
    print("")
elif number == 1:
    print("2")
elif number == 2:
    print("2 3")
elif number == 3:
    print("2 3 5")
else:
    for n in range(number - 3):
        if n % 2 == 0:
            sum = sum + 2
            number_list.append(sum)
        else:
            sum = sum + 4
            number_list.append(sum)
    print(number_list, sep = " ")

prime_count = 0

for num in range(2,100):
    if prime_count < 10:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            print(num, end = " ")
            prime_count += 1


# CORRECT ANSWER
number = int(input())
prime_count = 0
num = 2

while prime_count < number:
    for i in range(2, num):
        if num % i == 0:
            break

    else:
        print(num, end = " ")
        prime_count += 1
    num += 1

    
# 3
# The number of events that the company organizes every month is recorded sensibly and is seemed to have followed a specific series like: 30, 35, 38, 41, 54, 53 ...
# Write a program which takes an integer N as the input and will output the series till the Nth term.

# Input Format:
# First line of the input is an integer N.
# Output Format:
# Output a single line the series till Nth term, each separated by a comma.
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# 5
# Sample Output 1:
# 30 35 38 41 54
# Sample Input 2:
# 10
# Sample Output 2:
# 30 35 38 41 54 53 78 71 110 95

number = int(input())

even = 30
odd = 35

count_even = 0
count_odd = 0

list_number = []

for num in range(0, number):
    
    if num % 2 == 0:
        even = even + count_even
        list_number.append(even)
        count_even = count_even + 8
    else:
        odd = odd + count_odd
        list_number.append(odd)
        count_odd = count_odd + 6

for list in list_number:
    print(list, end = " ")


# 4
# As per the rules of the contest, two members form a team and Richie initially has the number A and Riya has the number B.
# There are a total of N turns in the game, and Richie and Riya alternatively take turns. In each turn the player whose turn it is, multiplies his or her number by 2. Richie has the first turn. Suppose after the entire N turns, Richie’s number has become C and Riya’s number has become D. The final score of the team will be the sum of the scores (C+D) of both the players after N turns.
# Write a program to facilitate the quiz organizers to find the final scores of the teams.
# Input Format:
# The only line of input contains 3 integers A, B, and N.
# Output Format:
# Output a single line which contains the integer that gives the final score of the team which will be the sum of the scores of both the players after N turns.
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# 1 2 1
# Sample Output 1:
# 4
# Sample Input 2:
# 3 2 3
# Sample Output 2:
# 16


numbers = (input("Enter a number of A, B and N separate by space: "))

number_list = numbers.split(" ")

for n in range(len(number_list)):
    number_list[n] = int(number_list[n])

print(number_list)

print(type(number_list))

A = number_list[0]
B = number_list[1]
N = number_list[2]


for i in range(N):
    if i % 2 == 0:
        A = A * 2
    else:
        B = B * 2
    
total_sum = A + B

print(total_sum)


# 5
# This week’s competition was a Team event and students who register for the event will be given a unique registration code N. The participants are teamed into 10 teams and the team to which a participant is assigned to depends on the absolute difference between the first and last digit in the registration code.
# The event organizers wanted your help in writing an automated program that will ease their job of assigning teams to the participants. If the registration number given is less than 10, then the program should display "Invalid Input".

# Input Format:
# The only line of input contains an integer N.
# Output Format:
# Output the absolute difference between the first and last digit of N.
# Refer sample input and output for formatting specifications.
# Sample Input 1:
# 345
# Sample Output 1:
# 2
# Sample Input 2:
# 9
# Sample Output 2:
# Invalid Input

N = int(input())

last_digit = 0
first_digit = N

if N < 10:
    print("Invalid Input")
        
else:
    last_digit = N % 10 

    while first_digit >= 10:
        first_digit = first_digit // 10

    if last_digit > first_digit:
        answer = last_digit - first_digit
    else:
        answer = first_digit - last_digit

    print(answer)


# iAssess
# A.R.Rahman wants the list of prime numbers available in a range of numbers.
# Can you help him out?
# Write a program to print all prime numbers in the interval [a,b] (a and b, both inclusive).

# Input Format:
# Input consists of 2 integers which correspond to a and b. Assume that a is always less than or equal to b.
# Output Format:
# Refer sample output for details.
# Sample Input 1:
# 2
# 15
# Sample Output 1:
# 2 3 5 7 11 13

a = int(input())
b = int(input())

if a < 2:
     
     a = 2

for num in range(a, b + 1):
    for i in range(2,num):
        if num % i == 0:
            break

    else:
        print(num, end = " ")
    

    