# 1 + 2 + 3 + ..... + n series
n = int(input("Enter the range(n): "))
sum = 0
for i in range (1,n):
    print(i,end=" ")
    sum = sum + i
print("\nSum = ",sum)
