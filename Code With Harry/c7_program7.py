'''
* * *
*   *
* * *
same :
* * * * *  this is i = 1
*       *  here wil always be 2 stars,
*       *  so the rest will be spaces'
*       *  that means if n == 5 then the number of spaces will be n - 2(the amount of stars)
* * * * *  this is n = 5
'''
n = int(input("Enter the number: "))
for i in range(1,n+1):
    if(i == 1 or i == n):
        print( "*" * n, end="")
    else:
        print("*",end="")
        print(" " * (n-2),end="")
        print("*",end="")
    print("")
