class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        print(f"""Name:{self.name}
Age:{self.age}
Salary:{self.salary}""")

e1 = Employee("Ahnaf", 24, 150000)
e1.show()
