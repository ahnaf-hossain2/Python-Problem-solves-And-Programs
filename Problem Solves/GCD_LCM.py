num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
n1 = num1
n2 = num2

while num2 != 0:
    rem = num1 % num2
    num1 = num2
    num2 = rem
print("GCD: ",num1)
print("LCM: ",((n1*n2)/num1) )
