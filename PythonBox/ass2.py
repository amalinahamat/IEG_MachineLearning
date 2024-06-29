
# 1
# Write a Python program that takes an integer as input and checks whether it is even or odd.
number = int(input("Enter a whole number: "))

if(number % 2 == 0):
    print("The number is an even number.")
else:
    print("The number is an odd number.")

# 2
# Write a Python program that takes a score (between 0 and 100) as input and prints the corresponding grade based on the following criteria:
# A for scores 90 and above
# B for scores 80-89
# C for scores 70-79
# D for scores 60-69
# F for scores below 60
number = int(input("Enter a score between 0 to 100: "))

if(number >= 90):
    print("A")
elif(number >= 80 and number < 90):
    print("B")
elif(number >= 70 and number < 80):
    print("C")
elif(number >= 60 and number < 70):
    print("D")
else:
    print("F")

# 3
# Write a Python program that takes a year as input and checks whether it is a leap year.
number = int(input("Enter a year: "))

if (number %  4 == 0 and number % 100 != 0) or (number % 400 == 0):
    print("That year is a leap year")
else:
    print("That year is not a leap year")

# 4
# Write a program that takes three numbers as input and prints the largest one.
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

if(a > b and a > c):
    print("The largest one: ", a)
elif(b > a and b > c):
    print("The largest one: ", b)
else:
    print("The largest one: ", c)

# 5
# Write a Python program that takes a single character as input and checks whether it is a vowel or consonant.
alphabet = str(input("Enter a single character: "))

if(alphabet == "a" or alphabet == "e" or alphabet == "i" or
   alphabet == "o" or alphabet == "u" or alphabet == "A" or
   alphabet == "E" or alphabet == "I" or alphabet == "O" or
   alphabet == "U"):
    print("That single character is : vowel character.")
else:
    print("That single character is : consonant character.")

# 6
# Write a program that calculates the Body Mass Index (BMI) and categorizes it into different weight statuses. 
# The formula for BMI is weight / height^2, where weight is in kilograms and height is in meters.
# Categories:
# Underweight: BMI < 18.5
# Normal weight: 18.5 <= BMI < 24.9
# Overweight: 25 <= BMI < 29.9
# Obesity: BMI >= 30
weight = float(input("Enter a weight in kilograms: "))
height = float(input("Enter a height in meters: "))
BMI = weight / (height ** 2)

print("BMI: ", "%.2f"%BMI)

if(BMI < 18.5):
    print("Underweigth")
elif(BMI >= 18.5 and BMI < 24.9 ):
    print("Normal weight")
elif(BMI >= 25 and BMI < 29.9):
    print("Overweight")
else:
    print("Obesity")

# 7
# Write a program that takes the lengths of three sides of a triangle and 
# determines whether the triangle is equilateral, isosceles, or scalene.
# Equilateral: All three sides are equal.
# Isosceles: Exactly two sides are equal.
# Scalene: All three sides are different.
length_a = int(input("Enter a first length: "))
length_b = int(input("Enter a second length: "))
length_c = int(input("Enter a third length: "))

if(length_a == length_b == length_c):
    print("Equilateral triangle")
elif(length_a == length_b or length_a == length_c or length_b == length_c):
    print("Isosceles triangle")
else:
    print("Scalene triangle ")

# 8
# Write a program that simulates an ATM withdrawal. The user enters the withdrawal amount 
# and the program checks if the amount is a multiple of 10. If it is, 
# the program prints the number of each denomination (50, 20, 10) required to dispense the amount. 
# If not, it prints an error message. For example if the amount is 233 then it must 
# print "4 50 dollar bills, 1 20 dollar bills, 1 10 dollar bills, 3 1 dollar bills
withdrawal = int(input("Enter a withdrawal amount: "))

if(withdrawal % 10 == 0):
    notes50 = withdrawal // 50
    print("notes 50: ", notes50)
    withdrawal = withdrawal % 50
    notes20 = withdrawal // 20
    print("notes 20: ", notes20)
    withdrawal = withdrawal % 20
    notes10 = withdrawal // 10
    print("notes 10: ", notes10)
else:
    print("the amount cannot be withdraw. please enter an amount that is multiple of 10 means the number must be divisible by 10 without a remainder")

