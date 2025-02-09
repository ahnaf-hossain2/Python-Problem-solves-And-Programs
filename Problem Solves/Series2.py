# sum of even numbers 2 + 4 + 6 + ..... + n

n = int(input("Enter value for n: "))
sum = 0
for i in range (2,n+1,2):
    print (i, end=" ")
    sum = sum + i
print ("\nSum of even numbers from 2 to",n,"is = ",sum)
