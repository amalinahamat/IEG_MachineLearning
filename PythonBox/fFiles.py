# files
'''
open("filename", "mode and format") => open the file

mode and format

mode: 
r - read
w - write  // if not have file creates a new file, if have, rewrite all in the file
a - append // add more content to the existing file, if not have file creates a new file
x - exclusive //  create a new file only if the file does not exist. it through errors if the file exists.

format:
t - text
b - byte

read -> read the
readline -> read the firstline
readlines ->

write
writelines



'''
f = open("input.txt","rt")
# f = open("input.txt","r")
# f = open("input.txt","rt")
# f = open("input.txt","t") -> wrong
# f = open("input.txt")

#s = f.read()
#s = f.read(10)
'''
s = f.readline()
print(s)
s = f.readline()
print(s)
s = f.readline()
print(s)
'''

# sl = f.readlines()
# print(sl)
'''
f = open("sample.txt","w")

t = "Python programming\n"
s = "Welcome all\n"
sl = ["Google\n","Amazon\n","Amphisoft\n","Apple\n"]
f.write(t)
f.write(s)
f.writelines(sl)


f = open("text.txt","a")

'''
'''
# sum method

f = open("text.txt")
l = f.readlines()
print(l)
sum = 0
for s in l:
    sum = sum + int(s)

print("sum = ", sum)

'''
'''
Assignment:
file format is (mark studentName)
94 jk
96 sam 
90 arun
80 mike

add 93 govind between index 0 and 1
'''
'''
f = open("input.txt")
l = f.readlines()
print(l)
s = "93 govind"
l.insert(1,s+"\n")

f = open("input.txt","w")
f.writelines(l)

'''
'''
import os
os.rename("sample.txt","content.txt") # change the filename
os.remove("") # to remove the file
'''
'''

fo = open("foo.txt","rw+")
print("Name of the file:",fo.name)

for index in range(5):
    line = fo.next()
    print("Line No %d - %s" %(index,line))

fo.close
'''
'''
fo = open("input.txt")
line = fo.readline()
print(line)
pos = fo.tell()
print("Current Position:"+str(pos))
fo.close()
'''
# idesign
# 1
'''


file_path = open("averageLength.txt","rt")
text = file_path.read()
if len(text) > 0: 
    words = text.split()
    if len(words) > 0:
        total_length = sum(len(word) for word in words)
        average_length = total_length / len(words)
        print(int(average_length))
else:
    print("0")

'''
# 2
'''

#file_path = open("sample.txt","w")
#t = "1\n2\n3\n4\n5\n"
#ile_path.write(t)

file_path = open("sample.txt","rt")
number = file_path.readlines()
#print(number)
total_sum = 0
for s in number:
    total_sum = total_sum + int(s)

print(f"The sum of the integers in the file sample.txt is:{total_sum}")

'''
'''
# 3
file_path = open("input.txt","rt")
file = file_path.readlines()
file_path.close()

total_lines = len(file)

print(f"The file has {total_lines} lines")
'''
'''
# 4

file_path = open("input.txt","rt")

content = file_path.read()

reverse_content = content[::-1]

file_reverse_path = open("output.txt","w")

file_reverse_path.write(reverse_content)

print(reverse_content)

'''

# 5

file_path = open("SalariesDataSet.csv","rt")

content = file_path.read()

modified_content = content.replace(",",";")

print(modified_content)




















