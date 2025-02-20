'''
Basic method to find the area of Triangle--->

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))

area = 0.5 * base * height
print("The area of Triangle is: ", area)
'''

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
