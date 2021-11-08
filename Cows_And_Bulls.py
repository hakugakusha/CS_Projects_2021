import random


def compare_cows(number, guess):
    cows = 0
    for value in range(len(number)):
        if number[value] == guess[value]:
            cows += 1
    return cows


def compare_bulls(number, guess):
    bulls = 0
    number_list = []
    guess_list = []
    for value in number:
        number_list.append(value)
    for value in guess:
        guess_list.append(value)

    if guess_list[0] in number_list and guess_list[0] != number_list[0]:
        bulls += 1
    if guess_list[1] in number_list and guess_list[1] != number_list[1]:
        bulls += 1
    if guess_list[2] in number_list and guess_list[2] != number_list[2]:
        bulls += 1
    if guess_list[3] in number_list and guess_list[3] != number_list[3]:
        bulls += 1
    return bulls


game_start = True
guess_count = 0
number = str(random.randint(999, 9999))

while game_start:
    guess = input("Enter your guess: ")
    if guess == "exit":
        game_start = False
    cow_count = compare_cows(number, guess)
    bull_count = compare_bulls(number, guess)
    guess_count += 1

    print("You have " + str(cow_count) + " cows, and " + str(bull_count) + " bulls.")
    if cow_count == 4:
        game_start = False
        print("You win! You guessed " + str(guess_count) + " times.")