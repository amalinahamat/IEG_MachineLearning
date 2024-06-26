# keyword => pass

# This is outer function
def authentication(username,password):
    # we have created inner function
    def calculateSI(principle,period,rate):
        def something():
            pass

        result = (principle * period * rate) / 100
        return result

    if(username == "admin" and password == "hrhiu4"):
        # since calculateSI function is inside auntheticaiton function
        # we can call this function here
        print("Simple interest: ", calculateSI(1000,1,6))
    
    return calculateSI

# you can call the function which is in this context
# authenticate("admin","hrhiu4")
# you cannot call the inner function
# which is inside another function context
# calculateSI(1000,1,6) # YOU CANNOT DO THIS

# However if outer function (authenticate)
# returns the inner function (calculateSI)
# then we can call the inner function
func = authentication("admin","hrhiu4")
print("Simple Interest: ", func(1000,1,6))

print("Simple Interest: ", authentication("admin","hrhiu4")(1000,1,6))

# lambda (can only write in one line)
add = lambda a , b : a + b

# 
