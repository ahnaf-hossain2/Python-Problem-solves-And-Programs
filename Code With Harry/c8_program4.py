'''
***
**
*
for n = 3
'''

def pattern(n):
    if n == 0:
        return
    else:
        print('*' * n)
        pattern( n-1 )

n = int(input('Enter the number of rows: '))
pattern(n)
