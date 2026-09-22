# Function + List
# Create a function that recieves a list of numbers and returns the largest.

def find_largest(numbers):
    largest = 0
    for i in numbers:
        if i > largest:
            largest = i
    return largest

num = [3,6,1,6,11,26]
print(find_largest(num))

# Function + Dictionary
# Create a function, this should show the the values of the keys of the dictionary that you created in the main.


def show_student(student):
    for i in student:
        print (f"{i} : {student[i]}")

student = {
    "name" : "Ahnaf",
    "age" : 22,
    "department" : "CSE"
}

show_student(student)
print()

# Create a function that receives a list and returns a set containing only unique values.

def unique_set(num_list):
    unique_num = set(num_list)
    return unique_num

n_list = [1,223,4,5,2,2,5,5,3,3,6,7,20]
print(unique_set(n_list))
print()

"""
Create a function: find_number(numbers, target)
If target exists in the list, return the target.
If it doesn't exist, return None.
"""

def find_number(numbers, target):
    if target in numbers:
        return target
    else:
        return None

num = [22,55,1,4,6,8,100]
print(find_number(num, 1))
print(find_number(num, 11))
print()

"""
Create a dictionary:
Create a function that receives the dictionary and returns the average marks.
"""

def avg(student):
    sum = 0
    for i in student["marks"]:
        sum = sum + i
    avgmarks = sum/ len(student["marks"])
    return avgmarks

student = {
    "name" : "Ahnaf",
    "marks" : [80, 86, 90, 78]
}

print(avg(student))
