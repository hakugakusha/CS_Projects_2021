secret_word = "Burrito"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit: # do they still have some guesses left? if they do, go again
        guess = input("Guess the secret word: ")
        guess_count = guess_count + 1 # adds how many times the player has guessed
        print("You have guessed " + str(guess_count) + " times.") # the input will be stored in the guess variable, if it's not equal, it loops and asks again.
    else:
        out_of_guesses = True # if out of guesses, this becomes true.

if out_of_guesses: # if true, you lose.
    print("\nYou are out of guesses. You lose! The secret word was " + secret_word + ".")

else:
    print("\nCongrats! You won in " + str(guess_count) + " guesses.")










