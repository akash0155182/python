import math
l=[]
l1=[]
num=int(input("enter the how amny no you want to input::"))
for n in range(num):
    x=int(input(f"enter the {n+1}element::"))
    l.append(x)
print("created list",l)
for i in l:
    sum=0
    for j in str(i):
        sum=sum+int(j)**3

    if(sum==i):
        l1.append(i)
print("largest number::",max(l1))
print("smallest number::",min(l1))





     