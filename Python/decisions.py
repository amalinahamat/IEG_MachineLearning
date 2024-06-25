# Write a program to find whether the given number is positive, negative or zero
# Write a program to find whether our business is making profit, loss or breakeven

expenses = 1000
sale = 1100

# objective 1: just say whether we are making profit
# if(sale - expenses > 0)
if(sale > expenses):
    # block of code
    print("You are making profit")

# objective 2 : Say whether we are making profit or loss
if(sale > expenses):
    print("You are making profit")
else:
    print("You are making losses")

# objective 3: say whether we are making profit or loss or breakeven (3 conditions)
if (sale > expenses):
    print("You are making profit")
else:
    if(sale == expenses):
        print("You are making breakeven")
    else:
        print("You are making losses")

# objective 3: say whether we are making profit or loss or breakeven (3 conditions)
if (sale > expenses):
    print("You are making profit")
elif(sale == expenses):
    print("You are making breakeven")
else:
    print("You are making losses")
    
print("Thank you")


# aware of indentation error 

# if the statement to be executed is not a block of code
# it is a single statement then we can write it in the same line

# find whether the given number is even or odd
# modulus => %
given_number = 5
if(given_number % 2 == 0): print("Even Number")
# else: print("Odd Number")

# find whether the given number is even or odd. if the statement is single statement
print("Even Number") if (given_number % 2 == 0) else print("Odd NUmber")

# find whether the given number is positive, negative or zero
given_number = 1
print("+ve") if (given_number > 0) else print("-ve") if (given_number < 0) else print("zero")


