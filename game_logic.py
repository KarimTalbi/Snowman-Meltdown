import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    if mistakes < len(STAGES) - 1:
        print(STAGES[mistakes])
    # Build a display version of the secret word.
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Word: ", display_word)
        print("\n")

    else:
        print(STAGES[mistakes])


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:
        if len(guessed_letters) == len(secret_word):
            print(f"You saved the snowman by guessing the word {secret_word}")
            break

        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower().strip()
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)

        else:
            mistakes += 1

        if mistakes >= len(STAGES) - 1:
            print("The snowman melted before you guessed the word")
            print(f"The word was {secret_word}")
            display_game_state(mistakes, secret_word, guessed_letters)
            break