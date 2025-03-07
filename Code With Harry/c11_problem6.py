class Complex:
    # r = real part, i = imaginary part
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i) # this returns the sum of two complex numbers

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1, 2) # this creates a complex number 1 + 2i
c2 = Complex(3, 4)
print(c1 + c2) # this prints the sum of c1 and c2
