# Write a class "calculator" capable of finding square, cube and square root of a
# number.

class Calculator:
    @staticmethod # This method can be called without creating an object of the class
    def greet():
        print("Hello")
    def display(self, num):
        print(num ** 2)
        print(num ** 3)
        print(num ** 0.5)
        
number = Calculator()
number.greet()
number.display(5)
