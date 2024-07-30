# video

# 1
l = [1,2,3,[123,34,56],"hi","hello",[12.3,23.5,"jk",[1234,3456]]]

print(l[5])
print(l[3])
print(l[6])


# 2
n = int(input())
l = []
for i in range(n):
    d = int(input())
    l.append(d)
print(l)

l = [1,2,3,4,5]
l.insert(2,2.5) # add element at specific index [2]
print(l)

l.extend([6,7,8,9]) # add more element 
print(l)

l.append([32,44,55]) # it will add as a single element
print(l)
print(len(l))

for i in l:
    print(i)

#concatenation
l1 = [1,2,3]
l2 = [4,5,6]
l = l1 + l2
print(l)
print(id(l))

l = []
for i in range(100):
    l.append(i)
print(l)


# 3

# tuples - immutable => cannot be modified

t = ()
t = tuple()

l = [1,2,3,4,5]
t = tuple(l)
print(t)
print(type(t))

t = [1,2,3,[123,34,56],"hi","hello",[12.3,23.5,"jk",[1234,3456]],(321,432,(576,8676))]
print(t[7][2][0])

t = (1,) # add comma to make it tuple

t = (12,31)
n = 5
for i in range(n):
    d = int(input())
    dt = (d,)
    t = t + dt
    print(t)

t = (0,) * 100
print(t)


# 4. sets

art_friend = {"Rolf", "Anne"}
science_friend = {"Jen", "Charlie"}

art_friend.add("Jen")

print(art_friend)

art_friend.remove("Jen")

print(art_friend)


# 5. advanced set


art_friend = {"Rolf", "Anne","Jen"}
science_friend = {"Jen", "Charlie"}

art_but_not_science = art_friend.difference(science_friend)
science_but_nor_art = science_friend.difference(art_friend)

print(art_but_not_science)
print(science_but_nor_art)

not_in_both = art_friend.symmetric_difference(science_friend)
print(not_in_both)

art_and_science = art_friend.intersection(science_friend)
print(art_and_science)

all_friends = art_friend.union(science_friend)
print(all_friends)


# 6. PYTHON DICT

#key-value

friend_ages = {"Rolf":24, "Adam":30, "Anne":27}
print(friend_ages["Rolf"])

friend_ages["Bob"] = 20
friend_ages["Rolf"] = 40

print(friend_ages)

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne an", "age": 27},

)


print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

friends = [("Rolf",24),("Adam",30),("Anne",27)]
friend_ages = dict(friends)
print(friend_ages)



# iexplore

# 1
# Which of the following are true for objects of Python’s set type:
# [Note: Select two or more options]
# - A given element can't appear in a set more than once
# - sets are mutable

#  can add or remove elements from a set after it has been created. However, the elements within a set must be immutable (e.g., integers, strings, tuples) because sets are implemented as hash tables and require hashable elements.


# 2
# Which of these about a frozenset is not true?
# -> mutable data type

# A frozenset is an immutable version of a set in Python. Unlike a regular set, you cannot modify a frozenset after it has been created. This means you cannot add or remove elements from a frozenset. However, like regular sets, frozensets support set operations such as union, intersection, difference, and symmetric difference.

# Key Characteristics of frozenset:
# Immutable: Once created, the elements of a frozenset cannot be changed.
# Hashable: Because they are immutable, frozensets can be used as keys in dictionaries or as elements of other sets.
# Unordered: frozensets, like regular sets, do not maintain order.


# 3
# What is the result of this statement?
print({1,2,3,4,5}-{3,4}^{5,6,7})
# -> {1, 2, 6, 7}

# The operators - (difference) and ^ (symmetric difference) are involved. According to Python's operator precedence, the set difference - is evaluated before the symmetric difference ^.
# {1, 2, 3, 4, 5} - {3, 4}
# This removes the elements 3 and 4 from the first set.
# Result: {1, 2, 5}

# {1, 2, 5} ^ {5, 6, 7}
# Symmetric difference returns elements that are in either of the sets, but not in both.
# {1, 2, 5} ^ {5, 6, 7} includes all elements from both sets except 5, which is present in both sets.
# Result: {1, 2, 6, 7}


# 4
# What will be the output?
my_tuple = (1, 2, 3, 4)
my_tuple.append( (5, 6, 7) )
print(len(my_tuple))
# -> error as tuple is immutable
# AttributeError: 'tuple' object has no attribute 'append'


# 5
# What is the correct syntax of converting a set into a frozen set?
# given:  set([5,6,7]). 
# -> rozenset({5,6,7})


