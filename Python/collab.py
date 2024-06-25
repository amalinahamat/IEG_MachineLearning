'''
number = int(input("Enter a whole number: "))

if(number % 2 == 0):
    print("The number is an even number.")
else:
    print("The number is an odd number.")

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


number = int(input("Enter a year: "))

if(number %  4 == 0):
    print("That year is a leap year")
else:
    print("That year is not a leap year")


a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

if(a > b and a > c):
    print("The largest one: ", a)
elif(b > a and b > c):
    print("The largest one: ", b)
else:
    print("The largest one: ", c)



alphabet = str(input("Enter a single character: "))

if(alphabet == "a" or alphabet == "e" or alphabet == "i" or
   alphabet == "o" or alphabet == "u" or alphabet == "A" or 
   alphabet == "E" or alphabet == "I" or alphabet == "O" or 
   alphabet == "U"):
    print("That single character is a vowel character.")
else:
    print("That single character is a consonant character.")



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

'''
'''
length_a = int(input("Enter a first length: "))
length_b = int(input("Enter a second length: "))
length_c = int(input("Enter a third length: "))

if(length_a == length_b == length_c):
    print("Equilateral triangle")
elif(length_a == length_b or length_a == length_c or length_b == length_c):
    print("Isosceles triangle")
else:
    print("Scalene triangle ")



withdrawal = int(input("Enter a withdrawal amount: "))

if(withdrawal % 10 == 0):
    notes50 = withdrawal // 50
    print("notes 50: ", notes50)
    notes20 = (withdrawal % 50) // 20
    print("notes20: ", notes20)
    notes10 = (withdrawal % 20) // 10
    print("notes10: ", notes10)
else:
    print("the amount cannot be withdraw. please enter an amount that is multiple of 10 means the number must be divisible by 10 without a remainder")



number = int(input("Enter a number max to 1000: "))

square_number = number ** 2
print("Square number: ", square_number)

if(number >= 0 and number < 4):
    reverse_number = 0
    reverse_number = reverse_number * 10 + (number % 10)
    print("Reverse number: ",reverse_number)
    square_reverse_number = reverse_number ** 2
    print("Square reverse number: ",square_reverse_number)
    reverse_square_reverse_number = 0
    reverse_square_reverse_number = reverse_square_reverse_number * 10 + (square_reverse_number % 10)
    print("Reverse_square_reverse_number: ", reverse_square_reverse_number)
elif((number > 10 and number < 14) or (number > 20 and number < 23) or (number == 31)):
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
elif((number > 100 and number < 104) or (number > 110 and number < 114) or (number > 120 and number < 123) 
     or (number > 200 and number < 203) or (number > 210 and number < 213) or (number == 221) 
     or (number == 301) or (number == 311)):
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
else:
    print("This is not an Adams number")

if(square_number == reverse_square_reverse_number):
    print("The square number and the reverse square reverse number is equal. This is an Adam number")
else:
    print("The square number and the reverse square reverse number is not equal. This is an Adam number")



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


number = int(input("Enter a number max to 1000: "))

num = number

if(number >= 0 and number < 10):
    result = 0
    result = result * 10 + (number % 10)
    print(result)
    sum = result ** 1
    print(sum)
elif(number >= 10 and number < 100):
    result1 = 0
    result1 = result1 * 10 + (number % 10)
    result1 = result1 ** 2
    print(result1)
    number = number // 10
    result2 = 0
    result2 = result2 * 10 + (number % 10)
    result2 = result2 ** 2 
    print(result2)
    sum =  result1 + result2  
    print(sum)
elif(number >= 100 and number < 1000):
    result1 = 0
    result1 = result1 * 10 + (number % 10)
    result1 = result1 ** 3
    print(result1)
    number = number // 10
    result2 = 0
    result2 = result2 * 10 + (number % 10)
    result2 = result2 ** 3
    print(result2)
    number = number // 10
    result3 = 0
    result3 = result3 * 10 + (number % 10)
    result3 = result3 ** 3
    print(result3)  
    sum =  result1 + result2 + result3 
    print(sum)
else:
    print("Please enter the number which maximum is 1000")

if(sum == num):
    print("This is an Armstrong number")
else:
    print("This is not an Armstrong number)")




withdrawal = int(input("Enter a withdrawal amount: "))

if(withdrawal % 10 == 0):
    notes50 = withdrawal // 50
    print("notes 50: ", notes50)
    withdrawal = withdrawal % 50
    print("withdrawal: ", withdrawal)
    notes20 = withdrawal // 20
    print("notes 20: ", notes20)
    withdrawal = withdrawal % 20
    print("Withdrawal: ", withdrawal)
    notes10 = withdrawal // 10
    print("notes 10: ", notes10)
else:
    print("the amount cannot be withdraw. please enter an amount that is multiple of 10 means the number must be divisible by 10 without a remainder")

   

quotient = 97409

remainder = quotient % 2
quotient  = quotient // 2
print(str(remainder), quotient)

result = str(remainder)
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(
remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)

remainder = quotient % 2
quotient = quotient // 2
print(remainder, quotient)

result = str(remainder) + result
print(result)



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
quotient = quotient // 2
print(result, quotient)


x = 5
y = 10
x = x ^ y
y = x ^ y
x = x ^ y
print("X=%d, Y=%d"%(x,y))


x = 5
k = x + 6j
print("Real part: %d\nImaginary part: %d" %(k.real,k.imag))


x =10
print("Binary number:", bin(x))

x = 10
print("complex number:", complex(x))

x = "B"
print("ASCII value:", ord(x))

x = 15
print("Octal Value: ",oct(x))
print("Hexadecimal Value: ",hex(x))

a = 8 + 4j
print ("is complex number?", isinstance(a,complex) )

n = 80
print("character:", chr(n))

total = 1 + 2 + 3 + 4  + 5 + 6 + 7
print("Total:", total)

S ="Hello"
print('e' is S)

print("Welcome to Amphi Event Management System")

welcome = "Welcome to Amphi Event Management System"
print(welcome)

name = (input("Enter your name"))
#bold_start = '\033[1m'
#bold_end = '\033[0m'
print(f"\033[1m{name}\033[0m")
#print(f"bold_start + name + bold_end") 
welcome = f"Hello {name} ! Welcome to Amphi Event Management System"
print(welcome)

name = (input("Enter your name"))
print(f"\033[1m{name}\033[0m")
welcome = f"Hello {name} ! Welcome to Amphi Event Management System"
print(welcome)



print("Enter your name")
name = input()
print(f"\033[1m{name}\033[0m")
welcome = f"Hello {name} ! Welcome to Amphi Event Management System"
print(welcome)


print("Enter your name")
name = input(f"\033[1m\033[0m")
#print(f"\033[1m{name}\033[0m")
welcome = f"Hello {name} ! Welcome to Amphi Event Management System"
print(welcome)



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



x = int(input("Enter the value of X\n"))
y = int(input("Enter the value of Y\n"))

children = (y - (5*x)) / 13
adult = children + x
senior = 2 * children
y = (5*adult) + (2 * children) + (3 * senior)

print(f"Number of children tickets sold : {int(children)}")
print(f"Number of adult tickets sold : {int(adult)}")
print(f"Number of senior tickets sold : {int(senior)}")


side = float(input("Enter the side in cm of a square tile\n"))
number_tiles  = int(input("Enter the number of square tiles available\n"))

max_side_length = int(number_tiles ** 0.5)
print(max_side_length)
largest_area = (side * max_side_length) ** 2

print(f"Area of the largest possible square is {int(largest_area)}sqcm")




total_salary = int(input("Enter the total salary paid"))

weekend_rate = 50
weekday_rate = 80

# total_salary = (weekday_rate * weekday_hour) + (weekend_rate * weekend_hour)
weekend_hour = int((total_salary - 800 ) / 130)
weekday_hour = int(10 + weekend_hour)

print(f"Number of weekday hours is {weekday_hour}")
print(f"Number of weekend hours is {weekend_hour}")


worker_a = int(input("Enter an hours completed project worker A\n"))
worker_b = int(input("Enter an hours completed project worker B\n"))
print(worker_a)
print(worker_b)

complete_time = ((1/worker_a) + (1/worker_b))
reciprocal_complete_time = (1 / complete_time)

print("%.2f"%reciprocal_complete_time)

worker_c = int(input("Enter an hours completed project worker C\n"))
worker_d = int(input("Enter an hours completed project worker D\n"))
print(worker_c)
print(worker_d)

complete_time = complete_time + (1/worker_c) + (1/worker_d)
reciprocal_complete_time = (1 / complete_time)
print("%.2f"%reciprocal_complete_time)



x = int(input("Enter the value of X\n"))
y = int(input("Enter the value of Y\n"))

children = ( y  -   (5 * x ))  // 13
adult = children + x
senior = 2 * children
y = (5*adult) + (2 * children) + (3 * senior)co

print(f"Number of children tickets sold : {children}")
print(f"Number of adult tickets sold : {adult}")
print(f"Number of senior tickets sold : {senior}")

arguments = input("")
print(arguments[::])
print("arguments:")

for argument in arguments:
    if(argument != " "):
        print(argument)
    else:
        print("nothing")

print(len(arguments))


#import sys

arguments = str(input(""))
arguments = arguments.split(" ")
#print(arguments)
print("Arguments: ")
for argument in arguments:
    print(argument)

print(f"Number of arguments is {len(arguments)}")


total = 0
for number in numberlist:
    # int function trim the string value
    # remove the spaces in the string and then convert
    # string ot integer
    total = total + int(number)
print(total)

total_solution = int(input("Enter a total liter of solution (liters): "))
total_salt = float(input("Enter a percentage of total salt: "))
total_salt /= 100
salt_a = float(input("Enter a percentage of salt a: "))
salt_a /= 100
salt_b = float(input("Enter a percentage of salt b: "))
salt_b /= 100

solution_a = ((salt_b * total_solution) - (total_salt * total_solution)) / (salt_b - salt_a)
solution_b = (total_solution - solution_a)

print(f"solution a : {solution_a}, solution b : {solution_b})

max_solution = 3

if(solution_a < max_solution and solution_b < max_solution):
    print("Solution (A) and Solution(B) is available can proceed.")
elif(solution_a  < max_solution and solution_b > max_solution):
    solution_b = solution_b - max_solution
    print(f"Only Solution (A) is available , please order {solution_b} liter now.")
elif(solution_a > max_solution and solution_b < max_solution):
    solution_a = solution_a - max_solution
    print(f"Only Solution (B) is available ,please order {solution_a} liter now.")
else:
    solution_a = solution_a - max_solution
    solution_b = solution_b - max_solution
    print(f"Solution (A) and Solution(B) is not available, please order solution A {"%.2f"%solution_a} liter and solution b {"%.2f"%solution_b} liter now.")



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



# 1/work_rate = 1/workera + 1/workerb
worker_a = int(input("Enter an hours complete by worker A: "))
worker_b = int(input("Enter an hours complete by worker B:  "))

work_rate = (worker_a * worker_b) / (worker_a + worker_b)

print(f"times for both workers to complete the project: {work_rate:.2f}")




a = 0b10101000
b = 0b01010100

# 1.
mask_a = 0b00001111
print(f"1. {bin(a | mask_a)}")

# 2.
print(f"2. {bin(a | b)}")

# 3.

mask_b = 0b10001010
print(f"3. {bin(a ^ mask_b)})



total_money = float(input("Enter a number of total invest amount: "))
interest_rate_a = float(input("Enter a percentage of interest rate first account: "))
interest_rate_b = float(input("Enter a percentage of interest rate second account: "))
total_interest = float(input("Enter a number of total interest amount: "))

interest_rate_a = interest_rate_a / 100
print(interest_rate_a)
interest_rate_b = interest_rate_b / 100


second_account = (total_interest - (total_money * interest_rate_a)) / (interest_rate_b - interest_rate_a)
first_account = (total_money - second_account)

print(f"first account invest: {first_account:.2f}\nsecond account invest: {second_account:.2f}")

 

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
print(a == b)


 

show_1 = int(input("Enter the number of people who watched show 1\n"))
average_show_1 = float(input("Enter the average rating for show 1\n"))

show_2 = int(input("Enter the number of people who watched show 2\n"))
average_show_2 = float(input("Enter the average rating for show 2\n"))

show_3 = int(input("Enter the number of people who watched show 3\n"))
average_show_3 = float(input("Enter the average rating for show 3\n"))

total_average_show = ((show_1 * average_show_1) + (show_2 * average_show_2) + (show_3 * average_show_3)) / (show_1 + show_2 + show_3)
print(f"The overall average rating for show is {total_average_show:.2f}")
 

n = int(input("Enter the change money: "))

result = n // 100
remainder = n % 100
total_result = result

result = remainder // 50
remainder = n % 50
total_resultresult = total_result + result

result = remainder // 10
remainder = remainder % 10
total_result = total_result + result

result = remainder // 5
remainder = remainder % 5
total_result = total_result + result

result = remainder // 2
remainder = remainder % 2
total_result = total_result + result

result = remainder // 1
remainder = remainder % 1
total_result = total_result + result
print(f"Enter the change money:{total_result}")


x = True
y = False
z = False
if x or y and z:
    print("Hello")
else:
    print("World")

a = 20
b =3
if (a >= b):
    print("if")
elif a>=21:
    print("elif")
else:
    print("else")




grade = 60
if grade >= 65:
    print("passing grade")
else:
    print("Failing grade")



number = 1
while number < 11:
  print(number)
  number = number + 1


prime_count = 0
number = 2

for _ in range(1,100):
    if prime_count >= 10:
        break
    prime_number =  True
    if number > 1:
        #for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime_number = False
                break
    else:
        prime_number = False
    
    if prime_number:
        print(number)
        prime_count += 1

    number += 1





number = int(input("Enter a number: "))

square_number = number ** 2
print("Square number: ", square_number)

original_number = number
reverse_number = 0
while (number > 0):
    reverse_number = (reverse_number * 10) + (number % 10)
    number = number // 10

print("reverse_number: ", reverse_number)

square_reverse_number = reverse_number ** 2

reverse_square_reverse_number = 0
temp =  square_reverse_number
while (temp > 0):
    reverse_square_reverse_number =  (reverse_square_reverse_number * 10) + (temp % 10)
    temp = temp // 10

print("Reverse square reverse number: ", reverse_square_reverse_number)

if ( square_number == reverse_square_reverse_number ):
    print("Adam Number")
else:
    print("Not Adam Number")


number = int(input("Enter a number: "))

original_number = number

digit_number = len(str(number))

sum = 0
while(number > 0):
    result = number % 10
    sum = sum + (result ** digit_number)
    number = number // 10

print(f"Sum: {sum} ")

if (sum ==  original_number):
    print("This is an Armstrong number")
else:
    print("This is not an Armstrong number")






for pattern in range(1, 6):
    print("o" * pattern)

      
digit_line = 5

for digit in range(1,digit_line + 1):
    for digits in range (1, digit + 1):
        print(digits, end = " ")
   
    print()



number = int(input("Enter a number: "))

sum = 0
for i in range (1, number + 1):
    sum = sum + i
print(sum)



numbers = (input("Enter a few number separated by spaces: "))

numbers_list = numbers.split()

print("all numbers: ")
for number in numbers_list:
    print(number)

print("even numbers: ")
for even in numbers_list[0::2]:
    print(even)

print("odd numbers: ")
for odd in numbers_list[1::2]:
    print(odd)



numbers = (input("Enter a few number separated by spaces: "))

numbers_list = numbers.split()

numbers_length = (len(numbers_list))

sum = 0
for number in numbers_list:
    sum = sum + int(number)

average = sum / numbers_length
print("Average number:", average)







import sys
print(sys.argv)

numbers =  sys.argv

print(numbers)
#numbers_list = numbers.split()

print("all numbers: ")
for number in numbers[1::]:
    print(number)

print("even numbers: ")
for even in numbers[1::2]:
    print(even)

print("odd numbers: ")
for odd in numbers[2::1]:
    print(odd)


import sys
print(sys.argv)

numbers = sys.argv[1:]
print(numbers)

#numbers_list = numbers.split()
numbers = [int(number) for number in numbers]

numbers_length = (len(numbers))

sum = 0
for number in numbers:
    sum = sum + number

average = sum / numbers_length
print("Average number:", average)


numbers = (input ("Enter numbers separated by commas: "))
print(type(numbers))

numbers_list = numbers.split(",")
print(numbers_list)

same_number = False

for number in range(len(numbers_list)):
    for num in range(number + 1, len(numbers_list)):
        if(numbers_list[number] == numbers_list[num]):
            print("same number detected:", numbers_list[number])
            same_number = True
            break
    if same_number:
        break
else:
    print("all numbers are different") 

   

numbers = (input ("Enter numbers separated by commas: "))
print(type(numbers))

numbers_list = numbers.split(",")
print(numbers_list)

numbers_list = [int(number) for number in numbers_list]
print(numbers_list)

total_unique = False

for i in range(len(numbers_list)):
    for j in range(i + 1, len(numbers_list)):
        for k in range(j + 1, len(numbers_list)):
            if numbers_list[i] + numbers_list[j] + numbers_list[k] == 100:
                print(f"Three numbers that sum total 100: {numbers_list[i], numbers_list[j], numbers_list[k]}")
                total_unique = True
                break
        if total_unique:
            break
    if total_unique:
        break

else:
    print("No total unique that sum to 100.")


first_number = int(input("Enter a first positive number: "))
second_number = int(input("Enter a second positive number: "))

result = 0
for i in range (second_number):
    result = result + first_number
    
print(result)


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

print(result)


number = (input("Enter a number : "))

decimal_number = 0

for i in range(len(number)):
    convert = int(number [len(number) -1 -i])
    decimal_number = decimal_number + convert * ( 2 ** i)

print(decimal_number)
'''

# question prime number 
'''
START

given_number = range(2, 51)
count = 9
Display 1
repeat given_number as given_number
    if(count > 0):
        isPrime = True
        divisors = range(2, given_number)
        repeat divisors as divisor
            if given_number % divisor == 0
                isPrime = False
                break
        if isPrime == True  
            Display given_number 
            count = count - 1

        if count == 0 break

END

'''

