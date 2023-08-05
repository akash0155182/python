sentence = "Hi My Name is"
a = 0

for c in sentence:
     if c.isupper():
         a = a + 1
     else:
         pass

print(a, " capital letters")

b = sum(1 for c in sentence if c.isupper())

print(b, " capital letters")