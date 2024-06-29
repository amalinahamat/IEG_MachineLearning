'''
# i explore
import math
print(abs(math.sqrt(25)))

print(all([2,4,0,6])) # False due to 0 is considered false

print(round(4.576))

a = (1,2,3,4)
# del(a[2]) => tuple ia immutable. cannot be modified

a = (1,2,3)
b =("A", "B", "C")
c = zip(a,b)
print(list(c))

d = {"john":40, "peter":45}
print(d["john"])

a = (2,3,4)
print(sum(a,3)) # means initial sum = 3 => 3 +2 + 3+4 = 12
'''
'''
# iAnalyse

a = (1,2,3)
b = ("A","B","C")
C = zip(a,b) 
print(c)
# zip is a built in function that allow to aggregate
# elemts drom multiple iterable into a single iterable

a = [1,2,3]
b = a.append(4)
print(a)
print(b)

a = [14,52,7]
b=a.copy()
print(b is a) # False. different object. different memory address 

if a == (1,2,3,4):
    print(a[1:-1])
'''


number = int(input())

set_list = []
for num in range(number):
    input_line = input()
    input_number = input_line.split(",")
    s = set()
    for nums in input_number:
        s.add(int(nums))
    set_list.append(s)

union_set = set()
for i in set_list:
    union_set = union_set.union(i)

sorted_union = sorted(union_set)

if len(sorted_union) >= 2:
    second_largest = sorted_union[-2]
else:
    second_largest = None

print(f"set({sorted_union})")
print(second_largest)