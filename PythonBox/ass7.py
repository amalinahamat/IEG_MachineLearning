'''
'''
# 1 
# A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, 
# so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
# For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
# Example: The quick brown fox jumps over the lazy dog.
# Your task is to figure out if a sentence is a pangram.

sentences = input("Write a sentences\n").strip()
sentences = sentences.lower()
sentences = sentences.replace(" ", "")
sentences = sentences.replace(".", "")
sentences = sentences.replace(",", "")
# or
# sentences = sentences.lower().replace(" ", "").replace(".", "").replace(",", "")
#print(sentences)

alphabets = {"a","b", "c", "d", "e", "f", "g",
             "h","i", "j", "k", "l", "m", "n",
             "o","p", "q", "r", "s", "t", "u",
             "v","w", "x", "y", "z" }

list_char = set()

for char in sentences:
    #print(char)
    list_char.add(char)

print()
print(f"list alphabet from alphabet list:\n{sorted(alphabets)}")
print(f"list alphabet from input_user:\n{sorted(list_char)}")
print()

if alphabets <= list_char:
    print("The sentences is a PANGRAM")
else:
    print("The sentences is NOT PANGRAM")

'''

'''
# 2
# n isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, 
# however spaces and hyphens are allowed to appear multiple times.
# Examples of isograms:
# lumberjacks background downstream six-year-old
# The word isograms, however, is not an isogram, because the s repeats.
# Your task is to figure out if the user input is isogram

word = input("Enter a word or phrase: ").strip()
word = word.replace("-","")
word = word.replace(".","")
word = word.replace(",","")
word = word.replace(" ","")

char_set = set()
char_repeated = []
for char in word:
    if char in char_set:
        if char not in char_repeated:
            char_repeated.append(char)      
    else: 
        char_set.add(char)

if char_repeated:
    print(f"'{word}' is not an isogram as {char_repeated} repeated")

else:
    print(f"'{word}' is an isogram")

'''
'''

# 3
# Parse and evaluate simple math word problems returning the answer as an integer.
# What is 5?    -> 5
# What is 5 plus 13?    -> 13
# What is 7 minus 5?    -> 2
# What is 6 multiplied by 4?     -> 24
# What is 25 divided by 5?       -> 5
# What is 5 plus 13 plus 6?      -> 24
# What is 3 plus 2 multiplied by 3?       -> 15
# print(first = int("What is 5?")f"   -> {}") 

import re

