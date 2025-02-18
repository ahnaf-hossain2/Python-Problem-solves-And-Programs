file = open("Python-Problem-solves-And-Programs/Code With Harry/name.txt")
# lines = file.readlines()
# print(lines, type(lines))

# line1 = file.readline()
# print(line1)
# line2 = file.readline()
# print(line2)
# line3 = file.readline()
# print(line3)
# line4 = file.readline()
# print(line4)
# line5 = file.readline()
# print(line5 ) # This will print an empty string because there is no line left to read.
line = file.readline()
while (line != ""):
    print(line)
    line = file.readline()
file.close()