# 9
# Write a Python program to check whether a given number is an Adam number.
# An Adam number is a number for which the square of the number and the square of its reverse are themselves reverses of each other. 
# In other words, if you take a number, reverse it, square both the original number and the reversed number, and the results are still 
# reverse of each other, then the original number is called an Adam number.

number = int(input("Enter a number max to 1000: "))

if(number >= 0 and number < 4):
    square_number = number ** 2
    print("Square number: ", square_number)
    reverse_number = 0
    reverse_number = reverse_number * 10 + (number % 10)
    print("Reverse number: ",reverse_number)
    square_reverse_number = reverse_number ** 2
    print("Square reverse number: ",square_reverse_number)
    reverse_square_reverse_number = 0
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    print("Reverse_square_reverse_number: ", reverse_square_reverse_number)
    if(square_number == reverse_square_reverse_number):
        print("The square number and the reverse square reverse number is equal. This is an Adam number")
    else:
        print("The square number and the reverse square reverse number is not equal. This is an Adam number")
elif(number >= 4 and number < 10):
    square_number = number ** 2
    print("Square number: ", square_number)
    reverse_number = 0
    reverse_number = reverse_number * 10 + (number % 10)
    print("Reverse number: ",reverse_number)
    square_reverse_number = reverse_number ** 2
    print("Square reverse number: ",square_reverse_number)
    reverse_square_reverse_number = 0
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    print("Reverse_square_reverse_number: ",reverse_square_reverse_number)
    if(square_number == reverse_square_reverse_number):
        print("The square number and the reverse square reverse number is equal. This is an Adam number")
    else:
        print("The square number and the reverse square reverse number is not equal. This is an Adam number")
elif(number > 10 and number < 32):
    square_number = number ** 2
    print("Square number: ", square_number)
    reverse_number = 0
    reverse_number = reverse_number * 10 + (number % 10)
    #print(reverse_number)
    number = number // 10
    reverse_number = reverse_number * 10 + (number % 10)
    print("Reverse number: ",reverse_number)
    square_reverse_number = reverse_number ** 2
    print("Square reverse number: ",square_reverse_number)
    reverse_square_reverse_number = 0
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    print("Reverse_square_reverse_number: ",reverse_square_reverse_number)
    if(square_number == reverse_square_reverse_number):
        print("The square number and the reverse square reverse number is equal. This is an Adam number")
    else:
        print("The square number and the reverse square reverse number is not equal. This is an Adam number")
elif(number >= 32 and number < 100):
    square_number = number ** 2
    print("Square number: ", square_number)
    reverse_number = 0
    reverse_number = reverse_number * 10 + (number % 10)
    #print(reverse_number)
    number =  number // 10
    reverse_number = reverse_number * 10 + (number % 10)
    print("Reverse number: ",reverse_number)
    square_reverse_number = reverse_number ** 2
    print("Square reverse number: ",square_reverse_number)
    reverse_square_reverse_number = 0
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    print("Reverse_square_reverse_number: ",reverse_square_reverse_number)
    if(square_number == reverse_square_reverse_number):
        print("The square number and the reverse square reverse number is equal. This is an Adam number")
    else:
        print("The square number and the reverse square reverse number is not equal. This is an Adam number")
elif(number > 100 and number < 317) :
    square_number = number ** 2
    print("Square number: ", square_number)
    reverse_number = 0
    reverse_number = reverse_number * 10 + (number % 10)
    #print(reverse_number)
    number =  number // 10
    reverse_number = reverse_number * 10 + (number % 10)
    #print(reverse_number)
    number = number // 10
    reverse_number = reverse_number * 10 + (number % 10)
    print("Reverse number: ",reverse_number)
    square_reverse_number = reverse_number ** 2
    print("Square reverse number: ",square_reverse_number)
    reverse_square_reverse_number = 0
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    print("Reverse_square_reverse_number: ",reverse_square_reverse_number)
    if(square_number == reverse_square_reverse_number):
        print("The square number and the reverse square reverse number is equal. This is an Adam number")
    else:
        print("The square number and the reverse square reverse number is not equal. This is an Adam number")
