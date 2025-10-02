import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

class NotSingleCharError(Exception):
    pass

class NoInputError(Exception):
    pass

class AlreadyGuessedError(Exception):
    pass

class NotAlphaError(Exception):
    pass


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
    wrong_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:
        if len(guessed_letters) == len(secret_word):
            print(f"You saved the snowman by guessing the word {secret_word}")
            break

        display_game_state(mistakes, secret_word, guessed_letters)

        while True:
            try:
                guess = input("Guess a letter: ").lower().strip()
                if not guess:
                    raise NoInputError("guess can't be empty")

                if not guess.isalpha():
                    raise NotAlphaError("guess must be letter of the alphabet")

                if len(guess) != 1:
                    raise NotSingleCharError("guess can only be 1 letter")

                if guess in guessed_letters or guess in wrong_letters:
                    raise AlreadyGuessedError(f"You have already guessed '{guess}'")

                break

            except Exception as e:
                print(e)

        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)

        else:
            mistakes += 1
            wrong_letters.append(guess)

        if mistakes >= len(STAGES) - 1:
            print("The snowman melted before you guessed the word")
            print(f"The word was {secret_word}")
            display_game_state(mistakes, secret_word, guessed_letters)
            break