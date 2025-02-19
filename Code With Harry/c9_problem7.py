lineNo = 1
with open("Python-Problem-solves-And-Programs/Code With Harry/replace.txt", "r") as file:
    content = file.readlines()

for line in content:
    if ("Python" in line):
        print(f"Line {lineNo}: Python is present")
    else:
        print(f"Line {lineNo}: Python is not present")
    lineNo += 1
else:
    print("Python is not present")