# 6
Is the following piece of code valid?
a={1,2,3}
b={1,2,3,4}
c=a.issuperset(b)
print(c)
# -> valid
# c = a.issuperset(b): The issuperset method checks if set a contains all elements of set b.
# Set Relationship:
# For a to be a superset of b, every element of b must be present in a.
# a.issuperset(b) returns False.


# 7
# What is the result of this statement? 
print({'b','a','r'} & set('qux'))
# -> set()
# Create the Sets:
# {'b', 'a', 'r'} is a set containing the characters 'b', 'a', and 'r'.
# set('qux') converts the string 'qux' into a set of its characters:
# 'qux' becomes {'q', 'u', 'x'}.
# Find the Intersection:
# The & operator finds the intersection of two sets, i.e., it returns a set of elements that are common to both sets.
# Result:
# The intersection of the two sets is an empty set.
# set()  # or equivalently, {}


# 8
# What is the output of the following code?
a=(1,2,3,4)
del(a[2])
# -> Error as tuple is immutable


# 9
# Which of the following define the set {'a', 'b', 'c'}:
# [Note: Select two or more options]
# -> s = set(['a', 'b', 'c'])
# -> s = {('a', 'b', 'c')}
# -> s = set('abc')


# 10
# You have a set s defined as follows:
s = {100, 200, 300}
# Which one of the followi/ng statements does not correctly produce the union of s and the set {300, 400, 500}:
# -> s | [300, 400, 500]


#iAna;yse

# 1
# What will be the output?
d = {"john":40, "peter":45}
"john" in d
# -> True

# 2
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}
print(set1.issubset(set2))
print(set2.issuperset(set1))
# -> True, True


# 3
x = {1, 2, 3}
y = {1, 2}
#print(y.ispropersubset(x))


print(a & b <= a and a & b <= b )

a = (1,2,3)
b = ("A","B","C")
c = zip(a,b) #returns Zip Object
print(list(c))

s ={"foo", "bar", "baz", "qux"}
s.discard("bar")
print(s)
s &={"foo", "baz", "qux"}
print(s)
s -= {"bar"}
print(s)
#del s["bar"]
print(s)

a = (1,2,3,4)
print(sum(a,3))

a = (0,1,2,3,4)
b = slice(0,2)
print(a[b])

a = (1,2,(4,5))
b = (1,2,(3,4))
print(a<b)
'''

# i design
'''
# 1
name = str(input())
n = int(input())


if 0 < n <= len(name):
    listword = list(name)
    listword.pop(n-1)
    #print(listword)
    latestname = ""
    for char in listword:
        latestname += char
    print(latestname)
else:
    print()
'''
'''
# 2

word = input()


reverse_word = word[::-1]
if word == reverse_word:
    print(word)
else:
    palindrome = ""
    if len(word) > 1:
        for i in range(len(word)):
            if word[i] != word[-i]:
                word[-i] == word[i] 
            else:
                palindrome = palindrome + word[i]
    else:
        palindrome = word.upper()
        
    print(palindrome)

'''
words = input()
length = len(words)
if words[::-1] == words:
    print(words)
else:
    half_lenght = int(length / 2)
    if length % 2 != 0 :
        new_word = words[:half_lenght + 1] + words[half_lenght - 1 :: -1]
        print(new_word)
    else:
        new_word = words[:half_lenght] + words[half_lenght - 1 :: -1]
        print(new_word)

'''
Example 1: Palindrome Input
Input: racecar

length = 7
words[::-1] == words is True because racecar reversed is racecar.
Output: racecar
Example 2: Non-Palindrome Input
Input: hello

length = 5
words[::-1] == words is False because hello reversed is olleh.
HL = 2 (since int(5 / 2) is 2)
length % 2 != 0 is True because 5 % 2 is 1.
new_word = words[:HL + 1] + words[HL - 1 :: -1]
words[:HL + 1] is words[:3] which is hel
words[HL - 1 :: -1] is words[1::-1] which is eh (substring from index 1 to 0, inclusive, in reverse)
new_word = "hel" + "eh" = "heleh"
Output: heleh

'''
     
'''
# 3

number = int(input())

for num in range(4):
    right = "/" * number
    left = "\\" * number
    print(right,left,right,left, sep="")

'''
'''
# 4 

first_string = input("Enter the first string:\n")
second_string = input("Enter the second string:\n")

list_first_string = list(first_string)
list_second_string = list(second_string)

