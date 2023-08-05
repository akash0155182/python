n=int(input("enter the no"))
l1,l2,l3=[],[],[]
for i in range (n):
    num1=int(input("enter the number"))
    l1.append(num1)
print(l1)
for i in range (n):
    num2=int(input("enter the number"))
    l2.append(num2)
print(l2)
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)


