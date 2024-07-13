# video 1 dictionary introduction

'''dictionary:
key - value

key
1) unique
2) immutable
3) cannot be None

value
1) not need to be unique
2) can be None
3) can be mutable data

d = {}
d = dict{}'''

d = {\
     "name" : "JK", 
     "age": 25, 
     "rollNo": 12345,
     "weight": 80.5,
     "subject": ["Maths","Science"],
     "Address":
        {"DNo": 5213,
         "SName": "1st cCross", 
         "City": "Cbe",
         "PinCode": 620014
        }}

print(d)
print(d["name"])
print(d["address"])
print(d["address"]["City"])
print(d["subject"][0])
print(d["subject"][1])


# video 2 dictionary functions

'update value'

d["age"] = 27
print(d)

d["height"] = "5.7"
print(d)

'delete'

del(d["weight"])
print(d)
del(d)

d = {1:"int",2.4:"float", (12,23):"tuple", "name":"str",2+3j:"complex"}

for i in d:
    print(i,d[i],sep="") # i is just key. d[i will print their value]
    
d = {12:"qwe", 123:"dfd", 1234:"ssd"}

for i in sorted(d): # => sorted list
    print(i, d[i],sep="-")

d.pop(12) # => remove something
print(d)

d.popitem()
print(d)


#video 3 set introductions

'''sets 
1) unordered - hashing
2) unindexed
3) no duplicate elements
4) elements should be immutable // cannot have list,dict because it is mutable, but can have tuple
s ={} => cannot use this. it will refer to the dictionary class
s = set{} => should write like it'''

l = [1,202,34,14,5,6,7,1,2,3,4]
s = set(l)
print(l)
print(s)

for i in s:
    print(i)

for i in sorted(s):  # make it sort in ascending order
    print(i)

s = {12,23,43,12,34}
print(s)
s.add(123)
print(s)

'or'

s1 = {234,345,567}
s.update(s1)
print(s)


'remove'

s = {12,23,43}
s.remove(12)
print(s)
s.remove(56) # key error because element does not have in the set
print(s)


s = {12,23,43}
s.discard(56) #s same as remove but if element are not in the set, it will print nothing
print(s)

s.pop() # random element will be remove
print(s)

s.clear()
print(S)

del(s)
print(s) # error as s already deleted


# video 4 set operations

'''union
intersection
difference
symmetric difference'''

s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {2,4,6,8,10,12,14,16,18,20}
print(s1.union(s2))
print(s1)

print(s1.intersection(s2))
print(s1)
print(s1.intersection_update(s2))

print(s1.difference(s2))

print(s1.symmetric_difference(s2))

'''subset
superset'''

s1 = {1,2,3,4,5,6,7,8,9,10} 
s2 = {2,4,6,8,10} 

print(s1.issuperset(s2)) #-> true
print(s1.issubset(s2)) #-> false
print(s2.issuperset(s1)) #-> false
print(s2.issubset(s1)) #-> true

# if both sets have same elements, everything will be true
# if both sets have different elements, everything will be false

'''disjoint => true if both element not have same element between each other'''