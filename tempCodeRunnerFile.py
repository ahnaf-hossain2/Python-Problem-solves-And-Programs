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
