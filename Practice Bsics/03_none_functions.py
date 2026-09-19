#  Creat a none variable and check if the result is none.

result = None
print(result is None)


"""
Create a function called hello() that prints: Hello, Python!
"""

def hello():
    print("Hello, Python!")

hello()


"""
Create a function with parameter prints your name:
"""

def greet(name):
    print(f"Hello {name}")

greet("Ahnaf")

"""
Create a function that calculates:
"""

def calculate(a,b):
    print(a+b)
    print(a-b)
    print(a/b)
    print(a*b)
    print(a**b)

calculate(57, 101.032)
