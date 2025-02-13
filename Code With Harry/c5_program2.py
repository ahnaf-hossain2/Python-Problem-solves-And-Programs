# numbers = set()
# for i in range(8):
#     print("Enter number",i+1,": ",end="")
#     take = int(input())
#     numbers.add(take)
# print(numbers)

# test = {18, '18'}
# test.add("hello")
# print(test, type(test))

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s, " Length is:",len(s))
