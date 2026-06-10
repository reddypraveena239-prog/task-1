import random

# Predefined words
words = ["apple", "mango", "grapes", "banana", "orange"]

# Choose random word
chosen_word = random.choice(words)

# Create empty display
display = ["_"] * len(chosen_word)

# Wrong guesses limit
attempts = 6

guessed_letters = []

print("🎮 Welcome to Hangman Game!")

while attempts > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check already guessed
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

        print("Correct Guess!")

    else:
        attempts -= 1
        print("Wrong Guess!")
# Final result
if "_" not in display:
    print("\n🎉 Congratulations! You Won!")
    print("The word was:", chosen_word)

else:
    print("\n💀 Game Over!")
    print("The word was:", chosen_word)

