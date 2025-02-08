# Create an interactive coffee shop ordering system that welcomes customers,
# takes their name, displays a menu, processes their order with quantity,
# calculates the total, and provides a personalized order confirmation.
#------------------------------------------------------------------------

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

# Price of a coffee (in dollars)
price = 5

quantity  = input("How many coffees would you like to order?\n")
# As the quantity is saved as a string, we need to convert it to integer.
total = price * int(quantity)

# Confirm the order
# Now quantity and total are integers. So an integer and a string can't be added together
# So we need to convert them to string.
print("Sounds good, " + name + "! We'll have your " + str(quantity)
    + " " + order + " coffee ready for you in a moment.\n And your total will be $" + str(total))
