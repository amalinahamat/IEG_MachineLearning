#  Aida
# any/ all
# They are builtin functions
# they take boolean list as parameter
# [True, True, False, False]
# check whether the given number is prime number

givennumber = 11
divisors  = range(2,givennumber)

if (len([mynumber for mynumber in divisors if (givennumber % mynumber == 0)]) == 0 ):
    print("Prime number")
else:
    print("not Prime number")

if any([givennumber % mynumber == 0 for mynumber in divisors]):
    print("Not prime number")
else:
    print("Prime number")


# prime number
# check whether the given number is prime or not
# check whether the input is prime or not
# genereate first 10 prime numbers
# generate prime numbers between 10 to 100