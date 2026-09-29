# ==========================================
# INTERMEDIATE TASK 2 - HANGMAN
# ==========================================

import random


# Words for the game
words = [
    "python",
    "machine",
    "developer",
    "computer",
    "programming"
]


# Hints for each word
hints = {
    "python": "A popular programming language",
    "machine": "A device that performs a task",
    "developer": "A person who creates software",
    "computer": "An electronic device used for computing",
    "programming": "Writing instructions for a computer"
}


# Select a random word
word = random.choice(words)

hint = hints[word]

guessed_letters = set()

wrong_guesses = 0

max_wrong_guesses = 6


# Visual progress
stages = [
    "[------]",
    "[O-----]",
    "[O|----]",
    "[O|/---]",
    "[O|/\\--]",
    "[O|/\\|-]",
    "[O|/\\|]"
]


print("==============================")
print("       HANGMAN GAME")
print("==============================")

print("\nHint:", hint)


# Main game
while wrong_guesses < max_wrong_guesses:

    display = ""

    for letter in word:

        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    print(
        "Wrong guesses:",
        wrong_guesses,
        "/",
        max_wrong_guesses
    )

    print(stages[wrong_guesses])


    # Check win
    if all(
        letter in guessed_letters
        for letter in word
    ):

        print("\nCongratulations!")
        print("You guessed the word:", word)

        break


    # Get guess
    guess = input(
        "Enter a letter: "
    ).lower().strip()


    # Validate input
    if len(guess) != 1 or not guess.isalpha():

        print(
            "Please enter one alphabet letter."
        )

        continue


    # Duplicate guess
    if guess in guessed_letters:

        print(
            "You already guessed that letter."
        )

        continue


    guessed_letters.add(guess)


    # Correct / wrong
    if guess in word:

        print("Correct guess!")

    else:

        wrong_guesses += 1

        print("Wrong guess!")


# Game over
else:

    print(stages[max_wrong_guesses])

    print("\nGame Over!")

    print("The word was:", word)