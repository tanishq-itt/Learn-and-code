def isValidGuess(value):
    if value.isdigit() and 1 <= int(value) <= 100:
        return True
    else:
        return False

def main():
    targetNumber = random.randint(1, 100)
    guessedCorrectly = False
    userGuess = input("Guess a number between 1 and 100:")
    guessCount = 0
    while not guessedCorrectly:
        if not isValidGuess(userGuess):
            userGuess = input("I won't count this one. Please enter a number between 1 to 100:")
            continue
        else:
            guessCount += 1
            userGuess = int(userGuess)

        if userGuess < targetNumber:
            userGuess = input("Too low. Guess again")
        elif userGuess > targetNumber:
            userGuess = input("Too high. Guess again")
        else:
            print("You guessed it in", guessCount, "guesses!")
            guessedCorrectly = True

main()
