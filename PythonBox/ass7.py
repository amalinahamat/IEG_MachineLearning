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
print(first = int("What is 5?")f"   -> {}") 

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

# 4

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
# 6
# Write a Python class that has two methods: getString and printString , 
# The getString accept a string from the user and printString prints the string in upper case.


'''
'''
# 8
# Write a Python class Inventory with attributes like id, productName, 
# availableQuantity and price. Add methods like addItem, updateItem, 
# and checkItem_details.
# Use a dictionary to store the item details, where the key is the id 
# and the value is a dictionary containing the productName, availableQuantity and price.
'''
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






        

