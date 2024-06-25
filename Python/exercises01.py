# Given number is 97531
# I want you to reverse the number
# Expected result is 13579

# mr jegan solution 
a0 = 97531
result = a0 % 10
a1 = a0 // 10
print(result, a1)

result = (result * 10) + (a1 % 10)
a2 = a1 // 10
print(result, a2)

result = (result * 10) + (a2 % 10)
a3 = a2 // 10
print(result, a3)

result = (result * 10) + (a3 % 10)
a4 = a3 // 10
print(result, a4)

result = (result * 10) + (a4 % 10)
a5 = a4 // 10
print(result, a5)

#akmal solution
a0 = 97531

result = (a0 % 10) * 10000
result = result + ((a0 // 10) % 10) * 1000
result = result + ((a0 // 100) % 10) * 100
result = result + ((a0 // 1000) % 10) * 10
result = result + ((a0 // 10000) % 10) * 1
print(result)


a = 2 % 5
print(a)

given_number = 97531
result = 0
result = result * 10 + (given_number % 10)
print(result)
given_number //= 10
print(given_number)
result = result * 10 + (given_number % 10)
print(result)
given_number //= 10
result = result * 10 + (given_number % 10)
given_number //= 10
result = result * 10 + (given_number % 10)
given_number //= 10
result = result * 10 + (given_number % 10)
#result *= 10  + (given_number % 10)
print(result)



'''
total_days = 5
current_day = 0
print(current_day % total_days)
current_day = current_day + 1
print(current_day % total_days)

'''



