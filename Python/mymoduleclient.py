# first method

import mymodule

print("Interest: ", mymodule.simpleInterest(1000,1,6))

# second module
# second method is better than first because 
# we do not need to write module name everytime
# there is also a drawback if you want to import more than
# 1 function you have to explicitly say it
# however python recommend this method
from mymodule import simpleInterest
print("Interest: ",simpleInterest(1000,1,6))

from mymodule import simpleInterest,add
print("Interest: ",simpleInterest(1000,1,6))
print("Result: ", add(10,20))

# third method

from mymodule import *
# this will bring all the functions available to use
print("Interest: ",simpleInterest(1000,1,6))
print("Result: ", add(10,20))


