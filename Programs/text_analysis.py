text = input("Enter your text: ")

numOfLetters = 0
numOfWords = 0
numOfDigits = 0
for n in text:
    n.lower()
    if n >= 'a' and n <= 'z':
        numOfLetters+=1
    elif n >= '0' and n <= '9':
        numOfDigits+=1
    elif n == ' ':
        numOfWords+=1
print("Number of Letters: ",numOfLetters)
print("Number of words: ",numOfWords+1)
print("Number of Digits: ",numOfDigits)
