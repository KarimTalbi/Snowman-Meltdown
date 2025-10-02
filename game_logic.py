import random
import sys

from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown"]


class NotSingleCharError(Exception):
    pass

class NoInputError(Exception):
    pass

class AlreadyGuessedError(Exception):
    pass

class NotAlphaError(Exception):
    pass

class BinaryQuestionError(Exception):
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


def get_input(secret_word, guessed_letters, wrong_letters):
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

            return guess

        except Exception as e:
            print(e)


def play_game():
    print("Welcome to Snowman Meltdown!")

    while True:
        secret_word = get_random_word()
        guessed_letters = []
        wrong_letters = []
        mistakes = 0

        while True:
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = get_input(secret_word, guessed_letters, wrong_letters)

            print("You guessed:", guess)

            if guess in secret_word:
                guessed_letters.append(guess)

            else:
                mistakes += 1
                wrong_letters.append(guess)

            if len(guessed_letters) == len(secret_word):
                print(f"\nYou saved the snowman by guessing the word {secret_word}")
                break

            elif mistakes >= len(STAGES) - 1:
                print("\nThe snowman melted before you guessed the word")
                print(f"The word was {secret_word}")
                display_game_state(mistakes, secret_word, guessed_letters)
                break

        while True:
            try:
                keep_playing = input("\nWould you like to keep playing (y/n)? ").lower().strip()

                if not keep_playing:
                    raise NoInputError("can't be empty")

                if keep_playing not in {"y", "n"}:
                    raise BinaryQuestionError("Please enter 'y' or 'n'")

            except Exception as e:
                print(e)

            else:
                if keep_playing == 'y':
                    break

                else:
                    sys.exit("\nThank you for playing!")