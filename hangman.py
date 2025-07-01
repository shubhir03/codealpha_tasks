import random

# Step 1: Predefined list of words
words = ["apple", "banana", "grape", "orange", "mango"]

# Step 2: Choose a random word
word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

# Step 3: Display word with underscores
def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])

# Step 4: Game Loop
print("🎮 Welcome to Hangman!")
while attempts_left > 0:
    print("\nWord:", display_word())
    print("Attempts left:", attempts_left)
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("❗ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
        if all(letter in guessed_letters for letter in word_to_guess):
            print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
            break
    else:
        print("❌ Wrong guess.")
        attempts_left -= 1

if attempts_left == 0:
    print("\n💀 Game over! The word was:", word_to_guess)
