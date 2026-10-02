# Task 4: Hangman_closure.py

def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter)
        
        word_display = ""
        
        for character in secret_word:
            if character in guesses:
                word_display += character
            else:
                word_display += "_"
                
        print(word_display)
        
        return all(character in guesses for character in secret_word)
    
    return hangman_closure

# Mainline
secret_word = input("Enter the secret word: ")

hangman = make_hangman(secret_word)

while True:
    guess = input("Guess a letter: ")
    
    if hangman(guess):
        print("You guessed the word!")
        break