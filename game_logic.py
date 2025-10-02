"""game logic functions"""

import random
import sys

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


class NotSingleCharError(Exception):
    """used to display Errormessage if char is more than 1 char"""
    pass


class NoInputError(Exception):
    """used to display Errormessage if there was no input """
    pass


class AlreadyGuessedError(Exception):
    """used to display Errormessage if a letter has already been guessed"""
    pass


class NotAlphaError(Exception):
    """used if guess is not in the alphabet"""
    pass


class BinaryQuestionError(Exception):
    """used if input is not a valid option (e.g. (y/n))"""
    pass


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list[str]) -> None:
    """displays the snowman at current stage and the word to guess"""
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


def get_input(guessed_letters: list[str], wrong_letters: list[str]) -> str:
    """gets input from a user and validates it"""
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


def play_game() -> None:
    """entry point of game"""
    print("Welcome to Snowman Meltdown!")

    while True:
        secret_word = get_random_word()
        guessed_letters = []
        wrong_letters = []
        mistakes = 0

        while True:
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = get_input(guessed_letters, wrong_letters)

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
