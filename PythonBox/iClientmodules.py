def change(a):
    b=[x*2 for x in a]
    print(b)

def sum_of_two_numbers(a,b):
    print("Inside module")
    c = a + b
    return c

person = {"name":"JK", "rNo":123,"address": "Cuba"}

JKconstant = 54321

def mul_2_num(a,b):
    print("Inside mul module mul2 function")
    c = a * b
    return c

def mul_3_num(a,b,c):
    print("Inside mul module mul 3 function")
    d = a * b * c
    return d

def area_of_circle(r):
    print("Inside area module circle function")
    a = 3.14*r*r
    return a

def area_of_rectangle(l,b):
    print("Inside are module rectangle function")
    a = l * b
    return a

def perimeter_or_rect(l,b):
    peri = 2(l+b)
    return peri