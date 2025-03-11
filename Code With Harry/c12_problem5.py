num = int(input("Enter a number: "))

multiplication_table = [num*i for i in range(1, 11)]

with open("Python-Problem-solves-And-Programs/Code With Harry/multiplication_table.txt", "w") as f:
    f.write(str(multiplication_table) + "\n")
