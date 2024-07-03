# import os
# os.path.exists('filename')
# from os import path
# path.exists('filename')

from os.path import exists

def keyboardInput(datatype, caption, errorMessage):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(filename):
    choice = -1
    while choice != 0:
        print("-----------")
        print("0  -  Exit")
        print("1  -  List")
        print("2  -  Add")
        print("3  -  Edit")
        print("-----------")
        choice = keyboardInput(int, "Choice(0,1,2,3): ", "Choice must be Integer")
        if (choice == 0):
            print("Thnx")
        elif (choice == 1):
            printProduct(filename)
        elif (choice == 2):
            addProduct(filename)
        elif (choice == 3):
            editProduct(filename)



filename = "fruits.txt"

# if not exists(filename):
#     open(filename, "xt")

def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, "xt")
        except Exception as e:
            print("Something went wrong when we create the file:", e)
        else:
             createTitle(filename)
        finally:
            filehandler.close()


def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            filehandler.write("Product|Quantity|Price")
    except Exception as e:
            print("Something went wrong when we create the title:", e)
    finally:
            filehandler.close()

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be interger")
        price = keyboardInput(float, "Price: ", "Price must be float")

        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we append the product:", e)

def printProduct(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            if (index == 0):
                print(f"{"No:":<5}{product:20}{quantity:>20}{price:>20}")
                print("=" * 80)
            else:
                print(f"{index:<5}{product:20}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e:
        print("Something went wrong when we print the products", e)

def editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filerhandler:
            lines = filerhandler.readlines()
        data = []
        for line in lines:
           data.append(line.strip().split("|"))
        index = keyboardInput(int, "Index of Product:", "Index must be INT")
        if (index >= len(data)):
            print("Sorry not available :(")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
            if (confirm == "y"):
                newproduct = keyboardInput(str, f"Product[{product}]: ", "Product must be string")
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be interger")
                newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be float")
                data[index] = [newproduct, newquantity, newprice]
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the products", e)


filename = "fruits.txt"
createFile(filename)
doMenu(filename)

# addProduct(filename)
# printProduct(filename)





import os

def create_file(filename):
    if not os.path.exists(filename):
        try:
            with open(filename, "x") as file:
                file.write("Product | Quantity | Price | Total\n")
        except IOError as e:
            print(f"Error creating file: {e}")
    else:
        print(f"File '{filename}' already exists.")

def add_product(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "a") as file:
                product = input("Enter the product: ")
                quantity = input("Enter the quantity: ")
                price = input("Enter the price (RM): ")
                total = int(quantity) * float(price)
                file.write(f"\n{product} | {quantity} | {price} | {total}")
        except IOError as e:
            print(f"Error adding product: {e}")
    else:
        print(f"File '{filename}' does not exist.")

def read_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                for line in file.readlines():
                    line = line.strip()
                    if line and "|" in line:
                        product, quantity, price, total = line.split("|")
                        print(f"{product.strip():40}{quantity.strip():>20}{price.strip():>20}{total.strip():>20}")
        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename}' does not exist.")

import os

def edit_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r+") as file:
                lines = file.readlines()
                file.seek(0)

                found = False
                for line_index, line in enumerate(lines):
                    line = line.strip()
                    if "|" in line:
                        product, quantity, price, total = line.split("|")
                        print(f"{product.strip():40}{quantity.strip():>20}{price.strip():>20}{total.strip():>20}")

                search_product = input("Enter the product to edit or delete: ").strip().lower()
                edited = False
                for line_index, line in enumerate(lines):
                    if "|" in line:
                        parts = line.strip().split("|")
                        product = parts[0].strip()
                        if product.lower() == search_product:
                            print("\n1. Edit product")
                            print("2. Edit quantity")
                            print("3. Edit price")
                            print("4. Delete product")
                            print("5. Exit")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                new_product = input("Enter the new product: ").strip()
                                parts[0] = new_product
                                edited = True
                                print(f"Product '{product}' has been updated to '{new_product}'.")
                            elif choice == "2":
                                new_quantity = input("Enter the new quantity: ").strip()
                                if new_quantity.isdigit():
                                    parts[1] = new_quantity
                                    edited = True
                                    print(f"Quantity '{quantity}' has been updated to '{new_quantity}'.")
                                else:
                                    print("Invalid input. Quantity must be a number.")
                            elif choice == "3":
                                new_price = input("Enter the new price: ").strip()
                                try:
                                    float(new_price)
                                    parts[2] = new_price
                                    edited = True
                                    print(f"Price '{price}' has been updated to '{new_price}'.")
                                except ValueError:
                                    print("Invalid input. Price must be a number.")
                            elif choice == "4":
                                confirmation = input(f"Are you sure you want to delete '{product}'? (y/n): ").strip().lower()
                                if confirmation == "y":
                                    del lines[line_index]
                                    edited = True
                                    print(f"Product '{product}' has been deleted.")
                                    break  # Exit after deletion
                                else:
                                    print(f"Deletion of '{product}' canceled.")
                            elif choice == "5":
                                print("Exiting...")
                                break
                            else:
                                print("Invalid choice. Try again.")
                                print("")
                            if edited:
                                lines[line_index] = " | ".join(parts) + "\n"
                            break

                if not edited:
                    print(f"Product '{search_product}' not found.")

                file.seek(0)
                file.writelines(lines)
                file.truncate()
        except IOError as e:
            print(f"Error editing file: {e}")
    else:
        print(f"File '{filename}' does not exist.")

def main():
    while True:
        print("1. Create new file")
        print("2. Choose existing file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename to create: ")
            create_file(filename)
            while True:
                print("\nOperations:")
                print("1. Add product")
                print("2. Read file")
                print("3. Edit file")
                print("4. Back to main menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    add_product(filename)
                elif sub_choice == "2":
                    read_file(filename)
                elif sub_choice == "3":
                    edit_file(filename)
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Try again.")
        
        elif choice == "2":
            filename = input("Enter the existing filename: ")
            while True:
                if os.path.exists(filename):
                    print("\nOperations:")
                    print("1. Add product")
                    print("2. Read file")
                    print("3. Edit file")
                    print("4. Back to main menu")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        add_product(filename)
                    elif sub_choice == "2":
                        read_file(filename)
                    elif sub_choice == "3":
                        edit_file(filename)
                    elif sub_choice == "4":
                        break
                    else:
                        print("Invalid choice. Try again.")
                else:
                    print(f"File '{filename}' does not exist.")
                    break
        
        elif choice == "3":
            print("\nExiting...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()