x = 10

def printX():
    print("in:" ,x)

print(x)
printX()

def modifyX():
    x = 15
    return  x
   
modifyX()
print(x)

x = modifyX()
print(x)

# however in python we also have a short cut
# because if you follow the tradiitonal method, function always return a single value
# which means we can modify only 1 value at a time
# how about i want to modify more than 1 value??

def pythonModifyX():
    global x # you are telling python do not create x locally
    x = 25
    print("Inside the function(pythonModifyX): ", x)


pythonModifyX()
print(x)

#def simpleInterest(principle, period, rate):


# Summary
# global keyword allows the function to modify the variable which is
# in the global context
# local keyword allows the inner function to modify the variable which is
# in the outer function context
