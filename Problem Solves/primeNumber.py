n = int(input("Enter the value of n: "))

if (n == 0 or n == 1):
    print("Not Prime Number")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime Number")
