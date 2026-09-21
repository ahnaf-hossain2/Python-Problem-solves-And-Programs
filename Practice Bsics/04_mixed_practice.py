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

