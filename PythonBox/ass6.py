'''
# 1 : Write a python function that takes a number as 
# parameter and prints the multiplication table of 
# that number
def arithmetic(number):

    for i in range (1,13):
        mul = i * number
        print(f"{number} x {i} = {mul}")

number = int(input("Enter an integer number:"))
print()

arithmetic(number)

# 2

# Write a simple python function that returns twin primes 
# less than 1000. If two consecutive odd numbers are both 
# prime then they are known as twin primes.

# Pairs of primes that differ by 2. For example, 3 and 5, 
# 5 and 7, 11 and 13, and 17 and 19 are twin primes.

def twin_primes ():
    numprime = []
    for num in range (2,1000):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            numprime.append(num)

    twin_primes_list = []

    for odd in range(len(numprime) - 1):
        if numprime[odd + 1] - numprime[odd] == 2:
                twin_primes_list.append((numprime[odd], numprime[odd + 1]))

    for twin in twin_primes_list:
        print(f"{twin[0]} and {twin[1]}")

twin_primes()

# 3 
# Write a simple python function that takes a number as parameter and returns 
# the prime factors of that number. Prime Factorization is finding which prime 
# numbers multiply together to make the original number.
# Example: prime factors of 56 - 2, 2, 2, 7

def prime_factor(number):
    prime_factors = []

    while number % 2 == 0:
        prime_factors.append(2)
        number = number // 2

    for j in range(3,number):
        while number % j == 0:
            prime_factors.append(j)
            number = number // j
            
    if number > 2:
        prime_factors.append(number)

    print("prime factor: ", prime_factors)
            

number = int(input("Enter an integer number: "))

prime_factor(number)

    
# 4
# Write a function that inputs a number and returns 
# the product of digits of that number.

def product_number(number):
    total = 1
    while number > 0:
        product = number % 10 
        total = product * total

        number = number // 10
    
    print("Product of the digits of number: ",total)


number = int(input("Enter an integer number: "))

product_number(number)

# 5
# Write a function that takes a number as parameter. 
# The function finds the proper divisors of that number 
# and then finds the sum of proper divisors. Proper divisors 
# of a number are those numbers by which the number is divisible, 
# except the number itself.

# For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18
 
def proper_divisors(number):
    list_properdivisor = []
    sum = 0
    for num in range(1,number):
        if number % num == 0:
            list_properdivisor.append(num)
            sum = sum + num
        
    print("list of proper divisor: ", list_properdivisor)
    print("sum of proper divisor: ",sum)

number = int(input("Enter an integer of a number: "))
proper_divisors(number)

# 6

# A number is called perfect if the sum of proper divisors 
# of that number is equal to the number. For example 28 is 
# perfect number, since 1+2+4+7+14=28. Write a program to 
# print all the perfect numbers in a given range

def perfect_proper_divisors(number):
    perfect_numbers = []
    for num in range(1,number + 1):
        sum = 0
        proper_divisors = []
        for divisor in range(1,num):
            if num % divisor == 0:
                proper_divisors.append(divisor)
                sum = sum + divisor
        if sum == num:
            perfect_numbers.append(num)
            print(f"{num} is a perfect number. Proper divisors: ({proper_divisors} = {sum})")
        
    return perfect_numbers


number = int(input("Enter an integer of a number: "))
perfect_number = perfect_proper_divisors(number)

print(f"Perfect numbers between 1 and {number}: {perfect_number}")


# 7
# Write a python function that takes 2 parameters lower and upper (range).
# Let the function returns pairs of amicable numbers in that range.
# Two different numbers are called amicable numbers if the sum of the proper 
# divisors of each is equal to the other number. For example 220 and 284 are 
# amicable numbers.

def amicableNumbers(lower,upper): 
    def sum_proper_division(num):
        proper_divisors = []
        total = 0
        for i in range(1,num):
            if num % i == 0:
                proper_divisors.append(i)
                total = total + i
                   
        return total,proper_divisors
    
    amicable_pairs = []
    for num in range(lower, upper + 1):
        sum, divisor = sum_proper_division(num)
        if sum > num and sum <= upper:
            next_sum, next_divisor = sum_proper_division(sum)
            if next_sum == num:
                amicable_pairs.append((num,sum))
                print(f"Amicable pair: {num} and {sum}")
                print(f"Sum of proper divisors of {num} : {divisor} = {sum}")
                print(f"Sum of proper divisors of {sum} : {next_divisor} = {next_sum}")  
                print()  
    return amicable_pairs

lower = int(input("Enter a lower integer number: "))
upper = int(input("Enter a hupper integer number: "))

amicable_pairs = amicableNumbers(lower,upper)

# 8

# Write a python function that takes variable length parameters and returns maximum
# and minimum number in the parameter numbers.
# For example if we call the function: maximumMinimum(10, 20, 30, 40, 50)
# The function must return: [10, 50]

def maximun_minimum(numbers):

    listnumbers = list(map(int,numbers.split(",")))

    print(len(listnumbers)) 

    maximun = max(listnumbers)
    minimum = min(listnumbers)

    listmaxmin = [minimum,maximun]

    print(f"minimum and maximum = {listmaxmin}")


    return listmaxmin


numbers = (input("Enter a set of number separated by comma: "))
print((numbers))
print(len(numbers))

maximun_minimum(numbers)

# 9 
# Write a simple Python function that takes a number(n) as a parameter. 
# Then the function prints out the first n rows of Pascal's triangle. 
# Note : Pascal's triangle is an arithmetic and geometric figure first 
# imagined by Blaise Pascal.

def Pascal_Triangle(numbers):

    def factorial(numbers):
        sum = 1
        for num in range(1,numbers + 1):
            sum = sum * num

        return sum
    
    for i in range(numbers):
        for j in range(numbers - i + 1):

            print(end =" ")
        
        for j in range(i + 1):
            print((factorial(i) // (factorial(j) * factorial(i-j))), end = " ")

        print()
    

numbers = int(input("Enter an integer of a number: "))
Pascal_Triangle(numbers)

'''

# 10
# Write a simple python function that accepts a hyphen-separated sequence of words 
# as parameter and returns the words in a hyphen-separated sequence after sorting 
# them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def sort_alphabet(words):
    listword = list(map(str,words.split("-")))
    listword.sort()

    sort_word = ""
    for word in range(len(listword)):
        sort_word = sort_word + listword[word]
        if word != len(listword) - 1:
            sort_word = sort_word + "-"
    
    print(sort_word)

    return 

words = input("Enter a hypen-separated sequence of words:\n")

sort_alphabet(words)







