# video

n = 7

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print("#", end = " ")
    print()

True == False
while True:
    print(True)
    break

m = 2
total = 0
while(m < 6):
    total = total + m
    m = m + 1
print(total)

x = "abcd"
for i in x:
    print(i, end="")


x = "abcd"
for i in range(x): # str cannor be interpreted as integer
    print(i)


for i in range(0):
    print(i)

print()

while True:
    print(True)
    break

x = "abcd"
for i in range(len(x)):
    print(i)


x = "abcdef"
while i in range(x):
    pass
    # print x[:4] # Missing parentheses in call to 'print'

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)

for i in range(5):
    if i == 5:
        break
    else:
        print(i, end="")
else:
    print("Here")

for i in range(2):
    print(i)
for i in range(4,6):
    print(i)


# iExplore

# 1
# What is the output of the following?

# True = False
while True:
    print(True)
    break
# -> Syntax Error # the True == False, double equal

# 2
# What is the output of the following?

m=2
total=0
while(m<6):
    total=total+m
    m=m+1
print(total) # 2 + 3 + 4 + 5
# -> 14


# 3
# What is the output of the following?
     
x = 'abcd'
for i in x:
    print(i,end=" ")
# -> a b c d


# 4
# What is the output of the following?
x = 'abcd'
for i in range(x):
    print(i)
# -> error
# Error Explanation:
# x is assigned the string value 'abcd'.
# range(x) attempts to create a range object, but range() expects an integer input, not a string.
# TypeError: 'str' object cannot be interpreted as an integer


# 6
# What is the output of the following?
for i in range(0):
    print(i)
# -> no output
# Explanation:
# range(0) creates an empty range, meaning it generates no numbers.
# Since there are no numbers to iterate over, the loop body (print(i)) never executes.


# 7
# What is the output of the following?
while True:
    print(True)
    break
# -> True


# 8
# What is the output of the following?

x = 'abcd'
for i in range(len(x)):
    print(i)
# -> 0 1 2 3


# iAnalyse

# 1
# What is the output of the following?
x = "abcdef"
while i in range(x):
    pass
    # print x[:4]
# -> TypeError


# 2
# What is the output of the following?

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)
# -> 0 1 2


# 3
# What is the output of the following?
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)
# -> 0 1 2 0
# while i < 3: Since 3 < 3 is False, the loop terminates.
# The else block executes because the while loop condition became False.
# print(0): This prints 0.


# 4
# What is the output of the following?

for i in range(5):    
    if i == 5:        
        break    
    else:        
        print(i,end=" ")
else:    
    print("Here")
# -> 0 1 2 3 4 Here
# The for loop completes all iterations from 0 to 4 without hitting the break statement.
# Since the loop was not exited via break, the else block associated with the for loop executes, printing Here.


# 5
# Which numbers are printed?

for i in range(2):
    print(i)
for i in range(4,6):
    print(i)
# -> 0 1 4 5




