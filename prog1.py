with open("story.txt","r") as f:
    c=0
    a=0
    b=0
    for line in f:
        words=line.split()
        for i in words:
            if i=="the":
                c=c+1
            elif i=="is":
                a=a+1
            elif i=="are":
                b=b+1
print(a)
print(b)
print(c)