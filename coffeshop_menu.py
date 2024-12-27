# Prompt for user's name and welcome them
print("Hello, welcome to Grand Coffee!!!")
name = input("What is your name?\n")

# Welcome message
print("Hello, " + name + ". Thank you so much for coming in today.\n\n\n")

# Menu items
menu = "Coffee, Espresso, Latte, Cappuccino"
print(name + ", what would you like from our menu today? Here is what we are serving: " + menu)

# Take the user's order
order = input()

# Confirm the order
print("Sounds good, " + name + "! We'll have that " + order + " ready for you in a moment.")