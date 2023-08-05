def power(a,b):
    if b==0:
       return 1
    else:
        return a*power(a,b-1)
a,b=eval(input('enter value of a and b: '))
print(power(a,b))
