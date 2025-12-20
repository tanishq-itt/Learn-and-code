import random

def isValid(guessedNumber):
    if guessedNumber.isdigit() and 1 <= int(guessedNumber) <= 100:
        return True
    else:
        print("I wont count this one Please enter a number between 1 to 100")
        return False


def userInput(prompt="Guess a number between 1 and 100: "):
    return input(prompt)


def processUserGuess(guessedNumber, originalNumber):
    if guessedNumber < originalNumber:
        print("Too low. Guess again")
        return "low"
    elif guessedNumber > originalNumber:
        print("Too High. Guess again")
        return "high"
    else:
        print("You guessed it correct")
        return "correct"


def getValidGuess():
    guessedNumber = userInput()
    while not isValid(guessedNumber):
        guessedNumber = userInput()
    return int(guessedNumber)


def playGuessingRound(originalNumber):
    numberOfGuesses = 0
    while True:
        guess = getValidGuess()
        numberOfGuesses += 1
        result = processUserGuess(guess, originalNumber)
        if result == "correct":
            return numberOfGuesses


def main():
    originalNumber = random.randint(1, 100)
    totalGuesses = playGuessingRound(originalNumber)
    print("You guessed it in", totalGuesses, "guesses!")


main()
