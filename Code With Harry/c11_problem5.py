class Person:
    def __init__(self, name):
        self.__name = name # this is a private variable

    @property
    def name(self):
        return self.__name # this is a getter method

p = Person("Ahnaf")
print(p.name) # used the getter method to get the private name variable
