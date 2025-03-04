class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class Vector3d(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = Vector2D(1, 2)
b = Vector3d(1, 2, 3)

a.show()
b.show()