#print(list_first_string)
#print(list_second_string)

if first_string[0] == second_string[0]:
    print(first_string, second_string)
else:
    print("Invalid Input")
'''
'''
# 5

school_number = int(input())

students_number = []

list_student_number = []
for student in range(school_number):
    students_number = int(input())
    list_student_number.append(students_number)

book_price = int(input())

total_book = 0
for list_student in list_student_number:
    total_book = total_book +  list_student

total_cost = total_book * book_price

print(f"Total number of books required : {total_book}")
print(f"Total cost: {total_cost}")
'''
'''
# 6
set1 = input().split(',')
set2 = input().split(',')

list_set1 = set(set1)
list_set2 = set(set2)

if list_set1 == list_set2:
    print("invalid set")
else:
    difference = list_set1.symmetric_difference(list_set2)

    ordered_difference = []
    for item in set1 + set2:
        if item in difference and item not in ordered_difference:
            ordered_difference.append(item)
    
    
    difference_set = set()
    for i in ordered_difference:
        difference_set.add(int(i))
    print(difference_set)
'''
'''
# 7
# The format of the dates is like "Jul 1 2014 2:43 PM"(without quotes). '
from datetime import datetime

first_date = input()
second_date = input()

date_format = "%b %d %Y %I:%M%p"

date1 = datetime.strptime(first_date,date_format)
date2 = datetime.strptime(second_date,date_format)

#if date1 > date2:
#    date1,date2 = date2,date1

difference = date2 - date1

days = difference.days
seconds = difference.seconds
hours = seconds // 3600
seconds = seconds - (hours * 3600)
minutes = seconds // 60
seconds = seconds - (minutes * 60)

output = (f"{days} days, {hours}:{minutes:02}:{seconds:02}")
print(output)
'''
'''
# 8
sheet_number = int(input())

list_student_code = []
for number_student in range(sheet_number):
    student_code = input().split()
    students_tuple = tuple(map(int, student_code))
    list_student_code.append(students_tuple)

print(f"Attendance Sheets with Register Number: {tuple(list_student_code)} ")

register_number = set()
for number_tuple in list_student_code:
    register_number.update(number_tuple)
    
final_number = tuple(sorted(register_number))
print(f"Final sheet: {final_number}")

'''
# 9
'''
students = \
{
    "John"   :{"Exam mark": 65},
    "Paul"   :{"Exam mark": 68},
    "Ringo"  :{"Exam mark": 75},
    "George" :{"Exam mark": 76},
    "Fred"   :{"Exam mark": 63},
    "Wilma"  :{"Exam mark": 76},
    "Betty"  :{"Exam mark": 70},
    "Barney" :{"Exam mark": 60},
}
'''
'''
students = \
{
    "John"   :[65],
    "Paul"   :[68],
    "Ringo"  :[75],
    "George" :[76],
    "Fred"   :[63],
    "Wilma"  :[76],
    "Betty"  :[70],
    "Barney" :[60],
}
students_number = int(input())

for student in range(students_number):
    student_input = input().split(" ")
    name = student_input[0]
    marks = list(map(int,student_input[1:]))
    students[name] = marks

find_student = input()

if find_student in students:
    student_mark = students[find_student]
    find_mark = set(student_mark)

    if len(find_mark) == 1:
        marks = student_mark[0]
        print(f"{find_student} scored same marks in all subjects: {marks}")
    else:
        sort_mark = sorted(find_mark)
        second_highest = sort_mark[-2]
        print(f"Second highest mark of {find_student}: {second_highest}")

else:
    print("Students does not exist")

'''
'''
# 10

sentences = input()
words = sentences.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)
'''
'''
# iAssess_ 1
set1 = input()
set2 = input()

list_set1 = set(set1)
list_set2 = set(set2)

first = list_set1.issubset(list_set2)
second = list_set2.issubset(list_set1)
third = list_set1.issuperset(list_set2)
fourth = list_set2.issuperset(list_set1)
print(first,second,third,fourth,sep="\n")

'''
'''
# iAssess_2

passport_details = {}

number = int(input("Enter the number of clients\n"))

for num in range(1,number + 1):
    print(f"Enter the details of the client {num}")
    name = input()
    email = input()
    passport = input()

    passport_details[passport] = f"{name}--{email}--{passport}"

passport_search = input("Enter the passport number of the client to be searched\n")

if passport_search in passport_details:
    print("Client Details")
    print(passport_details[passport_search])
else:
    print("Client not found")
'''

# 5












