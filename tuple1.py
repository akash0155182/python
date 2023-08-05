t=()
n=int(input("enter the number of element::"))
for i in range(n):
    name=input("enter the name::")
    cgpa=float(input("enter the cgpa::"))
    t=t+((name,cgpa),)
    