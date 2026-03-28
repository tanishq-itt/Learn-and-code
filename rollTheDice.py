import random
def rollDice(numberOfSides):
    numberOutcome=random.randint(1, numberOfSides)
    return numberOutcome


def main():
    numberOfSides=6
    running=True
    while running:
        userInput=input("Ready to roll? Enter Q to Quit")
        if userInput.lower() !="q":
            rollValue=rollDice(numberOfSides)
            print("You have rolled a",rollValue)
        else:
            running=False


