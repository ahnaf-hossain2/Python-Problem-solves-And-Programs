''' Before Python 3.8
n = [1,2,3,4,5]
if len(n) > 3:
    print("List is greater than 3")
'''

if (n := len([1,2,3,4,5])) > 3:
    print (f"List is greater than 3 and length is {n}")
