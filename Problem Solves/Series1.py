# 1 + 2 + 3 + ..... + n series
n = int(input("Enter the range(n): "))
sum = 0
for i in range (1,n+1):
    print(i,end=" ")
    sum = sum + i
print("\nSum = ",sum)
