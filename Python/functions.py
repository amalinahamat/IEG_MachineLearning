# functions are used to organized our code

# when to create our own function?
# whenever you copy and paste a block of code 
# then you know already it has to be a function
# remember the first code we did in python is
print("Hello World !!!")

# the above statement can we just write as 1 line
# or do we have to create a function put this line inside the
# function and call the function
# well it depend on your requirement
# lets say if you copy this line and paste it in 5 places
# then it must be converted to a function
def sayHelloWorld():
    print("Hello World inside the function!!!")

# functions are created using the keyword def
# followed by function name
# which is again followed by parantheses()
# which is again followed by colon :
# place your block of code inside the function with indentation

# calling a function
# what will happen if we never call / invoke the function
# nothing happend the code inside the functions never gets executed
# how do i call the function ?
# function name followed by paranthesis ()
sayHelloWorld()

# when we create a function if that fucntion takes some value
# then we must create a variable ( placeholder ) in between the bracket
# if the function takes more than 1 value then we must create
# more than 1 variable(s) (placeholders) separated by comma
# these variable/variables is called "parameter"
# if the parameter is dull color then it means we are taking parameter
# but not using that parameter inside the function
def greeting(name):
    print("Good morning David", name)

# when we called the fucntion since the function is taking a parameter/parameter(s)
# we must pass value to the parameter/parameters
# the value we are passing is called argument
# the number of argument(s) must match with number of parameter(s)
greeting("Jegan")

def total(x,y,z):
    result = x + y + z
    print("Result: ", result)

total(10, 20, 30)
# the arguments are positional


# we ask him to buy, technically after buy he must give it back to us
# so that we can eat
# for example i have this function and inside this function we have code
# to identify the price for each food and return the prices
# so that the caller can do the payment

def buyLunch(makan, minum):
    prices = [] # empty list
    for food in makan:
        if (food  ==  "nasi"):
            # append is a function inside the object prices (instance of list)
            # so append is a method
            prices.append(2.80)
        elif(food == "sayur"):
            prices.append(2.20)
    for food in minum:
        if(food == "nescafe"):
            prices.append(2.50)
    #print(prices)
    #print(makan, minum)
    return prices

# now calculate the amount to be paid
# unless the function return/give you back the receipt
# there is no way for us to find the amount to be paid
# since the buyLunch function is returning some value
# it become compulsory for us to hold the value
# we must declare the placeholder
itemprices = buyLunch(["nasi", "sayur"], ["nescafe"])
total = 0
for price in itemprices:
    total = total + price
print("Amount to be paid:", total)

# buyLunch(["nasi","sayur"], ["nescafe"])

# whether the return value must be a list
def simpleInterest(principle, period, rate):
    interest = (principle * period * rate)
    #return [interest, principle, period, rate]
    return interest
print("Interest Amount:",  simpleInterest(1000, 1, 6))

# however when you return more than one value separated by comma
# it will be a tuple (tuple is nothing but readonly list)
def participantList(nameone, nametwo, namethree):
    nameone = nameone + "Data Science"
    nametwo = nametwo + "Data Science"
    namethree = namethree + "Data Science"
    return nameone, nametwo, namethree

result = participantList("John", "Peter", "Parker")
print(type(result))
    

# you can also make the rate parameter(s) optional by having a default value
def calculatesimpleInterest(principle, period, rate = 6):
    interest = (principle * period * rate)
    return interest

# since we are not passing the value for rate parameter
# the rate will automatically become 6
print(calculatesimpleInterest(1000, 1))


# you can also make the rate parameter(s) optional by having a default value
def calculatesimpleInterest(principle, period = 1, rate = 6):
    interest = (principle * period * rate)
    return interest

# since we are not passing the value for period and rate parameter
# the period will automatically become 1 and the rate will automatically become 6
print(calculatesimpleInterest(1000))
# now the second argument is passed which means period becomes 2 and rate becomes 6
# which means the argument are still positional
print(calculatesimpleInterest(1000, 2))

# is there a way to pass values for principle and rate only
# we can use something called "Named Argument" // Keyword Argument
# here the name is referring to parameter
print(calculatesimpleInterest(principle=1000, rate=5))

def findTotal(givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total = total + givenNumber
    return total

# Variable length Argument
# the number of arguments which we pass vary
# caller can pass the values as a list
print(findTotal([10, 20, 30]))
print(findTotal([10, 20, 30, 40, 50, 60]))
print(findTotal([10, 20, 30, 40, 50, 60, 70, 80, 90]))

# but there are use cases where the caller is not able to place the
# values inside the list and pass the list
# but you can declare the parameter to be able to accept any number
# by introducing * infront of the parameter
# python will take all the arguments place them inside a list
# and pass the list to the function
def calculateTotal(*givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total = total + givenNumber
    return total

# Variable length Argument
# the number of arguments which we pass vary
# caller can pass the values as a list
print(calculateTotal(10, 20, 30))
print(calculateTotal(10, 20, 30, 40, 50, 60))
print(calculateTotal(10, 20, 30, 40, 50, 60, 70, 80, 90))

def listSixLetterFruits(*fruits):
    for fruit in fruits:
        if len(fruit) == 6: print(fruit)

# we are sending the items/fruits individually (not as a list)
# however python will convert them to a list of fruits and pass it
listSixLetterFruits("apple", "orange", "mango", "banana", "durian", "grapes")

def listFruitDetails(*fruits):
    for fruit in fruits:
        print(fruit)

listFruitDetails("apple", 20, 1.40, "orange", "mango", "banana", "durian", "grapes")



def sum(a,b):
    return a + b

print(sum(10,20))
# remember when we see "function(values)" we always call values as an argument
# in the above statement it looks like we are passing
# sum function as an argument to print function
# but in python when you have a function folllowed by ()
# the function is executed first
# which mean , in other words, sum function is executed first
# and the sum function takes 10,20 as an argument and returns 30
# that number 30 becomes argument to print function

# so, what do we mean by passing function as an argument?

def minus(a,b):
    return a - b

# basically in this case we want to hide the sum and minus funtions 
# from the user . We want the user to use the function arithematic
# to perform sum and minus
'''
def arithmatic(keyword,a,b):
    if keyword == "s":
        return sum(a,b)
    elif keyword == "m":
        return minus(a,b)
'''
def arithmatic(func,a,b):
    return func(a,b)
# notice there is no () after the function name
print(arithmatic(sum,10,20))
arithmatic(minus,10,20)


#arithmatic("s",10,20)
print(arithmatic(minus,10,20))

def mul(a,b):
    return a * b

# can i use arithmetic to call mul?
# no cannot . if you want to call you must add one more
# elif inside the arithmetic function

# after modifying now the arithmatic function 
# can call functions created in future
arithmatic(mul,10,20)
print(arithmatic(mul,10,20))


