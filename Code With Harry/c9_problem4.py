word = "Donkey"
with open("Python-Problem-solves-And-Programs/Code With Harry/replace.txt", "r") as file:
    content = file.read()
contentNew = content.replace("Donkey", "#####")

with open("Python-Problem-solves-And-Programs/Code With Harry/replace.txt", "w") as file:
    file.write(contentNew)
    file.close()
