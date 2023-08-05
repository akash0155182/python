class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Sarah", 29)
print(p1.name)
print(p1.age)

class Person:
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
p1=Person()
p1.name="Rahul"
p1.age=20
p1.display()