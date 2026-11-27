# Loop :

# for i in range (11):
#     print(i,end=" ")

# print()

# for i in range(4,22):
#     print(i,end=" ")

# print()

# for i in range(4,22,2):
#     print(i,end=" ")

# print()

# for i in range(0,-102,-2):
#     print(i,end=" ")

# print()

# Slicing :
# Marks = [99, 55, 66, 88, 7, 79]
# Marks[4]=100
# for i in Marks:
#     print(i, end=" ")

# print(Marks[1:5])

# Array and Matrix:

# for i in range(3):
#     for j in range(4):
#         print("(,i),(j,))",end=" ")
#     print()

# Function:

# def greeting(name):
#     return f"Hello {name} how are you ?"

# print(greeting("Ahnaf"))


# x = [22.4,55.6,77.8]
# y=[]

# for i in x:
#     y.append(i)

# print(y)

# def incremetList(l3):
#     l2=[]
#     for i in l3:
#         l2.append(i+4)
#     return l2

# l1 = [1,2,3,4,5]
# print(incremetList(l1))


# def adissioList(l3,l4):
#     sum = 0
#     for i in range(len(l3)):
#         sum = sum + (l3[i]+l4[i])
#     return sum

# l1 = [1,2,3,4,5]
# l4 = [1,2,3,4,5]
# print(adissioList(l1,l4))

import math

def dotProduct(A,B):
    sum = 0
    for i in range(len(A)):
        sum = sum+(A[i]*B[i])
    return sum

def magnitude(A):
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i]**2
    magnitude = math.sqrt(sum)
    return magnitude

def angle(A,B):
    return math.acos(dotProduct(A,B)/(magnitude(A)*magnitude(B)))

A = [2,3]
B = [5,6]
# print(dotProduct(A,B))
# print(magnitude(A))
print(angle(A,B))
