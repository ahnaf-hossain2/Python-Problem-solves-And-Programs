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
