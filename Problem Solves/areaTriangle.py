''' Method 1:
Basic method to find the area of Triangle--->

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))

area = 0.5 * base * height
print("The area of Triangle is: ", area)
'''
''' Method 2:
class Triangle:
    # base = "" not needed to declare here
    # height = ""

    def __init__ (self, base, height):
        self.base = base
        self.height = height

    def display(self):
        area = 0.5 * self.base * self.height
        print("The area of Triangle is: ", area)

T1 = Triangle(10, 20)
T2 = Triangle(20, 30)
T1.display()
T2.display()
'''
''' # Method 3:
class Shape:
    def __init__ (self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    # Don't need to override this method in the child class
    # def area(self):
    #     print("This is area")

class Triangle(Shape):
    def area(self):
        return 0.5 * self.dim1 * self.dim2

class Rectangle(Shape):
    def area(self):
        return self.dim1 * self.dim2

T = Triangle(10, 20)
R = Rectangle(10, 20)

print("Area of Triangle: ", T.area())
print("Area of Rectangle: ", R.area())
'''
Method 4:
from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__ (self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        # this is a abstract method that must be overridden in a subclass
        pass # this is a null statement

class Triangle(Shape):
    def area(self):
        return 0.5 * self.dim1 * self.dim2

# objects can't be created for abstract class
# S = Shape(10, 20)
# S.area()

T = Triangle(10, 20)
print("Area of Triangle: ", T.area())
