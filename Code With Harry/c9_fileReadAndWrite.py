message = "hello I am Ahnaf Hosasin. And you? How are doing? "
file = open("Python-Problem-solves-And-Programs/Code With Harry/name.txt", "w")
file.write(message)
file.close()

f = open("Python-Problem-solves-And-Programs/Code With Harry/name.txt")
data = f.read()
print(data)
f.close()

# Below code will create a file and write the data in it.
s = "Yo! wassup?"
n = open("Python-Problem-solves-And-Programs/Code With Harry/nyfile.txt", "w")
n.write(s)
n.close()
