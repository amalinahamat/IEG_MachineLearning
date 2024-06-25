# 1
'''
n = 1
while n < 11:
    print(n)
    n += 1
'''
'''
# 3
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

# 4
'''
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
n = 5
for i in range(1,n + 1):
    print("o" * i) 
'''
'''

# 6
n = 5
for i in range (1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
'''
# 7
'''
n = int(input())

sum = 0
for i in range(1,n + 1):
    sum += i
print(sum)
'''
# 8
'''
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
# 9
'''
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
# 10
'''
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
# 11

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