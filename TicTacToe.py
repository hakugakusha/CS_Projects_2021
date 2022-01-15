import random

print("Welcome to Tic-Tac-Toe! Your marking will be represented by the 'O'.")
print("The board will be visually represented by such:")
print('''    
    0 | 1 | 2
  ----+---+----
    3 | 4 | 5
  ----+---+----
    6 | 7 | 8
''')

print(
    "Each cell has a designated number. To place a marking in a certain cell, please type the number that corresponds with that cell's position. Good luck!")

Board_Spots = {
    "0": " ",
    "1": " ",
    "2": " ",
    "3": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "7": " ",
    "8": " ",
}


def printBoard(board):
    print(board['0'] + "  |" + board['1'] + "  |" + board['2'])
    print("---+---+---")
    print(board['3'] + "  |" + board['4'] + "  |" + board['5'])
    print('---+---+---')
    print(board['6'] + "  |" + board['7'] + "  |" + board['8'])


game_start = True
move_count = 0
while game_start:
    marking = "O"

    printBoard(Board_Spots)
    move = input("Where do you want to place your marking? ")

    if Board_Spots[move] == " ":
        Board_Spots[move] = marking
        move_count += 1

    else:
        print("This spot on the board has already been filled.")
        continue

    # AI
    AI_turn = True
    while AI_turn:

        AI_marking = "X"
        AI_move = random.randint(0, 8)

        if Board_Spots[str(AI_move)] == " ":
            Board_Spots[str(AI_move)] = AI_marking
            move_count += 1
            AI_turn = False
        else:
            continue

    # Winner Check
    if move_count == 10:
        print("Tie!")
        game_start = False

    if move_count >= 5:

        if Board_Spots['0'] == Board_Spots['1'] == Board_Spots['2'] != " ":
            if Board_Spots['0'] == Board_Spots['1'] == Board_Spots['2'] == "O":
                game_start = False
                print("Game over! " + marking + " wins!")

            elif Board_Spots['0'] == Board_Spots['1'] == Board_Spots['2'] == "X":
                game_start = False
                print("Game over! X wins!")

        elif Board_Spots['3'] == Board_Spots['4'] == Board_Spots['5'] != " ":
            if Board_Spots['3'] == Board_Spots['4'] == Board_Spots['5'] == "O":
                game_start = False
                print("Game over! " + marking + " wins!")

            elif Board_Spots['3'] == Board_Spots['4'] == Board_Spots['5'] == "X":
                game_start = False
                print("Game Over! " + marking + " wins!")

        elif Board_Spots['6'] == Board_Spots['7'] == Board_Spots['8'] != " ":
            if Board_Spots['6'] == Board_Spots['7'] == Board_Spots['8'] == "O":
                game_start = False
                print("Game over! " + marking + " wins!")

            elif Board_Spots['6'] == Board_Spots['7'] == Board_Spots['8'] == "X":
                game_start = False
                print("Game over! X wins!")

        elif Board_Spots['0'] == Board_Spots['3'] == Board_Spots['6'] != " ":
            if Board_Spots['0'] == Board_Spots['3'] == Board_Spots['6'] == "O":
                game_start = False
                print("Game over! " + marking + " wins!")

            elif Board_Spots['0'] == Board_Spots['3'] == Board_Spots['6'] == "X":
                game_start = False
                print("Game over! X wins!")

        elif Board_Spots['1'] == Board_Spots['4'] == Board_Spots['7'] != " ":
            if Board_Spots['1'] == Board_Spots['4'] == Board_Spots['7'] == "O":
                game_start = False
                print("Game over! " + marking + " wins!")

            elif Board_Spots['1'] == Board_Spots['4'] == Board_Spots['7'] == "X":
                game_start = False
                print("Game over! X wins!")

        elif Board_Spots['2'] == Board_Spots['5'] == Board_Spots['8'] != " ":
            if Board_Spots['2'] == Board_Spots['5'] == Board_Spots['8'] == "O":
                game_start = False
                print("Game over! " + marking + " wins!")

            elif Board_Spots['2'] == Board_Spots['5'] == Board_Spots['8'] == "X":
                game_start = False
                print("Game over! X wins!")

        elif Board_Spots['0'] == Board_Spots['4'] == Board_Spots['8'] != " ":
            if Board_Spots['0'] == Board_Spots['4'] == Board_Spots['8'] == "O":
                game_start = False
                print("Game over! " + marking + " wins!")

            elif Board_Spots['0'] == Board_Spots['4'] == Board_Spots['8'] == "X":
                game_start = False
                print("Game over! X wins!")

        elif Board_Spots['2'] == Board_Spots['4'] == Board_Spots['6'] != " ":
            if Board_Spots['2'] == Board_Spots['4'] == Board_Spots['6'] == "O":
                game_start = False
                print("Game over! " + marking + " wins!")

            elif Board_Spots['2'] == Board_Spots['4'] == Board_Spots['6'] == "X":
                game_start = False
                print("Game over! X wins!")


printBoard(Board_Spots)
print(move_count)
