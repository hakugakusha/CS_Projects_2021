import random

secret_number = random.randint(1, 9)
guess = input("Guess the random number from 1-9: ")
game_start = True
round_amount = 1
count = 0
wins = 0
total_count = 0

while game_start:
    if guess == "exit":
        print("\nThanks for playing!")
        print("You have guessed a total of: " + str(total_count) + " times and you won " + str(wins) + " times!")
        break

    guess = int(guess)
    if guess < secret_number:
        print("You guessed too low.\n")
        count = count + 1
        total_count = total_count + 1
        print("You have guessed " + str(count) + " times.\n")
        guess = int(input("Guess the random number from 1-9: "))

    elif guess > secret_number:
        print("You guessed too high.\n")
        count = count + 1
        total_count = total_count + 1
        print("You have guessed " + str(count) + " times.\n")
        guess = int(input("Guess the random number from 1-9: "))

    else:
        print("You guessed correctly! Good job.")
        count = count + 1
        total_count = total_count + 1
        print("You have guessed " + str(count) + " times.\n")
        secret_number = random.randint(1, 9)
        round_amount = round_amount + 1
        wins = wins + 1
        print("Round " + str(round_amount))
        print("You have won " + str(wins) + " times!\n")
        guess = (input("Guess the random number from 1-9: "))
        count = 0
