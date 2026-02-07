import random


words = ["python", "apple", "banana", "coding", "laptop"]


secret_word = random.choice(words)


guessed_letters = []
attempts_left = 6

print("🎯 Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")


while attempts_left > 0:
    display_word = ""

    
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())

  
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break

   
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

 
    if guess in secret_word:
        print("✅ Good guess!\n")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}\n")

if attempts_left == 0:
    print("💀 Game Over!")
    print("The correct word was:", secret_word)
