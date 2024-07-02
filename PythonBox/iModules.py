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









    




