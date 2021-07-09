import time
print("Welcome to Rock Paper Scissors!\n")
player1_name = input("Player One, what is your name? ")
player2_name = input("Player Two, what is your name? ")
print("\nNice to meet you " + player1_name + " and " + player2_name + "!\n")


player1_move = input(player1_name + ", Rock Paper or Scissors? ").capitalize()
player2_move = input(player2_name + ", Rock Paper or Scissors? ").capitalize()

game_start = True

while game_start is True:
    print("3!")
    time.sleep(1)
    print("2!")
    time.sleep(1)
    print("1!\n")
    time.sleep(1)
    print(player1_name + " chose " + player1_move + "!")
    time.sleep(1)
    print(player2_name + " chose " + player2_move + "!\n")
    time.sleep(1)

    if player1_move == "Rock" and player2_move == "Scissors":
        print(player1_name + " wins!")
        game_start = False
    elif player1_move == "Rock" and player2_move == "Paper":
        print(player2_name + " wins!")
        game_start = False
    elif player1_move == "Paper" and player2_move == "Rock":
        print(player1_name + " wins!")
        game_start = False
    elif player1_move == "Paper" and player2_move == "Scissors":
        print(player2_name + " wins!")
        game_start = False
    elif player1_move == "Scissors" and player2_move == "Rock":
        print(player2_name + " wins!")
        game_start = False
    elif player1_move == "Scissors" and player2_move == "Paper":
        print(player1_name + " wins!")
        game_start = False
    elif player1_move == player2_move:
        print("Tie!")
        game_start = False
    else:
        print("Invalid Inputs")
        game_start = False

again = input("\nWould you like to play again? ").capitalize()
if again == "Yes":
    print("Welcome to Rock Paper Scissors!\n")
    player1_name = input("Player One, what is your name? ")
    player2_name = input("Player Two, what is your name? ")
    print("\nNice to meet you " + player1_name + " and " + player2_name + "!\n")

    player1_move = input(player1_name + ", Rock Paper or Scissors? ").capitalize()
    player2_move = input(player2_name + ", Rock Paper or Scissors? ").capitalize()

    game_start = True
else:
    print("Thanks for playing!")




