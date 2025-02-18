import random

def game():
    print("Welcome to the number guessing game!")

    # Generate a random score between 1 and 10
    score = random.randint(1, 10)

    # Fetch the previous highscore
    with open("Python-Problem-solves-And-Programs/Code With Harry/Hi-score.txt", "r") as f:
        highscore = f.read()
        if highscore == '':
            highscore = 0  # Set highscore to 0 if file is empty
        else:
            highscore = int(highscore)  # Convert highscore to integer

    print(f"The current score is {score}")

    # Check if the current score is higher than the highscore
    if score > highscore:
        # Write the new highscore to the file
        with open("Python-Problem-solves-And-Programs/Code With Harry/Hi-score.txt", "w") as f:
            f.write(str(score))
        print("New high score!")

    return score

# Start the game
game()
