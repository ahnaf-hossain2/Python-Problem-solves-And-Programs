words = ["Donkey", "Kaddu", "Mote", "Ganda"]
with open("Python-Problem-solves-And-Programs/Code With Harry/replace.txt", "r") as file:
    content = file.read()
for word in words:
    content = content.replace(word, "#" * len(word))

with open("Python-Problem-solves-And-Programs/Code With Harry/replace.txt", "w") as file:
    file.write(content)
    file.close()
