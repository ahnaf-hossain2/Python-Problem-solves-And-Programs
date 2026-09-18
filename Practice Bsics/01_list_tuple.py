# Print:

# the first fruit
# the last fruit
# the number of fruits

fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0], fruits[3])
print(len(fruits))
print()

# Create a list of 3 subjects:
# Add "English" to the list and print the list.

Subjects = ["Math","Physics","CSE"]
Subjects.append("English")
print(Subjects)
print()

# List — Change Item
# Change 30 to 50 and print the list.

numbers = [10, 20, 30, 40]
numbers[2] = 50
print(numbers)
print()

# Tuples cannot be changed
# Create a tuple containing 5 numbers and print its length.
# Tuple — Access
# Print the second and fourth colors

colors = ("red", "green", "blue", "yellow")
print(colors[1], colors[3])
print(len(colors))
print()

"""
List + Loop
Use a for loop to print every number in a list
"""

# will loop the numbers list from above:
for i in numbers:
    print(i)
print()

"""
List + Sum
Calculate and print the total without using sum().
"""

sum = 0
for i in numbers:
    sum = sum+i
print(sum)

print()