def solve_math(question):

    question = question.lower().strip().replace("?", "")

    patterns = [
        (r"what is (\d+)$", lambda x: int(x[0])),
        (r"what is (\d+) plus (\d+)$", lambda x: int(x[0]) + int(x[1])),
        (r"what is (\d+) minus (\d+)$", lambda x: int(x[0]) - int(x[1])),
        (r"what is (\d+) multiplied by (\d+)$", lambda x: int(x[0]) * int(x[1])),
        (r"what is (\d+) divided by (\d+)$", lambda x: int(x[0]) // int(x[1])),
        (r"what is (\d+) plus (\d+) plus (\d+)$", lambda x: int(x[0]) + int(x[1]) + int(x[2])),
        (r"what is (\d+) plus (\d+) multiplied by (\d+)$", lambda x: int(x[0]) + (int(x[1]) * int(x[2]))),
    ]

    for pattern , func in patterns:
        match = re.match(pattern, question)
        if match:
            return func(match.groups())
        
    return "Sorry, i could not understand the problem"

list_questions = ["What is 5?",
                  "What is 5 plus 13?", 
                  "What is 7 minus 5?", 
                  "What is 6 multiplied by 4?", 
                  "What is 25 divided by 5?", 
                  "What is 5 plus 13 plus 6?", 
                  "What is 3 plus 2 multiplied by 3?"]

for question in list_questions:
    print(f"{question} -> {solve_math(question)}")

'''
'''
# 4
# The first 2 bands of a resistor have a simple encoding scheme: each color maps to a single number.
# For example, if they printed a brown band (value 1) followed by a green band (value 5), 
# it would translate to the number 15.
# In this exercise you are going to create a helpful program so that you don't have to 
# remember the values of the bands. The program will take color names as input and output a two digit number,
# even if the input is more than two colors!

def band_color() :
    return {
    "black" : 0,
    "brown" : 1,
    "red"   : 2,
    "orange": 3,
    "yellow": 4,
    "green" : 5,
    "blue"  : 6,
    "violet": 7,
    "grey"  : 8,
    "white" : 9
}

user_color = input("Please put the 2 band colors with - as separator: ")

user_color_list = user_color.strip().lower().split("-")

if len(user_color) < 2:
    print ("Please provide at least 2 colors")
else:
    list_user = []
    color_map = band_color()
    for color in user_color_list:
        if color in color_map:
            list_user.append(color_map[color])
        else:
            print(f"Invalid color: {color}")
            break

if len(list_user) == 2:
    resistance_value = (list_user[0] * 10) + list_user[1]
    print(f"the resistance value for {user_color} is {resistance_value}.")
else:
    resistance_value = (list_user[0] * 10) + list_user[1]
    print(f"the resistance value for {user_color} is {resistance_value}, ignoring after color 2.")

'''
'''
# 5
# Your task is to Validate Credit Card Number
# Given a number determine whether or not it is valid per the Luhn formula.
# The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers,
# such as credit card numbers and Canadian Social Insurance Numbers.
# The task is to check if a given string is valid

account_number = input("Enter credit card number\n").replace(" ", "")

list_digit = []
for number in str(account_number):
    print(number)
    list_digit.append(int(number))

print(list_digit)

each_digits = []
for index in range(len(list_digit) -1, -1, -1):
    digit = list_digit[index]
    if (len(list_digit) - index) % 2 == 0:
        double_digit = digit * 2
        if double_digit > 9:
            double_digit = (double_digit //10) + (double_digit % 10) 
        each_digits.append(double_digit)
    else:
        each_digits.append(digit)

each_digits.reverse()

print(each_digits)

total_sum = sum(each_digits)

print(total_sum)

if total_sum % 10 == 0:
    print("This number is valid!")
else:
    print("This number is not valid!")

'''
'''

# 6
# Write a Python class that has two methods: getString and printString , 
# The getString accept a string from the user and printString prints the string in upper case.

class String:
    def __init__ (self):
        self.word = ""

    def getString(self):
        self.word = input("Enter a string: ")
    
    def printString(self):
        self.word = self.word.upper()
        print(self.word)
    
    
s = String()
s.getString()
s.printString()
'''
'''
# 7
# Write a Python class Employee with properties id, name, salary, and department and 
# methods like _init_ calculateSalary, assignDepartment and _str_.
# "E7876", "ADAMS", 50000, "ACCOUNTING"
# "E7499", "JONES", 45000, "RESEARCH"
# "E7900", "MARTIN", 50000, "SALES"
# "E7698", "SMITH", 55000, "OPERATIONS"

class Employee:
    def __init__(self,id_number,name,salary,department, hours_worked = 0):
        self.id_number = id_number
        self.name = name
        self.salary = salary
        self.department = department
        self.hours_worked = hours_worked

    def calculateSalary(self):
        if self.hours_worked > 50:
            overtime_hours = self.hours_worked - 50
            overtime_amount = overtime_hours * (self.salary / 50)
            total_salary = self.salary + overtime_amount

        else:
            total_salary = self.salary
        return f"{total_salary:.2f}"

    def assignDepartment(self, new_department):
        self.department = new_department

    def __str__(self):
        return f"Employee : Id Number : {self.id_number}, Name : {self.name}, Salary : {self.calculateSalary()}, Department : {self.department}, Hours Worked : {self.hours_worked}"


employee_data = [("E7876","ADAMS",50000,"ACCOUNTING", 55),
                 ("E7499","JONES",45000,"RESEARCH", 48),
                 ("E7900","MARTIN",50000,"SALES", 60),
                 ("E7698","SMITH",55000,"OPERATIONS", 45)]



employees = []

for id_number,name,salary,department,hours_worked in employee_data:
    employees.append(Employee(id_number, name, salary, department, hours_worked))

def add_new_employee():
    id_number = input("Enter the employee ID: ")
    name = input("Enter the employee name: ")
    salary = float(input("Enter the employee salary: "))
    department = input("Enter the employee department: ")
    hours_worked = int(input("Enter the number of hours worked: "))

    new_employee = Employee(id_number, name, salary, department,hours_worked)
    employees.append(new_employee)

    print("\nNew Employee Details: ")
    print(new_employee)
    print(f"Calculated Salary (for {hours_worked} hours worked): {new_employee.calculateSalary()}")

for employee in employees:
    print (employee)

add_new_employee()

print("\nAll Employees: ")
for employee in employees:
    print (employee)

'''

'''
# 8
# Write a Python class Inventory with attributes like id, productName, 
# availableQuantity and price. Add methods like addItem, updateItem, 
# and checkItem_details.
# Use a dictionary to store the item details, where the key is the id 
# and the value is a dictionary containing the productName, availableQuantity and price.

class Inventory:

    item_details = \
        {
            "97410": 
                { 
                    "productName" :"Television",
                    "availableQuantity" : 20,
                    "price" : 1455.99
                },

            "97411": 
                { 
                    "productName" :"Radio",
                    "availableQuantity" : 32,
                    "price" : 654.25
                }           
        }

    def __init__ (self,id_number,productName,availableQuantity,price):
        self.id_number = id_number
        self.productName = productName
        self.availableQuantity = availableQuantity
        self.price = price

    def addItem(self,id_number,productName,availableQuantity,price):
        Inventory.item_details[id_number] = \
        {
            "productName" : productName,
            "availableQuantity" : availableQuantity,
            "price" : price
        }
        print(f"Item added: {productName}")

    def updateItem(self,id_number,productName,availableQuantity,price):
        if id_number in Inventory.item_details:
            Inventory.item_details[id_number] = \
            {
                "productName" : productName,
                "availableQuantity" : availableQuantity,
                "price" : price
            }
            print(f"Item updated: {productName}")
        else:
            print(f"Item with ID {id_number} not found.")
        

    def checkItem_details(self,id_number):
        if id_number in Inventory.item_details:
            item = Inventory.item_details[id_number]
            print(f"ID: {id_number}\nProduct Name: {item['productName']}\n"
                  f"Available quantity: {item['availableQuantity']}\n"
                  f"Price: {item['price']}")
        else:
            print(f"Item with ID {id_number} not found.")


print("Select the matters:\n")
print("1. Add item\n2. UpdateItem\n3. CheckItem\n")
number = int(input("Enter the number: "))

if number == 1:
    id_number = input("Enter ID number: ")
    productName = input("Enter product name: ")
    availableQuantity = int(input("Enter available quantity: "))
    price = float(input("Enter price of product: "))
    Inventory.addItem(id_number,productName,availableQuantity,price)
elif number == 2:
    id_number = input("Enter ID number: ")
    productName = input("Enter updated product name: ")
    availableQuantity = int(input("Enter updated available quantity: "))
    price = float(input("Enter updated price of product: "))
    Inventory.updateItem(id_number,productName,availableQuantity,price)
elif number == 3:
    id_number = input("Enter ID number to be checked: ")
    Inventory.checkItem_details(id_number)
else:
    print("Invalid input! Please enter just number between 1 and 3.")

'''
'''
class Inventory():

    item_details = \
        {
            "97410": 
                { 
                    "productName" : "Television",
                    "availableQuantity" : 20,
                    "price" : 1455.99
                },

            "97411": 
                { 
                    "productName" : "Radio",
                    "availableQuantity" : 32,
                    "price" : 654.25
                }           
        }

    def __init__ (self,id_number,productName,availableQuantity,price):
        self.id_number = id_number
        self.productName = productName
        self.availableQuantity = availableQuantity
        self.price = price
        #self.item_details = {}
        

    def addItem(self,id_number,productName,availableQuantity,price):
        self.item_details[id_number] = \
        {
            "productName" : productName,
            "availableQuantity" : availableQuantity,
            "price" : price
        }
        #print(f"Item added: {productName}")
        print()
        print(f"Item added:\n\nID: {id_number}\nProduct Name: {productName}\n"
              f"Available quantity: {availableQuantity}\n"
              f"Price: {price}")

    def updateItem(self,id_number,productName,availableQuantity,price):
        if id_number in self.item_details:
            self.item_details[id_number] = \
            {
                "productName" : productName,
                "availableQuantity" : availableQuantity,
                "price" : price
            }
            #print(f"Item updated: {productName}")
            print()
            print(f"Item updated:\n\nID: {id_number}\nProduct Name: {productName}\n"
                  f"Available quantity: {availableQuantity}\n"
                  f"Price: {price}")
        else:
            print()
            print(f"Item with ID {id_number} not found.")
        

    def checkItem_details(self,id_number):
        if id_number in self.item_details:
            item = self.item_details[id_number]
            print()
            print(f"ID: {id_number}\nProduct Name: {item['productName']}\n"
                  f"Available quantity: {item['availableQuantity']}\n"
                  f"Price: {item['price']}")
        else:
            print()
            print(f"Item with ID {id_number} not found.")


print("Select the matters:\n")
print("1. Add item\n2. UpdateItem\n3. CheckItem\n")
number = int(input("Enter the number: "))

print()
if number == 1:
    id_number = input("Enter ID number: ")
    productName = input("Enter product name: ")
    availableQuantity = int(input("Enter available quantity: "))
    price = float(input("Enter price of product: "))
    inventory = Inventory(id_number, productName, availableQuantity, price)
    inventory.addItem(id_number,productName,availableQuantity,price)
elif number == 2:
    id_number = input("Enter ID number: ")
    productName = input("Enter updated product name: ")
    availableQuantity = int(input("Enter updated available quantity: "))
    price = float(input("Enter updated price of product: "))
    inventory = Inventory(id_number, productName, availableQuantity, price)
    inventory.updateItem(id_number,productName,availableQuantity,price)
elif number == 3:
    id_number = input("Enter ID number to be checked: ")
    inventory = Inventory(id_number, "", 0, 0.0)
    inventory.checkItem_details(id_number)
else:
    print("Invalid input! Please enter just number between 1 and 3.")


'''
'''

# 9
# Write a Python class BankAccount with attributes like accountNumber, 
# openingBalance, currentBalance dateOfOpening and customerName. 
# Add methods like deposit, withdraw, and checkBalance.

from datetime import datetime

class BankAccount:
    def __init__(self, accountNumber, openingBalance, dateOfOpening, customerName):
        self.accountNumber = accountNumber
        self.openingBalance = openingBalance
        self.currentBalance = openingBalance
        self.dateOfOpening = dateOfOpening if dateOfOpening else datetime.now().strftime('%Y-%m-%d')
        self.customerName = customerName

    def deposit(self, amount):
        if amount > 0:
            self.currentBalance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.currentBalance:
            self.currentBalance -= amount
            print(f"Withdrawn: {amount}")
        elif amount > self.currentBalance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive")

    def checkBalance(self):
        return self.currentBalance

    def __str__(self):
        return (f"Account Number: {self.accountNumber}\n"
                f"Customer Name: {self.customerName}\n"
                f"Opening Balance: {self.openingBalance}\n"
                f"Current Balance: {self.currentBalance}\n"
                f"Date of Opening: {self.dateOfOpening}")

bank_accounts = []

def add_bank_account():
    accountNumber = input("Enter an account number: ")
    openingBalance = float(input("Enter an opening balance: "))
    dateOfOpening = input("Enter the date of opening (YYYY-MM-DD, leave empty for today): ")
    customerName = input("Enter a customer name: ")

    if dateOfOpening == "":
        dateOfOpening = None

    new_bank_account = BankAccount(accountNumber, openingBalance, dateOfOpening, customerName)
    bank_accounts.append(new_bank_account)
    print("\nNew Bank Account Details: ")
    print(new_bank_account)

add_bank_account()

print("\nAll Bank Accounts: ")
for account in bank_accounts:
    print(account)

if bank_accounts:
    first_account = bank_accounts[0]
    first_account.deposit(200)
    print(f"Current Balance after deposit: {first_account.checkBalance()}")
    first_account.withdraw(100)
    print(f"Current Balance after withdrawal: {first_account.checkBalance()}")

print("\nUpdated Account Details:")
for account in bank_accounts:
    print(account)

'''
'''
# 10
# Write a Python class to check the validity of a string of parentheses,
# '(', ')', '{', '}', '[' and '].
# These brackets must be closed in the correct order, for example
# "()" and "()[]{}" are valid
# "[)", "({[)]" and "{{{" are invalid

class ValidParentheses:
    def __init__(self):
        self.open_list = ["[","{","("]
        self.close_list = ["]","}",")"]

    def check(self,Mystr):
        stack = []
        for i in Mystr:
            if i in self.open_list:
                stack.append(i)
            elif i in self.close_list:
                pos = self.close_list.index(i)
                if ((len(stack) > 0) and (self.open_list[pos] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return "unbalanced"
                
        if len(stack) == 0:
            return "Balanced"
        else:
            return "Unbalanced"
        
    

checks = ValidParentheses()

parentheses = input("Enter the parentheses: ").strip()

result = checks.check(parentheses)
print(f"The parentheses are {result}")





        

