'''
x = 1
y = 0
z = 0
if y or x and z:
    print("yes")
else:
    print("no")

x = 20
if not x == 50:
    print('the value of x different from 50')
else:
    print('the value of x is equal to 50')

i = 10
if(i>15):
    print("10 is less than 15")
print("I am Not in if")

age = 38
if(age >= 11):
    print("You are eligible to see the Football match.", end ="")
    if(age <= 20 or age >= 60):
        print("Ticket price is $12", end = "")
    else:
        print("Ticket price is $20", end="")
else:
    print("You are not eligible to buy a ticket.")

print("\n")

if(10 < 0 ) and (0 < -10):
    print("A")
elif(10 > 0) or False:
    print("B")
else:
    print("C")

if True or True:
    if False and True or False:
        print("A")
    elif False and False or True and True:
        print("B")
    else:
        print("C")
else:
    print("D")

x = True
y = False
z = False
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

var = 100
if var == 200:
    print("1 - Got a true expression value", end="")
    print(var,end="")
elif var == 150:
    print("2 - Got a true expression value", end="")
    print(var, end="")
elif var == 100:
    print("3 - Got a true expression value", end="")
    print(var, end="")
else:
    print("4 - Got a false expression value", end="")
    print(var, end="")
print("Good bye!")

x = False
y = True
if x and y:
    print('Both x and y are True')
else:
    print('x is False or y is False or both x and y are False')

# idesign (decision and flow control)
# 1
digits = (input("Enter the digit of your ticket number: "))

reverse_digits = (digits)[::-1]
print(reverse_digits)

print(reverse_digits[0])

if reverse_digits[0] == "3" or reverse_digits[0] == "8":
    print("Lucky Winner")
else:
    print("Not a Lucky Winner")

# 2

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

basic_salary = float(input())

if basic_salary < 15000:
    HRA = 0.15 * basic_salary
    DA = 0.9 * basic_salary
else:
    HRA = 5000
    DA = 0.98 * basic_salary

print(f"{basic_salary + HRA + DA :.2F}")



# 5

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
# iAsses
'''
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

'''