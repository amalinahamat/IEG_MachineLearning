# whenever you want to iterate a list of items then you must use for loop 
fruits = ["apple","rambutan", "orange", "durian", "mango", "cempedak", "banana", "mangosteen", "grape"]

for fruit in fruits:
    print(fruit)

# print all the items in the even position
for fruit in fruits[::2]:
    print(fruit)

# print only fruits with 6 letters
for fruit in fruits:
    if (len(fruit) == 6):
        print(fruit)

# i want to print each fruit together with the index (position)
position = 0
for fruit in fruits:
    print(position, fruit)
    position += 1

# i want to create a multiplication table of 5
# i want to go until 12
# 1 x 5 = 5
# 2 x 5 = 10
multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multiplicant = 5
for multiplier in multipliers:
    print(multiplier, "x", multiplicant, " = ", multiplier * multiplicant)

# however this is not practical when the until is 200 instead of 12
# we have to go for range option start_index: end_index
# but the : operator can work only on an array//list
# 0b => operator
# bin => function
# we have a built in function called range which can generate list of numebrs
# range function takes start index and end index and generate numbers between them
# start index is included end index is not included
print(range(1,12))

# range is an iterable object,
# which mean we can use it in for loops together with "in" operator
# however print function do not understand how to iterate them
# so it prints as range (1, 12)
# any iterable object can be typecast to a list using list function
# print function knows how to iterate the list
print(list(range(1,12)))
# range function does not include 12

# let us so the multiplication table using range
multiplicant = 6
for multiplier in range(1,13):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)


# split the digits in the input number and print them
# lets say the user give input 97409
# take the input and print 9, 7, 4, 0, 9
# since we do not have it as a list and we also do not know the number of digits
# we have to use while loop
given_number = 97409
while(given_number > 0):
    print(given_number % 10)
    # given_number //= 10
    given_number = given_number // 10

given_number = 12345
number_of_digit = len(str(given_number)) - 1 
print(number_of_digit)
while(given_number > 0):
    print(given_number // 10 ** number_of_digit)
    given_number %= 10 ** number_of_digit
    number_of_digit -= 1

given_number = 83632
str_given_number = str(given_number)
for digit in str_given_number:
    print(digit)

# for loop and while loop can have else block
fruits = ["apple", "orange", "mango", "banana", "grapes"]
# the code in the else block will get executed only when all the fruits are iterated
# list iteration is exhausted (no more item to iterate)

for fruit in fruits:
    print(fruit)
    # since we added this condition now when it sees mango
    # jumps out of the loop (list iteration is not exhausted)
    # the code in the else block not executed
    if(fruit == "mango"):break
else:
    print("all fruits printed")


# code in the else block gets executed only when the
# condition fails
multiplicant = 9
multiplier = 1
while(multiplier <= 12):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)
    multiplier += 1
    # since we added this condition now when it sees 11
    # jumps out of the loop (condition not fail yet 11 <= 12 true)
    # the code in the else block not executed
    if multiplier == 11: break
else:
    print("Multiplication table done")   


# please do not print when the multipliers are multiples of 5
# in other words do not print 
# 5 x 10 = 50
# 10 x 10 = 100
multiplicant = 10
multipliers = range(1,13)
for multiplier in multipliers:
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)



multiplicant = 10
multipliers = range(1,13)
for multiplier in multipliers:
    if multiplier % 5 != 0:
        print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

multiplicant = 10
multipliers = range(1,13)
for multiplier in multipliers:
    if multiplier % 5 == 0: continue
    # what continue keyword will do is
    # without executing the following line, it will jump back to the loop
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)