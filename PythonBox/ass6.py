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



