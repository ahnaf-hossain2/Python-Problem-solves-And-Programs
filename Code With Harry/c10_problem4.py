class Employee:
    def __init__(self):
        print("This is emplyoee class")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__() # This will call The Employee class constructor
        print("This is Programmer class")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__() # This will call both the Employee and Programmer class constructor because it inherited the Programmer class Which has inherited Employee class.
        print("This is Manager class")


# o = Employee()
# print(o.a)
# d = Programmer()
# print(d.b)
c = Manager()
print(c)
""" Output:
This is emplyoee class
This is Programmer class
This is Manager class
<__main__.Manager object at 0x0000028B2E7B7230>
"""
