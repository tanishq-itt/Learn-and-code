import random


def is_valid_guess(guess: str) -> bool:

    if not guess.isdigit():
        return False

    number = int(guess)
    return 1 <= number <= 100


def get_valid_guess(prompt: str) -> int:
    
    guess = input(prompt)

    while not is_valid_guess(guess):
        guess = input("Invalid input. Please enter a number between 1 and 100: ")

    return int(guess)


def evaluate_guess(guess: int, target: int) -> str:
    
    if guess < target:
        return "low"
    if guess > target:
        return "high"
    return "correct"


def play_game() -> None:
    
    target_number = random.randint(1, 100)
    number_of_guesses = 0

    while True:
        guess = get_valid_guess("Guess a number between 1 and 100: ")
        number_of_guesses += 1

        result = evaluate_guess(guess, target_number)

        if result == "low":
            print("Too low. Guess again.")
        elif result == "high":
            print("Too high. Guess again.")
        else:
            print(f"You guessed it in {number_of_guesses} guesses!")
            break


def main() -> None:
    play_game()


if __name__ == "__main__":
    main()
