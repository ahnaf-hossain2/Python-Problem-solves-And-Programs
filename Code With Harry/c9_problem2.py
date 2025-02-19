import random

def game():
    print("Welcome to the number guessing game!")

    # Generate a random score between 1 and 10
    score = random.randint(1, 10)

    # Fetch the previous highScore
    with open("Python-Problem-solves-And-Programs/Code With Harry/Hi-score.txt", "r") as f:
        highScore = f.read()
        if highScore == '':
            highScore = 0  # Set highScore to 0 if file is empty
        else:
            highScore = int(highScore)  # Convert highScore to integer

    print(f"The current score is {score}")

    # Check if the current score is higher than the highScore
    if score > highScore:
        # Write the new highScore to the file
        with open("Python-Problem-solves-And-Programs/Code With Harry/Hi-score.txt", "w") as f:
            f.write(str(score))
        print("New high score!")

    return score

# Start the game
game()
