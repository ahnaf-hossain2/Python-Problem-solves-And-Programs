# --------------------------------------------------------------

#it converts an object to string
str(123) #output: '123'

# It capitalizes the first charachter of each word in string.
name = "ahnaf hossain"
print(name.title()) # output: "Ahnaf Hossain"

name = "Ahnaf"
# It returns the length of the string.
print(len(name)) # Output: 5

# It converts all characters to lowercase.This method is case-insensitive.
print(name.lower())  # Output: ahnaf

# It converts all characters to uppercase.
print(name.upper())  # Output: AHNAF

# It Capitalizes the first character of the string.
print(name.capitalize()) # Output: Ahnaf

# It removes all leading and trailing whitespace characters.
text = "  Hello  "
print(text.strip())  # Output:Hello

# It splits the string into a list where each word is a list item.
# this function splits the string into a list of substrings based on the specified separator.
text = "Hello,World"
print(text.split(','))  # Output: ['Hello', 'World']
text = "Hello World, Hello Python"
result = text.split('d')
print(result)  # Output: ['Hello Worl', ', Hello Python']


# It joins the list items into a single string with a specified separator.
words = ['Hello', 'World']
print(' '.join(words))  # Output: Hello World
chars = ['H', 'e', 'l', 'l', 'o']
word = ''.join(chars)
print(word)  # Output: "Hello"
numbers = ['1', '2', '3', '4', '5']
hyphenated_numbers = '-'.join(numbers)
print(hyphenated_numbers)  # Output: "1-2-3-4-5"


# It replaces a specified phrase with another specified phrase.
text = "Hello World"
print(text.replace('World', 'Python'))  # Output: Hello Python

# Returns the lowest index of the substring if found, otherwise -1.
# Here the black space is also considered a string character.
text = "Hello World"
print(text.find('World'))  # Output: 6

# It counts how much time the substring or characters appear in a string.  
text = "Hello World, Hello Python"
print(text.count('Hello'))  # Output: 2
text = "Hello World"
print(text.count('l'))  # Output: 3
# In this example, the count method only looks for occurrences of 'Hello' from index 0 to 11 (up to but not including index 12) in the string.
text = "Hello World, Hello Python"
print(text.count('Hello', 0, 12))  # Output: 1

# Checks if the string starts with the specified prefix.
text = "Hello World"
print(text.startswith('Hello'))  # Output: True

#Checks if the string ends with the specified suffix.
text = "Hello World"
print(text.endswith('World'))  # Output: True
