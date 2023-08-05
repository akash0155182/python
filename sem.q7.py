dict = {}
n = int(input("Enter the number of players: "))
for i in range(n):
    name = input("Enter name of player: ")
    score = int(input("Enter the score:" ))
    dict[name] = score
pname = input("Enter player name to retrieve his runs: ")
if pname in dict:
    print(pname,"has scored",dict[pname])
else:
    print("No records found!")
h = 0
for i in dict:
    if dict[i] > h:
        h = dict[i]
        nm = i
print(nm,"has scored the highest runs",dict[nm])
