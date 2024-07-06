a = input("Enter 3 number: ")
print(a)
al = a.split(" ") #can also write without double quotation al = a.split()
print(al)
e,f,g = map(int, al)
print(e,f,g)
print(type(e))

e,f,g = map(int, input().split(" "))

a =  12.3455
print("%f"%a)

a =  12.3455
print("%.2f"%a)

m = 12.345
n = 123
o = "hi"
print("%f"%m)
print("%.2f"%m)
print("%d - %.3f : %s"%(n,m,o))