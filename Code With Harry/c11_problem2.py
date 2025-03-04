class Animals:
    print("This is an Animal")

class Pet(Animals):
    print("This is a pet")

class Dog(Pet):
    print("This is a dog")
    @staticmethod
    def bark():
        print("Woof! Woof !")

Dog.bark()
