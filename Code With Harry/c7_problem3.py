num = int(input("Enter the number: "))

if (num == 0 or num == 1):
    print("Not a prime number")
else:
    for i in range(2,num):
        if num % 2 == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")
