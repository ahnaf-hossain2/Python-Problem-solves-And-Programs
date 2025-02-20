with open("Python-Problem-solves-And-Programs/Code With Harry/this.txt") as file:
    content1 = file.read()

with open("Python-Problem-solves-And-Programs/Code With Harry/name.txt") as file:
    content2 = file.read()

if content1 == content2:
    print("The files are same")
else:
    print("The files are different")
