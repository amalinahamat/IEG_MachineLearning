age = 30
print(age)

age = 40
print(age)

maths_operation = 3 + 2 * 4 / 2 - 2
print(maths_operation)

maths_operation = 3 + 2 * 4 // 2 - 2
print(maths_operation)

float_operation = 12 / 3
print(float_operation)

integer_operation = 12 // 3
print(integer_operation)

float_operation = 8 / 3
print(float_operation)

integer_operation = 8 // 3
print(integer_operation)

reminder = 13 % 5
print(reminder)

x = 37
reminder = 37 % 2
print(reminder)


string_with_quotes = "Hello, it's me."
another_with_quotes = 'He said "You are amazing" yesterday'
another_with_same = "He said \"You are amazing\" yesterday"

print(string_with_quotes)
print(another_with_quotes)
print(another_with_same)


"""" 
this is my coding for learning process
"""

multiline = """

Aku bukanlah superman
Aku juga bisa nangis
Jika kekasih hatiku
Pergi meninggalkan aku

"""
print(multiline)


name = "Amal"
greet = "hi, " + name
print(greet)

age = "34"
print("You are, " + age)

age = 34
age_str = str(age)
print("You are " + age_str)


age = 34
print(f"You are {age}")

name = "amal"
greet = f"How are you , {name}"
print(greet)


answer = 5 * 5 + 10 / 2 * 7 - 3
print(answer)

answer = 5 * 5 + 10 // 2 * 7 - 3
print(answer)

#===

name = "Amal"
final_greet = "How are you, {}?"
amal_greet = final_greet.format(name)
print(amal_greet)

name = "Lia"
lia_greet = final_greet.format(name)
print(lia_greet)

my_name = "Amal"
your_name = input("Enter your name : ")
print(f"Hello {your_name}. My name is {my_name}") 

#===

age = input("Enter your age : ")
age_int = int(age)
print(f"You have live for {age_int * 12} months.") 

age = int(input("Enter your age: "))
print(f"You have lived for {age * 12} months.")

age = int(input("Enter you age: "))
month = age * 12
print(f"You have lived for {month} months")

#====

age = int(input("Enter your age: "))
can_learn_program = age > 0 and age < 150

print(f"You can learn programming : {can_learn_program}")

age =  int(input("Enter your age: "))
not_working = age < 18 or age > 65
print(f"At {age}, you are usually not working: {not_working}")


age = int(input("Enter your age: "))
working = age >= 18 and age <= 65
print(f"At {age}, you are usually working: {working}")

print(bool(35))
print(bool("Amal"))
print(bool(0))
print(bool(""))

x = True or False
print(f"{x}, {bool(x)}")

y = True and False
print(f"{y}, {bool(y)}")

m = 35 or 0
print(f"{m}, {bool(m)}")

n = 35 and 0
print(f"{n}, {bool(n)}")

name = (input("Enter your name: "))
surname = (input("Enter your surname: "))
greet = name or surname
print(greet)

print(not 35)

ages = 20
over_age = ages >= 18
under_Age = ages < 18
same_age = ages == 20
print (f"You are {ages}")


my_number = 9
user_number = int(input("Enter your number: "))
matches = my_number == user_number
print(f"You got it right: {matches}")  