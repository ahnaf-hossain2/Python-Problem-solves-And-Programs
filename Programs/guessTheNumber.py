from random import randint

while True:
    guessNumber = int(input("Enter any number between 1 to 10: "))
    randomNumber = randint(1,10)
    if (guessNumber == randomNumber):
        print("You won!")
        break
    else:
        print(f"You lost! The correct number was {randomNumber}")
    again = input("Do you want to try again? (y/n): ")
    if (again == "y" or again == "Y"):
        print("Starting.....")
    elif (again == "n" or again == "N"):
        print("The game is over Give up on your dreams and 死ぬ! ")
        break
