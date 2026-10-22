# Logical operators :


a = 20
b = 44
c = 9

print((a>b)&(a>c))
print((a>b)and(a>c))

print((a>b)or(a>c))
print((a>b)|(a>c))


# Array or List:

List = [10,20,30,25,13,40,50]
print(type(List))
print(List[0])
List.append(60)
print(List)
List.sort()
List.pop()
print(List)
print(len(List))
print(List[-1]) ## Last index
print(List[-2])
print(List[1:5]) ## Excludes 5th index. Prints 1 to 4 index.
