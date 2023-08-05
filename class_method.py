class employee:
    company="camel"
    salary=100
    location="india"
    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal
e=employee()
print(e.salary)
e.changeSalary(450)
print(e.salary)
print(employee.salary)