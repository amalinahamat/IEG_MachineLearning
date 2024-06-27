# 1
def arithmetic(number):

    for i in range (1,13):
        mul = i * number
        print(f"{number} x {i} = {mul}")

number = int(input("Enter an integer number:"))
print()

arithmetic(number)
