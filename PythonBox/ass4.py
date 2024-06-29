
# 1
# Print first 10 natural numbers using while loop
number = 1
while number < 11:
  print(number)
  number = number + 1
'''
'''
# 2
# Print first 10 prime numbers using for loop
prime_count = 0

for num in range(2,100):
    if prime_count < 10:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            print(num, end = " ")
            prime_count += 1
'''
'''
# 3
# Get number of items as input and generate that many ADAM Numbers
number = int(input("Enter a number: "))

count_adam = 0
num = 0

while count_adam < number:
    
    square_number = num ** 2
    #print("Square number: ", square_number)

    original_number = num
    reverse_number = 0
    while (original_number > 0):
        reverse_number = (reverse_number * 10) + (original_number % 10)
        original_number = original_number // 10

    #print("reverse_number: ", reverse_number)

    square_reverse_number = reverse_number ** 2

    temp =  square_reverse_number
    reverse_square_reverse_number = 0
    
    while (temp > 0):
        reverse_square_reverse_number =  (reverse_square_reverse_number * 10) + (temp % 10)
        temp = temp // 10
           
    if square_number == reverse_square_reverse_number:
        print(num, end = " ")
        count_adam += 1
      
    num += 1
'''
'''
# 4
# Get number of items as input and generate that many Armstrong Numbers

number = int(input("Enter a number: "))

count_armstrong = 0
num = 0


while count_armstrong < number:

    digit_number = len(str(num))
    sum = 0
    original_number = num

    while(num > 0):
        result = num % 10
        sum = sum + (result ** digit_number)
        num = num // 10

    #print(f"Sum: {sum} ")

    if sum == original_number:
        print(original_number, end = " ")
        count_armstrong += 1

    num = original_number + 1
'''
'''
# 5
# Write a program to print the following pattern using a loop.
pattern = 5
for pattern in range(1, pattern + 1):
    print("o" * pattern)

'''
'''

# 6
# Write a program to print the following pattern using a loop
n = 5

for i in range (1, n + 1): # 1 2 3 4 5
  for j in range (1, i + 1): # 1 2 3 4 5
    print(j, end = " ")
  print()

'''
'''
# 7
# Get a number as input and calculate the sum of all numbers from 1 to the given number.
n = int(input("Enter a number: "))

sum = 0
for i in range(1,n + 1):
    sum += i
print(sum)
'''
'''
# 8
# Write a python program that takes few numbers as command line argument.
# Use a loop to display all elements. Use another loop to display all elements in the 
# even position. Use another loop to display all elements in the odd position.
import sys
#print(sys.argv)

numbers =  sys.argv

#print(numbers)
#numbers_list = numbers.split()

print("all numbers: ")
for number in numbers[1::]:
    print(number, end = " ")

print()

print("even numbers: ")
for even in numbers[1::2]:
    print(even, end = " ")

print()

print("odd numbers: ")
for odd in numbers[2::1]:
    print(odd, end = " ")
    
'''
'''
# 9
# Write a python program that takes few numbers as command line argument. 
# Find the average of those numbers.

import sys
#print(sys.argv)

numbers = sys.argv[1:]
print(numbers)

sum = 0
for number in numbers:
    print(number, end = " ")
    sum = sum + int(number)

numbers_length = (len(numbers))

print()

average = sum / numbers_length
print(f"Average number: {average:.2f}")

'''
'''
# 10
# Write a Python program that takes a string as input, which contains numbers separated by commas.
# Convert the string to a list of numbers and determine whether all the numbers are different from each other

numbers = (input ("Enter numbers separated by commas: "))
print(type(numbers))

numbers_list = numbers.split(",")
print(numbers_list)

count = 0
for number in range(len(numbers_list)):
    for num in range(number + 1, len(numbers_list)):
        if(numbers_list[number] == numbers_list[num]):
            print("same number detected:", numbers_list[number])
            count += 1

if(count == 0):
    print("all numbers are different")

print("total duplicate",count)
'''
'''
# 11
# Write a Python program that takes a string as input, which contains numbers separated by commas. 
# Convert the string to a list of numbers. Now pick 3 unique numbers from the list whose sum is 100.

numbers = (input ("Enter numbers separated by commas: "))
print(type(numbers))

numbers_list = numbers.split(",")

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
print(numbers_list)

count = 0

for i in range(len(numbers_list)):
    for j in range(i + 1, len(numbers_list)):
        for k in range(j + 1, len(numbers_list)):
            if numbers_list[i] + numbers_list[j] + numbers_list[k] == 100:
                print(f"Three numbers that sum total 100: {numbers_list[i], numbers_list[j], numbers_list[k]}")
                count += 1
if (count == 0):
    print("No total unique that sum to 100.")

print("Total count unique number:", count)

# 12
# Write a Python program to get 2 positive numbers as input and multiply them without using the '*' operator.
first_number = int(input("Enter a first positive number: "))
second_number = int(input("Enter a second positive number: "))

result = 0
for i in range (second_number):
    result = result + first_number

print(result)

# 13
# Write a python program to print first 10 terms in a Fibonacci series
first_F = 0
second_F = 1
n_F = 0

print(first_F)
print(second_F)

for num in range(8):
    next_F = first_F + second_F
    print(next_F)

    first_F = second_F
    second_F = next_F

# 14
# Write a python program which takes a number as input and convert the number to binary. 
# Note: Don't use any builtin functions.
number = int(input("Enter a number: "))

print(type(number))

result = ""

if number == 0:
    result = "0"
else:
    while (number > 0):
        remainder = number % 2
        result = str(remainder) + result
        number = number // 2

print("Binary number: ", result)

# 15
# Write a python program which takes a binary number as input and convert the number to decimal. 
# Note: Don't use any builtin functions.
number = (input("Enter a number : "))

decimal_number = 0

for i in range(len(number)):
    convert = int(number [len(number) -1 -i])
    decimal_number = decimal_number + convert * ( 2 ** i)

print(decimal_number)