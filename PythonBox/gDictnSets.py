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
'''
'''
# 2

words = input()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
    
print(word_count)

sorted_word_count = dict(sorted(word_count.items()))

print(f"Dictionary of string: {sorted_word_count}")
for item in sorted_word_count.items():
    word = item[0]
    count = item[1]
    print(f"{word}--{count}")

'''
'''
# 3

students = {}

number = int(input())
for num in range(number):
    user = input().split(" ")
    name = user[0]
    marks = list(map(int,user[1:]))
    students[name] = marks

find_student = input()


if find_student in students:
    marks = students[find_student]
    average_mark = sum(marks) / len(marks)
    print(f"Average Mark of is:{average_mark:.2f}")
else:
    print()   
'''

# 5


number_element = int(input())

input_list_element = input().split()

set_element  = set()

for element in input_list_element:
    set_element.add(int(element))


sorted_set_element = sorted(set_element)

print(sorted_set_element)

sum_number = int(input())

next_sets_element = []

for sums_number in range(0,len(sorted_set_element), sum_number):
    if sums_number + sum_number <= len(sorted_set_element):
        sum_elements = sum(sorted_set_element[sums_number:sums_number + sum_number])
        next_sets_element.append(sum_elements)
    else:
        next_sets_element.extend(sorted_set_element[sums_number:sums_number + sum_number])

result_set = sorted(set(next_sets_element))
print(result_set)

    


    