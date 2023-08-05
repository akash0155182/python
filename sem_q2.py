l=list(eval(input("enter the elements")))
print("original list",l)
for i in range (len(l)):
    if l[i]%2!=0:
        for j in range (i+1,len(l)):
            if l[j]%2==0:
                l[i]=l[j]
                break      
print("list",l)