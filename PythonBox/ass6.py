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
    




    



