print("1" == 1)

# more than zero except statements for a try=except block

def foo():
    try:
        return 1
    finally:
        return 2
        
k = foo()
print(k)

try:
    if '1' != 1:
        raise "someError"
    else:
        print("someError has not occured")
except "someError":
    print ("someError has occured")

def foo():
    try:
        print(1)
    finally:
        print(2)
foo()

try:
    pass
    # Do something
except:
    pass
    # Do something
else:
    pass
    # Do something

valid = False
while not valid:
    try:
        n = int(input("Enter a number"))
        while n%2==0:
            print("Bye")
            valid = True
    except ValueError:
        print("Invalid")

        
