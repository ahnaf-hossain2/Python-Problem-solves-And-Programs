# series : 1.5 + 2.5 + 3.5 + ..... + n

n = float(input("Enter n: "))
sum = 0
i = 1.5
while i <= n:
    print(i, end=" ")
    sum+=i
    i+=1
print("Sum: ",sum)
