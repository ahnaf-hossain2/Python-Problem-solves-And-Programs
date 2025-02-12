lst = [-5, 0, 7, -2, 10, -1]
new=["Negative" if digit<0 else "Positive" if digit>0 else digit for digit in lst]
print(new)


"""
num = [7,-25, 0, -18, -0, 7]
output = []

for i in num:
    if i < 0:
        output.append("negative")
    elif i > 0:
        output.append("positive")
    else:
        output.append(0)

print(output)
"""
