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
# 5. advanced set


art_friend = {"Rolf", "Anne","Jen"}
science_friend = {"Jen", "Charlie"}

art_but_not_science = art_friend.difference(science_friend)
science_but_nor_art = science_friend.difference(art_friend)

print(art_but_not_science)
print(science_but_nor_art)

