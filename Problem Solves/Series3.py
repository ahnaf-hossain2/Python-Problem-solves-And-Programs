# sum of odd numbers 1 + 3 + 5 + ..... + n

n = int(input("Enter value for n: "))
sum = 0
for i in range (1,n+1,2):
    print (i, end=" ")
    sum = sum + i
print ("\nSum of odd numbers from 1 to",n,"is = ",sum)
