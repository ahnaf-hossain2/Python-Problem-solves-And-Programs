# print("Hello") #-> This is for printing
# Number = 5 #-> declare variable
# z = 1j # complex type
# print(type(Number)) #-> To know the type of the variable
# if (5>2): #-> If condition
#     print("Bigger") #-> Indentation Must follow
# print("Hello"); print("World"); print("Bye") #To write multiple statements in one line
"""
# print("Hello world", end=" ") #end to print in the same line
# print("This will print in the same line")
""" # this is for multiline comment.
# print("I am", 22, "years old.") #combine int and string
#x, y, z = 5, 6, 7 # Assign many values to multiple variables
# x, y, z = 10 # one value to multiple variables

''' # Unpack a collection
age = [21,33,29]
x, y, z = age
print(x, y, z) # output: 21, 33, 29
'''

"""
x = 10 # global variable can be used by everyone
y = 5
def addition():
    print(x+y) # 10 + 5
def sub():
    y = 2
    print(x-y) # 10 - 2
addition()
sub()
print("This is outside of func: ", y)
"""

"""
x = 10 # global variable
def changeGlobal():
    global x # to change the global variable
    x = 11
    print(x)

changeGlobal()
"""

# str = "My name is 'Ahnaf' " # quotes under quotes

'''
str = """ hello
    this is
    Multiline string
    """ # use 3 quotes to use multiline string
'''

# Strings are arrays
# name = "Ahnaf"
# print(name[1])
# for x in name: # looping in string
#     print(x)
# print(len(name))
# print('N' in name) # checks if N is present in name string
# print ('N' not in name) # check if not
# print(name[1:3]) # get the characters from position 1 to 3(not included)
# print (name[:5])

# age = 21
# print(f"I am {age} year's old")

# x = 2
# y = 5
# print (x**y) # power

# num = 10
# x = "Big" if num > 5 else "Small"

cars = ["BMW", "Audi", "Ferrari", "Toyota", "Honda"]
# print(cars[-2]) #Audi
# print(cars[0]) #BMW
# print(cars[-4:-1]) # -1 excluded
# cars[3] = "Suzuki"
# cars[1:3] = ["Mazda", "Hyundai"]
# cars.insert(3, "Kitty")
# cars.append("NewCAr")

# carEx = ["Pagani", "Porshe"]
# cars.extend(carEx)
# print(cars)
# cars.remove("Audi")
# cars.pop(1) #removes index 1 item
# cars.pop() #removes last item
# del cars # completly deletes cars list
# cars.clear # clears the list contents but the list stay
