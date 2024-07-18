'''
# i explore
# 1
Is Python case sensitive when dealing with identifiers?
-> yes

identifiers is a name we give to identify a variable, function , class, module or other object.
They must start with a letter (a-z, A-Z) or an underscore (_).
The remaining characters can be letters, underscores, or digits (0-9).
They are case-sensitive (var, Var, and VAR are different identifiers).
eg:
variables name:-
age = 25
name = "Alice"
_salary = 50000

function names :-
def calculate_area(length, width):
    return length * width

class names :-
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
module names:-
import my_module


# 2
What is the maximum possible length of an identifier?
-> unlimited in length

# 3
Which of the following is invalid?

_a=1
__a=1
__str__=1
none of the mentioned
-> none of the mentioned


# 4
Which of the following is an invalid variable?
my_string_1
1st_string
foo
_
-> 1st_string # cannstart with number


# 5
Why are local variable names beginning with an underscore discouraged?
-> they are used to indicate a private variables of a class


# 6
Which of the following is not a keyword?
eval # is a built-in function in Python that evaluates a string of Python code (expression) within the current scope and returns the result.
assert # keyword used for debugging purposes. It checks if a condition is true. If it's not, it raises an AssertionError exception with an optional error message.
nonlocal # keyword used to declare that a variable inside a nested function refers to a variable defined in the nearest enclosing function's scope.
pass # keyword used as a placeholder for a block of code where Python syntax requires a statement but no action is needed 
-> eval

x = 10
y = 20
expression = "x + y + 5"
result = eval(expression)
print(f"Result of {expression} = {result}")  # Output: Result of x + y + 5 = 35


# 7
All keywords in Python are in
-> Both Uppercase and Lowercase

False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield


# 8
Which of the following is true for variable names in Python?
-> unlimited length


# 9
Which is the correct operator for power (X^y)?
-> X**y


# 10
Which one of these is floor division?
-> //
a = 10
b = 3

result = a // b  # result will be 3

a = -10
b = 3

result = a // b  # result will be -4. rounding towards negative infinity.


# 11
What is the order of precedence in python?
(i) Multiplication
(ii) Exponential
(iii) Division
(iv) Parentheses
(v) Addition
(vi) Subtraction
-> iv,ii,iii,i,v,vi


# 12
What is answer of this expression, 22 % 3 is?
-> 1 # the modulus give a remainder of the result


# 13
Mathematical operations can be performed on a string. State whether true or false.
-> False

# 14
Operators with the same precedence are evaluated in which manner?
-> Left to Right

Example: Operators like addition (+), subtraction (-), multiplication (*), division (/), floor division (//), and modulus (%) are left-associative.
Evaluation Order: When operators of the same precedence appear in an expression, they are evaluated from left to right.
Exceptions:
Exponentiation (**): The exponentiation operator (**) is right-associative, which means it evaluates from right to left. For example, 2 ** 3 ** 2 is evaluated as 2 ** (3 ** 2), not (2 ** 3) ** 2.

# 15
What is the output of this expression, 3*1**3?
-> 3 # right to left as a behaviour of exponentiation


# i analyse

# 1
Tuples can't be made keys of a dictionary. True or False?
-> False

Since tuples are immutable (i.e., they cannot be changed after they are created), they can be used as dictionary keys.
# Creating a dictionary with tuples as keys
my_dict = {
    (1, 2): "value1",
    (3, 4): "value2"
}

# Accessing a value using a tuple key
print(my_dict[(1, 2)])  # Output: value1

However, if a tuple contains mutable elements, such as lists, it cannot be used as a dictionary key. For instance:
# This will raise an error
my_dict = {
    (1, [2, 3]): "value"
}

# 5
What does ~4 evaluate to?
-> -5

the ~ operator is the bitwise negation (or bitwise NOT) operator. It flips all the bits of its operand.

For a given integer 
𝑥
x, the bitwise negation ~x is equivalent to -(x + 1).

Binary Representation:

The binary representation of 4 is 0000 0100 (assuming an 8-bit system for simplicity).
Bitwise Negation:

Flipping all the bits results in 1111 1011.
Decimal Conversion:

In two's complement notation (which is used for signed integers in Python), 1111 1011 corresponds to -5

# 6
Find the value of the expression   4 + 3 % 5
-> 7

# 7
Evaluate the expression given below if A = 16 and B = 15.
A % B // A
-> 0

# 8
What is the value of x, if
x = int(43.55+2/2)
-> 44
The int() function truncates the decimal part of a floating-point number and converts it to an integer. So, int(44.55) will be 44


# 9
What are the values of the following expressions:
2**(3**2)
(2**3)**2
2**3**2
-> 512, 64, 512


# 10
What is the value of the following expression:
float (22//3 + 3/3)
-> 8.0

# 11
Fill the code to in order to get the following Output

Output: X=10,Y=5
x=5
y=10
x = x ^ y
___________
x = x ^ y
print("X=%d, Y=%d"%(x,y))
-> y = x ^ y


# 12
Fill the code to in order to get the following Output


Output:
Real part: 5
Imaginary part: 6

x=5
k= x+6j
print("Real part: %d\nImaginary part: %d"_________________)
-> %(k.real,k.imag)


# 13
Fill the code to in order to get the following Output
Output:
Binary number: 0b1010
x=10
print("Binary number:",______)
-> bin(x)


# 14
Fill the code to in order to get the following output.

Output:
Complex Number: (10+0j)
x=10
print "Complex Number:",______________
->complex(x)


# 15
Fill the code to in order to get the following output.

Output:
ASCII value :  66
x = B
print ("ASCII value:",______________ )
-> ord(x)


# 16
Fill the code to in order to get the following output

Output:
Octal Value: 017
Hexadecimal Value: 0oxf
x=15
print"Octal Value:",___________     (1)
print"Hexadecimal Value:",__________     (2)
-> oct(x)
-> hex(x)


# 17
Fill the code in order to get the following output.

Output:
(8+4j) is complex number? True
a = 8+4j
print a, "is complex number?", __________.
-> isinstance(a,complex)


# 18
Fill the code to in order to get the following output.

Output:
Charcter : P
n = 80
print ("Character :",____________)
-> chr(n)


# 19
Fill the code to in order to get the following output.
Output:
Total: 28
          
total = 1+2+3+4+_______
        5+6+7
print (“Total”, total)
-> \


# 20
Fill the code to in order to get the following output. 
Output: True False 
S="Hello" _____________(1) _____________(2) 
-> 1) print( 'H' in S)
   2) print ('l' not in S)






'''