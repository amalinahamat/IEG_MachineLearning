'''
video 1 - modules

1) python program
2) functions, other objects, variables, classes
3) can be accessed by multiple programs by importing the module

import iClientmodules

print("Inside main")
a = b
b = 10
c = iClientmodules.sum_of_two_numbers(a,b)
print("sum =", c)

print(iClientmodules.person["address"])
print(iClientmodules.JKconstant)

====
import iClientmodules as mm

print("Inside main")
a = b
b = 10
c = mm.sum_of_two_numbers(a,b)
print("sum =", c)

print(mm.person["address"])
print(mm.JKconstant)

=====
# from iClientmodules import sum_of_two_numbers,person
# from iClientmodules import *
print("Inside main")
a = b
b = 10

c = sum_of_two_numbers(a,b)

print("sum = ",c)

print(person["name"])

====
from iClientmodules import *

radius = 5
area = area_of_circle(radius)
print(area)

video 2 - packages

1) collection of modules

package//mypackage//all files
package//mypackage & main file

__init__.py => must put this file on the my package
------------------------------------------
inside my __init__.py

print("inside MyPackage \n importing the modules")
import MyPackage.MyModule
import MyPackage.MultipleModule
import MyPackage.AreaCalculationModule
import MyPackage.PerimeterPackage
print("modules imported successfully")
--------------------------------------------
inside Main.py

import MyPackage
import MyPackage.perimetercalculationmodule as per

print("inside main program")
l = 10
b = 10
area = MyPackage.AreaCalculationModule.are_of_rectangle(l,b)
print("area = ", area)

peri = MyPackgae.PerimeterPackage.rectPerimeterModule.perimeter_of_rect(l,b)
print("perimeter =", peri)

if we add another package in mypackage. in the another package, we must add __init__.py
--------------------------------------------
cd Packages
inside  __init__.py
print("importing perimeter package")
import MyPackage.perimeterPackage.circlePerimeterModule
import MyPackage.PerimeterPackage.rectPerimeterModule
print("perimeter package imported successfully")
'''

'''
# iexplore

import sys
print(sys.stdin.readline()) # accept a line

from math import factorial
# print(math.factorial(5)) => remove math
print(factorial(5))

print(sys.stdout.write("hello world"))

#print(eval(sys.stdin.readline()))

from iClientmodules import change
from bDecision import change
s = [1,2,3]
change(s)
'''

# i design
'''
# 1

number = int(input())

if number == 1:
    print("0")
elif number == 2:
    print("0 1")
elif number > 2:
    first_F = 0
    second_F = 1
    next_F = 0
    list_number = [0,1]
    for num in range(number - 2):
        next_F = first_F + second_F
        list_number.append(next_F)
        first_F = second_F
        second_F = next_F

    #print(list_number)
    for n in list_number:
        print(n, end = " ")
else:
    print("Invalid error")
'''
'''
# 2
number = int(input())
fact = 1
if number == 0 :
    print("1")
else:
    for num in range(1,number + 1):
        fact = num * fact
        
    print(fact)
'''
'''
# 3
number_ball = int(input())

list_number_ball = []
for number in range(number_ball):
    num = int(input())
    list_number_ball.append(num)

print(list_number_ball)

number_search_ball = int(input())


for ball in list_number_ball:
    if ball == number_search_ball:
        print("Got it")
        break
else:
    print("Sorry!")
        
'''
'''

# 4

words = input()

words = words.lower()
words = words.split(" ")

#print(words)

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

#sorted_words = sorted(word_count.items())

for sort in sorted(word_count):
    print(f"{sort}-{word_count[sort]}")
'''
'''
# 5

number = 2

list_num = []
for num in range(number):
    n = int(input())
    list_num.append(n)

A = list_num[0]
B = list_num[1]

GCD_AB = 0

list_GCD_AB = [(A,B)]
Q = 0
R = 0


while B != 0:
    Q = A // B
    R = A % B
    A = (B * Q) + R

    A = B
    B = R

    list_GCD_AB.append((A,B))

# print(list_GCD_AB)

GCD_AB = A
print(F"GCD:{GCD_AB}")
'''
'''
# 6

words = input()
word = words.lower()

char_count = {}

for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char in word:
    if char_count[char] == 1:
        print(char)
        break
else:
        print("#")


'''
# 7
number = input("Enter the values:\n").split(" ")


list_number = []
for num in number:
    list_number.append(int(num))
print(list_number)

max_number = max(list_number)
min_number = min(list_number)

print(f"The maximum value is : {max_number}")
print(f"The minimum value is : {min_number}")

        










    




