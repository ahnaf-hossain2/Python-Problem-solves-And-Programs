a = 5
b = 0

try:
    k = a/b
    print(k)

except ZeroDivisionError:
    print("You cannot divide a number by zero")
