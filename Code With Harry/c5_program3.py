dic = {}

for i in range(4):
    name = input("Enter friend name: ")
    lang = input("Enter language name: ")
    dic.update({name:lang})
print(dic)
