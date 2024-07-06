# write a python program to read the file
# 
# Create a file using python code 
# use the keyword open to create
# open('fruits.txt')
# the open built in funct takes 2 parameter
# 1) filename 2) mode
# Instruction to create file
# Mode
# 1. x - to create the file 
# 2. t - is going to be a text file
# 3. b - is to be a binary file
# open('fruits.txt', 'xt') # create a file to txt file
# when we run again, we get an error and its files already exist
# suppose to check whether the file already exist
# import os
# os.path.exists('fruis.txt')
# from os import path
# path.exists('filename')
from os.path import exists
# exists('filename')

# filename = "fruits.txt"
# if exists(filename):
#     pass
# else:
#     open(filename, 'xt')
def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if value.strip() == "":
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
        return value
    
def doMenu():
    choice = -1
    while choice != 0:
        print("-------------------")
        print("|    0 - Exit     |")
        print("|    1 - List     |")
        print("|    2 - Add      |")
        print("|    3 - Edit     |")
        print("|    4 - Delete   |")
        print("-------------------")

        choice = keyboardInput(int, "Choice[0, 1, 2, 3, 4]: ", "Choice must be an Integer.")
        if choice == 0:
            print("Thank you for using our system.")
        elif choice == 1:
            printProduct(filename)
        elif choice == 2:
            addProduct(filename)
        elif choice == 3:
            editProduct(filename)
        elif choice == 4:
            deleteProduct(filename)

def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, "xt")
        except Exception as a:
            print("Something went wrong when we create the file:", a)
        else:
            createTitle(filename)
        finally:
            # filehandler is an object/instance of file class
            # filehandler has many methods like read, write and close
            filehandler.close()

# content = input("Fruit Name:")

# whenever you can out of with block the resource will be closed automatically
def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            filehandler.write("Product | Quantity | Price")
    except Exception as e:
        print("Something went wrong when we create the header", e)


def addProduct(filename):   
    try:
        product = keyboardInput(str, "Product: ","Product must be in string")
        quantity = keyboardInput(int, "Quantity: ","Quantity must be in integer")
        price = keyboardInput(float, "Price: ","Price must be in float")
        with open(filename, 'at') as filehandler:
            filehandler.write(f"\n{product} | {quantity} | {price}")
    except Exception as e:
        print("Something went wrong when we append the product:", e)

def printProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity , price =line.strip().split("|") # strip method remove space
            if(index == 0):
                print(f"{"No.":5}{product:20}{quantity:>15}{price:>15}")
                print("="*60)
            else:
                print(f"{index:<5}{product:20}{int(quantity):>15}{float(price):>15.2f}")

    except Exception as e:
        print("Something went wrong when we append the product:", e)

def editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please keyin the index of the Product: ", "Index must be Integer")
        if index >= len(data):
            print("Sorry product not available")
        else:
            product, quantity , price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure you want to edit this product (y / n) ?: ", "Respond not valid")
            if confirm == 'y':
                newproduct = keyboardInput(str, f"Product[{product}]: ","Product must be in String", product)
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ","Quantity must be in Integer", quantity)
                newprice = keyboardInput(float, f"Price[{price}]: ","Price must be in Float", price)
                data[index] = [newproduct, newquantity, newprice]
                newlines = []
                for product in data:
                    line = " | ".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the product:", e)

def deleteProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please keyin the index of the Product: ", "Index must be Integer")
        if index >= len(data):
            print("Sorry product not available")
        else:
            product, quantity , price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure you want to delete this product (y / n) ?: ", "Respond not valid")
            if confirm == 'y':
                del data[index] 
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we delete the product:", e)


filename = "fruits.txt"
createFile(filename)
doMenu()
# addProduct(filename)
# printProduct(filename)



