# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []
    # defining inner function
    def hangman_closure(letter):
        # record guess
        guesses.append(letter.lower())

        # build masked word string
        displayed_word = ""
        for char in secret_word:
            if char.lower() in guesses:
                displayed_word += char
            else:
                displayed_word += "_"

        # Return True if won, False otherwise
        if "_" not in displayed_word:
            return True
        return displayed_word

    return hangman_closure

# Game Mainline
secret = input("Enter the secret word to start the game: ").strip()

# Creating closure instance
play_game = make_hangman(secret)

is_game_over = False
while not is_game_over:
    guess = input("Guess a letter: ")
    
    if len(guess) == 1 and guess.isalpha():
        is_game_over = play_game(guess)
    else:
        print("Please enter a single valid letter. ")
        
print("Congratulations! You guessed the word!")
    