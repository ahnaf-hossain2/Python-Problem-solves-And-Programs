# Series: 1^2 + 2^2 + 3^2 +......+ n^2

n = int(input("Enter n: "))

sum = 0
for i in range(1,n+1):
    print(str(i)+"^2",end=" ")
    sum+= i**2
print("\nSum:",sum)
