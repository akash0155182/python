class father:
    def __init__(self,name,property):
        self.name=name
        self.property=property
    def display(self):
        print("Fathers name = ",self.name," and property =", self.property)
class son(father):
    def __init__(self,property1,name,property):
        super().__init__(name,property)
        self.property1=property1
    def display(self):
        super().display()
        print("Total child propery = ",self.property1+self.property)
s=son(200000.00,'Arun',800000.00)
s.display()