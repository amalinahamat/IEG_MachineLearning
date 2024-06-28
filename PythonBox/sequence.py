# video
'''
# 1
l = [1,2,3,[123,34,56],"hi","hello",[12.3,23.5,"jk",[1234,3456]]]

print(l[5])
print(l[3])
print(l[6])
'''
'''
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

'''
'''
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
'''
'''
# 4. sets

art_friend = {"Rolf", "Anne"}
science_friend = {"Jen", "Charlie"}

art_friend.add("Jen")

print(art_friend)

art_friend.remove("Jen")

print(art_friend)
'''
'''
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
'''

'''
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

'''
'''
# iexplore
print({1,2,3,4,5}-{3,4}^{5,6,7})

a = {1,2,3}
b = {1,2,3,4}
c = a.issuperset(b)
print(c)

print({'b','a','r'} & set('qux'))


s = set(['a', 'b', 'c'])
print(s)
s = {('a', 'b', 'c')}
print(s)
#s = set('a', 'b', 'c')
print(s)
s = set('abc')
print(s)

s = {100, 200, 300}

s | set([300, 400, 500])
print(s)

s.union(set([300, 400, 500]))
print(s)

s.union([300, 400, 500])
print(s)

#s | [300, 400, 500]
print(s)

# i analyse

d = {"john":40, "peter":45}
print("john" in d)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}
print(set1.issubset(set2))
print(set2.issuperset(set1))

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

# 6
