'''
    *
   **
  ***
 ****
*****
'''

n = int(input("Enter line number: "))
for i in range(n+1):                    # here the main loop wil run from 1 upto n
    for j in range(n-i):                # here the space will print (n-i) time to get our destinated pattern
        print(" ",end="")
    for k in range(i):                  # here the star will be print i times which will be from 1 to n times stepwise
        print("*",end="")
    print()                             # here it will help to go into a new line for each main loop happens