elif(number >= 317 and number < 1000):
    square_number = number ** 2
    print("Square number: ", square_number)
    reverse_number = 0
    reverse_number = reverse_number * 10 + (number % 10)
    #print(reverse_number)
    number =  number // 10
    reverse_number = reverse_number * 10 + (number % 10)
    #print(reverse_number)
    number = number // 10
    reverse_number = reverse_number * 10 + (number % 10)
    print("Reverse number: ",reverse_number)
    square_reverse_number = reverse_number ** 2
    print("Square reverse number: ",square_reverse_number)
    reverse_square_reverse_number = 0
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    square_reverse_number = square_reverse_number // 10
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    #print(reverse_square_reverse_number)
    print("Reverse_square_reverse_number: ",reverse_square_reverse_number)
    if(square_number == reverse_square_reverse_number):
        print("The square number and the reverse square reverse number is equal. This is an Adam number")
    else:
        print("The square number and the reverse square reverse number is not equal. This is an Adam number")
elif(number == 10):
    square_number = number ** 2
    print("Square number: ", square_number)
    reverse_number = 0
    reverse_number = reverse_number * 10 + (number % 10)
    #print(reverse_number)
    number = number // 10
    reverse_number = reverse_number * 10 + (number % 10)
    print("Reverse number: ",reverse_number)
    square_reverse_number = reverse_number ** 2
    print("Square reverse number: ",square_reverse_number)
    reverse_square_reverse_number = 0
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    print("Reverse_square_reverse_number: ",reverse_square_reverse_number)
    if(square_number == reverse_square_reverse_number):
        print("The square number and the reverse square reverse number is equal. This is an Adam number")
    else:
        print("The square number and the reverse square reverse number is not equal. This is an Adam number")
elif(number == 100) :
    square_number = number ** 2
    print("Square number: ", square_number)
    reverse_number = 0
    reverse_number = reverse_number * 10 + (number % 10)
    #print(reverse_number)
    number =  number // 10
    reverse_number = reverse_number * 10 + (number % 10)
    #print(reverse_number)
    number = number // 10
    reverse_number = reverse_number * 10 + (number % 10)
    print("Reverse number: ",reverse_number)
    square_reverse_number = reverse_number ** 2
    print("Square reverse number: ",square_reverse_number)
    reverse_square_reverse_number = 0
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    print("Reverse_square_reverse_number: ",reverse_square_reverse_number)
    if(square_number == reverse_square_reverse_number):
        print("The square number and the reverse square reverse number is equal. This is an Adam number")
    else:
        print("The square number and the reverse square reverse number is not equal. This is an Adam number")
else:
    print("Please enter the number which maximum is 1000")

# 10
# Write a Python program to check whether a given number is an Armstrong number.
# An Armstrong number (also known as a Narcissistic number or a Pluperfect number) is a number that is 
# equal to the sum of its own digits each raised to the power of the number of digits. 
# For example, 153 is an Armstrong number because 1 ** 3 + 5 ** 3 + 3 ** 3 = 153
number = int(input("Enter a number max to 1000: "))

num = number

if(number >= 0 and number < 10):
    result = 0
    result = result * 10 + (number % 10)
    print("last digit number :", result)
    sum = result ** 1
    print("sum of all the number after power of 1: ", sum)
elif(number >= 10 and number < 100):
    result1 = 0
    result1 = result1 * 10 + (number % 10)
    result1 = result1 ** 2
    print("last digit number after power of 2:",result1)
    number = number // 10
    result2 = 0
    result2 = result2 * 10 + (number % 10)
    result2 = result2 ** 2
    print("first digit number after power of 2:",result2)
    sum =  result1 + result2
    print("sum of all the number after power of 2: ",sum)
elif(number >= 100 and number < 1000):
    result1 = 0
    result1 = result1 * 10 + (number % 10)
    result1 = result1 ** 3
    print("last digit number after power of 3:",result1)
    number = number // 10
    result2 = 0
    result2 = result2 * 10 + (number % 10)
    result2 = result2 ** 3
    print("middle digit number after power of 3:",result2)
    number = number // 10
    result3 = 0
    result3 = result3 * 10 + (number % 10)
    result3 = result3 ** 3
    print("first digit number after power of 3:",result3)
    sum =  result1 + result2 + result3
    print("sum of all the number after power of 3:",sum)
else:
    print("Please enter the number which maximum is 1000")

if(sum == num):
    print("This is an Armstrong number")
    print("a number that is equal to the sum of its own digits")
else:
    print("This is not an Armstrong number)")
    print("a number that is not equal to the sum of its own digits")
