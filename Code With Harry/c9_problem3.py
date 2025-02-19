'''
Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
Place these files in a folder for a 13 – year old.
'''

def generateTable(i):
    table = ""
    for j in range(1, 11):
        table += f"{i} x {j} = {i*j}\n"
    with open(f"Python-Problem-solves-And-Programs/Code With Harry/13 year old/table_{i}.txt", "w") as file:
        file.write(table)
    return table

for i in range(2, 21):
    print(f"Table of {i} is:\n{generateTable(i)}")
