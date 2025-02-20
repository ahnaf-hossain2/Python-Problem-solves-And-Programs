with open("Python-Problem-solves-And-Programs/Code With Harry/this.txt") as file:
    content = file.read()

with open("Python-Problem-solves-And-Programs/Code With Harry/copy.txt", "w") as file:
    file.write(content)
    file.close()
