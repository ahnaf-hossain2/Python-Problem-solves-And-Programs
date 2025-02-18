'''
sum(1) = 1
sum(2) = 1+2 = 3
sum(3) = 1+2+3 = 6
sum(n) = 1+2+3+...+n
'''

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

n = int(input("Enter the number: "))
print(f"Sum of first {n} natural numbers is: {sum(n)}")
