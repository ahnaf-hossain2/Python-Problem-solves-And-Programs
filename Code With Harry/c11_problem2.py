class Animals:
    print("This is an Animal")

class Pet(Animals):
    print("This is a pet")

class Dog(Pet):
    print("This is a dog")

    def bark(self):
        print("Woof! Woof !")

tommy = Dog()
tommy.bark()
