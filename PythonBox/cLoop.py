
#idesign

# 1
com_code = int(input())

reg_code = []

for n in range(com_code):
    code = int(input())
    reg_code.append(code)

print(reg_code)

count_even = 0 
count_odd = 0

for code in reg_code:
    if code % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(count_even,count_odd, sep = " ")



# 2

# wrong... it is a prime number

number = int(input())

number_list = [2, 3, 5]
sum = 5
count = 0

if number == 0:
    print("")
elif number == 1:
    print("2")
elif number == 2:
    print("2 3")
elif number == 3:
    print("2 3 5")
else:
    for n in range(number - 3):
        if n % 2 == 0:
            sum = sum + 2
            number_list.append(sum)
        else:
            sum = sum + 4
            number_list.append(sum)
    print(number_list, sep = " ")


prime_count = 0

for num in range(2,100):
    if prime_count < 10:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            print(num, end = " ")
            prime_count += 1


number = int(input())
prime_count = 0
num = 2

while prime_count < number:
    for i in range(2, num):
        if num % i == 0:
            break

    else:
        print(num, end = " ")
        prime_count += 1
    num += 1

    

# 3

number = int(input())

even = 30
odd = 35

count_even = 0
count_odd = 0

list_number = []

for num in range(0, number):
    
    if num % 2 == 0:
        even = even + count_even
        list_number.append(even)
        count_even = count_even + 8
    else:
        odd = odd + count_odd
        list_number.append(odd)
        count_odd = count_odd + 6

for list in list_number:
    print(list, end = " ")


# 4

numbers = (input("Enter a number of A, B and N separate by space: "))

number_list = numbers.split(" ")

for n in range(len(number_list)):
    number_list[n] = int(number_list[n])

print(number_list)

print(type(number_list))

A = number_list[0]
B = number_list[1]
N = number_list[2]


for i in range(N):
    if i % 2 == 0:
        A = A * 2
    else:
        B = B * 2
    
total_sum = A + B

print(total_sum)

# 5
N = int(input())

last_digit = 0
first_digit = N

if N < 10:
    print("Invalid Input")
        
else:
    last_digit = N % 10 

    while first_digit >= 10:
        first_digit = first_digit // 10

    if last_digit > first_digit:
        answer = last_digit - first_digit
    else:
        answer = first_digit - last_digit

    print(answer)


#iassess
a = int(input())
b = int(input())

if a < 2:
     
     a = 2

for num in range(a, b + 1):
    for i in range(2,num):
        if num % i == 0:
            break

    else:
        print(num, end = " ")
    

    