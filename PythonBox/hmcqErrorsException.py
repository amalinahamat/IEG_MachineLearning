# 1

What happens when ‘1’ == 1 is executed?
we get a False

# 2

How many except statements can a try-except block have?
more than Zero

# 3
What is the output of the following code?

def foo():
    try:
        return 1
    finally:
        return 2
        
k = foo()
print(k)

2

# 4

Can one block of except statements handle multiple exception?

yes, like except TypeError, SyntaxError [,…].
                                    
# 5

When will the else part of try-except-else be executed? 

when no exception occurs

# 6
Which of the following is not an exception handling keyword in Python?
accept

# 7

What is the output of the following?

try:
    if '1' != 1:
        raise "someError"
    else:
        print("someError has not occured")
except "someError":
    print ("someError has occured")

TypeError: exceptions must derive from BaseException

# 8

What is the output of the following code? 

def foo():
try:
print(1)
finally:
print(2)
foo()

12

# 9

Is the following code valid? 
try:
    # Do something
except:
    # Do something
else:
    # Do something


yes

# 10

When is the finally block executed?
always



# 1
The output of the code shown below is
int('65.43')

ValueError

# 2

What is the output of the code shown below if the input entered is 6?

 

valid = False
while not valid:
    try:
        n=int(input("Enter a number"))
        while n%2==0:
            print("Bye")
            valid = True
    except ValueError:
        print("Invalid")

Bye (printed infinite number of times)

# 3

What is the output of the code shown below?

def getMonth(m):
    if m<1 or m>12:
        raise ValueError("Invalid")
    print(m)
getMonth(6)

6
     

# 1
Which of the following is not a standard exception in Python?

AssignmentError

# 2