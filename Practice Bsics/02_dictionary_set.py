"""
Dictionary — Access Values
Print: name, age, department
Add Data - ABC University
"""
student = {
    "name" : "Ahnaf",
    "age" : 22,
    "department" : "CSE"
}

student["name"] = "MD. Ahnaf Hossain"
student["university"] = "ABC University"

print(student["name"], student["age"], student[ "department"], student["university"])
print()

"""
Set — Create
Create a set containing: 1, 2, 3, 4, 5 also use duplicates
Print the set.
"""

numbers = {1,2,2,3,5,4,5,1} # only 1,2,3,4,5 will be printed
print(numbers)
