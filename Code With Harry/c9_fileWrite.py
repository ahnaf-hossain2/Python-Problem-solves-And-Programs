message = "hello I am Ahnaf Hosasin. And you? How are doing? "
file = open("Python-Problem-solves-And-Programs/Code With Harry/name.txt", "w")
file.write(message)
file.close()

f = open("Python-Problem-solves-And-Programs/Code With Harry/name.txt")
data = f.read()
print(data)
f.close()
