m=int(input("enter the no of rows: "))
n=int(input("enter the no of columns : "))
l,l1=[],[]
for i in range(m):
    for j in range(n):
        l.append(int(input("enter the no ")))
    l1.append(l)
    l=[]
for i in range(m):
    for j in range(n):   
        print(l1[i][j],end=' ')
    print()
print("reverse order: ")
for i in range(m-1,-1,-1):
    for j in range(n):
        print(l1[i][j],end=' ')
    print()
