'''
'''
# 1
# Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" 
# instead of the number, and for the multiples of five, print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".
number = 100
three = 1
five = 1
for i in range(1, number + 1 ):
    if ((i == three * 3) and (i == five * 5)):
        print("FizzBuzz", end = " ")
        three += 1
        five += 1
    elif i == three * 3:
        print("Fizz", end = " ")
        three += 1
    elif i == five * 5:
        print("Buzz", end = " ")
        five += 1
    else:
        print(i, end = " ")

print()
print()

number = 100
for i in range(1, number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end = " ")
    elif i % 3 == 0:
        print("Fizz", end = " ")
    elif i % 5 == 0:
        print("Buzz", end = " ")
    else:
        print(i, end = " ")
'''
'''
# 2
# Write a program that takes an integer input from the user and generates the Collatz sequence for that number. 
# The Collatz sequence is defined as follows:
# start with a number n. If n is even, the next number is n/2. If n is odd, the next number is 3n + 1. 
# Repeat the process until n becomes 1.

number = int(input())

print(number, end = " ")

next_number = 0

while number > 0 and number != 1:

    if number % 2 == 0:
        next_number = (number // 2 )
        number = next_number
        
    else:
        next_number = ((3 * number) + 1 )
        number = next_number

    print(number, end = " ")


print()

number = int(input())

next_number = 0
list_number = [number]

while number > 0 and number != 1:

    if number % 2 == 0:
        next_number = (number // 2 )
        number = next_number
        list_number.append(number)
        
    else:
        next_number = ((3 * number) + 1 )
        number = next_number
        list_number.append(number)

for num in list_number:
    print(num, end = " ")

'''
'''
# 3
# Write a program that takes two integers from the user and 
# calculates their greatest common divisor (GCD) using the Euclidean algorithm.

A = int(input())
B = int(input())

GCD_AB = 0

list_GCD_AB = [(A,B)]
Q = 0
R = 0


while B != 0:       
    Q = A // B
    R = A % B
    A = (B * Q) + R

    A = B
    B = R 

    list_GCD_AB.append((A,B))

print(list_GCD_AB)

GCD_AB = A
print("GCD:", GCD_AB)
    
'''
'''
# 4
# Write a program that plays the game of Rock, Paper, Scissors with the user. 
# The user makes a choice, the program randomly chooses, and the winner is determined.
# To generate random number use random module
# import random
# random.randint(1,3)

import random


user = input("Enter either (Rock , Paper, Scissors): ")

possible_act =["Rock", "Paper", "Scissors"]
#machine_index = random.randint(0,len(possible_act) - 1)
machine_index = random.randint(1,3)
machine_act = possible_act[machine_index - 1]

print(f"machine choose: {machine_act}")

if user == machine_act:
    print("Draw")
elif user == "Rock" and machine_act == "Paper":
    print("machine win")
elif user == "Rock" and machine_act == "Scissors":
    print("user win")
elif user == "Paper" and machine_act ==  "Rock":
    print("user win")
elif user == "Paper" and machine_act == "Scissors":
    print("machine win")
elif user == "Scissors" and machine_act == "Rock":
    print("machine win")
elif user == "Scissors" and machine_act == "Paper":
    print("user win")
else:
    print("Invalid Input")

'''
'''
# 5
# Write a program that randomly generates a number between 1 and 100. 
# The user has to guess the number. After each guess, 
# the program tells the user whether the guess is too high, too low, or correct. 
# The game continues until the user guesses the correct number.
# To generate random number use random module
# import random
# random.randint(1,3)
import random

guess = int(input("Enter the number between 1 to 100: "))

machine_index = random.randint(1, 100)
print(machine_index)

while guess != machine_index:
    if guess > machine_index:
        print("the guess is to high")
    else:
        print("the guess is too low")

    guess = int(input("Enter the number between 1 to 100: "))
    print(machine_index)
    
print("The guess is correct")
'''
'''
# 6
# Write a program that generates 10 perfect numbers.
# Example
# 6: The divisors of 6 are 1, 2, 3, and 6. 
# The sum of its proper divisors (excluding 6 itself) is 1 + 2 + 3 = 6.
# 28: The divisors of 28 are 1, 2, 4, 7, 14, and 28. 
# The sum of its proper divisors (excluding 28 itself) is 1 + 2 + 4 + 7 + 14 = 28.

count_perfect = 0
prime_num = 2

print("first 10 Perfect number: ")

while count_perfect < 4:

    for i in range(2,prime_num):
        if prime_num % i == 0:
            break

    else:
        perfect_number = (2 ** (prime_num - 1)) * (2 ** prime_num - 1)
        print(perfect_number)
        count_perfect += 1


    prime_num += 1

print()

# or

count_perfect = 0
prime_num = 2

print("first 10 Perfect number: ")

while count_perfect < 8:

    #for i in range(2,prime_num):
    for i in range(2, int(prime_num ** 0.5) + 1):
        if prime_num % i == 0:
            break

    else:
        mersenne_prime = (2 ** prime_num - 1)

        #for j in range(2, mersenne_prime):
        for j in range(2, int(mersenne_prime ** 0.5) + 1):
            if mersenne_prime % j == 0:
                break

        else:
            perfect_number = (2 ** (prime_num - 1)) * mersenne_prime
            print(perfect_number)
            count_perfect += 1


    prime_num += 1

'''
'''
# 7
# Write a program that calculates the sum of the first n terms of the harmonic series. Take the n as Input.
# Hn = 1 + 1/2 + 1/3 + 1/4 .... + 1/n

n = int(input())

total_sum = 0
Hn = 0

if n <= 0 :
  print("Please enter a positive integer number!")
else:
  for i in range (1, n + 1):
      Hn = 1 / i 
      total_sum = total_sum + Hn

  print(f"sum of the harmonic number: {total_sum:.2f}")
'''
'''
# 8
# Write a program that converts a number to its word representation (e.g., 123 to "one hundred twenty-three").
number = int(input("Enter an integer of number: "))

def units(number):
    unit = {
        1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 
        8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
        14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
        19:"nineteen" 
    }
    return unit.get(number,"")
    
    
def tens(number):
    ten = {
        20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 
        70:"seventy", 80:"eighty", 90:"ninety"
    }
    if number in ten:
        return ten[number]
    else:
        return ten[(number // 10 )* 10] + " " + units(number % 10)
    
def hundreds(number):
    if number % 100 == 0:
        return units(number // 100) + " hundred "
    else:
        return units(number // 100) + " hundred " + number_to_word(number % 100)
    
def thousands(number):
    if number % 1000 == 0:
        return units(number // 1000) + " thousand "
    else:
        return units(number // 1000) + " thousand " + number_to_word(number % 1000)

def ten_thousands(number):
    if number < 20000 :
        return units(number // 1000) + " thousand " + number_to_word(number % 1000)
    else:
        return tens((number // 10000) * 10) +" " + number_to_word(number % 10000) 
    

def number_to_word(number):
    if number == 0:
        return "zero"
    elif number < 20:
       return units(number)

    elif number < 100:
        return tens(number)

    elif number < 1000:
        return hundreds(number)
    
    elif number < 10000:
        return thousands(number)
    
    elif number < 100000:
        return ten_thousands(number)
    
    else:
        return("Out of range")

print("number to words:",number_to_word(number))

'''
'''
# 9
# Write a program to convert a Roman numeral to an integer 
# and also convert integer to Roman numeral 

number = input("Enter a numeral number or roman number: ")

def numeral_to_roman(number):
    roman = {
        1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI",
        7:"VII", 8:"VIII", 9:"IX", 10:"X", 11:"XI",
        12:"XII", 13:"XIII", 14:"XIV", 15:"XV", 16:"XVI",
        17:"XVII", 18:"XVIII", 19:"XIX", 20:"XX", 30:"XXX",
        40:"XL", 50:"L", 60 :"LX", 70:"LXX", 80:"LXXX", 90:"XC",
        100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 
        600:"DC", 700:"DCC", 800:"DCCC", 900:"CM", 1000:"M"
        }
    
    if number < 1 or number > 4000:
        return "Out of range"
    
    roman_numeral = ""

    for value, symbol in roman.items():
        while number >= value:
            roman_numeral += symbol
            number -= value

    return roman_numeral

def roman_to_numeral(roman):
    numeral = {
        "I": 1, "II":2, "III":3, "IV":4, "V":5, "VI":6,
        "VII":7, "VIII":8, "IX":9, "X":10, "XI":11,
        "XII":12, "XIII":13, "XIV":14, "XV":15, "XVI":16,
        "XVII":17, "XVIII":18, "XIX":19, "XX":20, "XXX":30,
        "XL":40, "L":50, "LX":60, "LXX":70, "LXXX":80, "XC":90,
        "C":100, "CC":200, "CCC":300, "CD":400, "D":500,
        "DC":600, "DCC":700, "DCCC":800, "CM":900, "M":1000
    }
    return numeral.get(roman, "Invalid roman numeral")

if number.isdigit():
    number = int(number)
    print(numeral_to_roman(number))
else:
    print(roman_to_numeral(number.upper()))

# or

def integerToRoman(number):
    romansDict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }
 
    num = 1
    while number >= num:
        num *= 10
 
    num /= 10
 
    res = ""
 
    while number:
         # main significant digit extracted
        # into lastNum
        lastNum = int(number / num)
 
        if lastNum <= 3:
            res += (romansDict[num] * lastNum)
        elif lastNum == 4:
            res += (romansDict[num] +
                        romansDict[num * 5])
        elif 5 <= lastNum <= 8:
            res += (romansDict[num * 5] +
            (romansDict[num] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romansDict[num] +
                        romansDict[num * 10])
 
        number = (number % num)
        num /= 10
         
    return res

number = int(input("Enter a numeral number: "))


print("Roman to integer is:"
                + str(integerToRoman(number)))


def value_roman_to_integer(roman):
    if(roman == "I"):
        return 1
    if(roman == "V"):
        return 5
    if(roman == "X"):
        return 10
    if(roman == "L"):
        return 50
    if(roman == "C"):
        return 100
    if(roman == "D"):
        return 500
    if(roman == "M"):
        return 1000
    return - 1

def roman_to_integer(roman):
    n = 0
    i = 0
    while(i < len(roman)):
        s1 = value_roman_to_integer(roman[i])

        if(i + 1 < len(roman)):
            s2 = value_roman_to_integer(roman[i + 1])

            if (s1 >= s2):
                n = n + s1
                i = i + 1
            else:
                n = n + s2 - s1
                i = i + 2
        
        else:
            n = n + s1
            i = i + 1
    
    return n

roman = (input("Enter a roman number: "))
print("Integer to Roman is: ", roman_to_integer(roman))

'''
'''
# 10
# Write a program to perform basic string compression using the counts of repeated characters 
# (e.g., "aabcccccaaa" -> "a2b1c5a3").
    

list_word = input("Write a single word: ")

word = []
for char in list_word:
    print(char)
    char = char.lower()
    word.append(char)

print(word)

def word_string(word):

    compressed = ""
    count = 1

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
        
        else:
            compressed += word[i] + str(count)

            count = 1
    
    compressed += word[-1] + str(count)

    return compressed

compressed_word = word_string(list_word)

print("String compression: ", compressed_word)




    













