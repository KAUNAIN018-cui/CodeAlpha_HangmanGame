import random

def hangman():
    words = ['apple', 'banana', 'python', 'code', 'alpha']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    
    while tries > 0 and '_' in guessed:
        print(f"Word: {' '.join(guessed)}")
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("Incorrect guess.")
            tries -= 1

    if '_' not in guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"You lost! The word was: {word}")

hangman()
