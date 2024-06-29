'''




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

