choice=input('b: for binary\no:for octal\nh: for hexadecimal::')
if choice=='b':
    b_num=int(input('enter the number:'))
    count=0
    s=0
    while b_num!=0:
        n=b_num%10
        #s+=n*2**count
        s+=n<<count
        count+=1
        b_num=b_num//10
    print(s)
elif'o'==choice:
    o_num=int(input('enter the number:'))
    count=0
    s=0
    while o_num!=0:
        n=o_num%10
        s+=n*8**count
        count+=1
        o_num=o_num//10
    print(s)
elif'h'==choice:
    h_num=input('enter the number:')
    extra={'a':10,'A':10,'b':11,'B':11,'c':12,'C':12,'d':13,'D':13,'e':14,'E':14,'f':15,'F':15}
    count=0
    s=0
    for i in h_num[::-1]:
        if i in extra:
            value=extra[i]
        else:
            value=int(i)
        s+=value*16**count
        count+=1
        
    print(s)
else:
    print('wrong choice')

