import pygame
import random
import sys

from pygame.locals import *

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
grey = (128, 128, 128)
black = (0, 0, 0)
red = (110, 38, 14)

# Fonts
normalFont = pygame.font.Font("freesansbold.ttf", 32)
bigFont = pygame.font.Font("freesansbold.ttf", 64)
youWin = bigFont.render("You win!", True, green)
youLose = bigFont.render("You lose!", True, red)


def checkGuess(turns, word, guess, window):
    letter_list = ["", "", "", "", ""]
    spacing = 0
    guessColor = [grey, grey, grey, grey, grey]

    for x in range(0, 5):
        if guess[x] in word:
            guessColor[x] = yellow

        if guess[x] == word[x]:
            guessColor[x] = green

    list(guess)

    for x in range(0, 5):
        letter_list[x] = normalFont.render(guess[x], True, black)
        pygame.draw.rect(window, guessColor[x], pygame.Rect(60 + spacing, 50 + (turns * 80), 50, 50))
        window.blit(letter_list[x], (70 + spacing, 50 + (turns * 80)))
        spacing += 80

    if guessColor == [green, green, green, green, green]:
        return True


def main():
    file = open("wordle_words.txt", "r")
    wordle_words = file.readlines()
    word = wordle_words[random.randint(0, len(wordle_words) - 1)].upper()

    height = 700
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ""
    guess2 = ""

    print(word)

    for x in range(0, 5):
        for y in range(0, 6):
            pygame.draw.rect(window, grey, pygame.Rect(60 + (x * 80), 50 + (y * 80), 50, 50), 2)

    pygame.display.set_caption("Wordle for Alison")

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess += event.unicode.upper()

                if event.key == K_SPACE:
                    guess = guess[:-1]

                if event.key == K_RETURN and win is True:
                    main()

                if event.key == K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE or len(guess) > 5:
                    guess = guess[:-1]

                if event.key == pygame.K_RETURN and len(guess) > 4:
                    win = checkGuess(turns, word, guess, window)
                    turns += 1
                    guess = ""
                    window.fill(black, (0, 500, 500, 200))

        window.fill(black, (0, 500, 500, 200))
        render_guess = normalFont.render(guess, True, grey)
        window.blit(render_guess, (200, 530))

        if win is True:
            window.blit(youWin, (100, 600))

        if turns == 6 and win is not True:
            window.blit(youLose, (100, 600))
            window.blit(normalFont.render(word[:-1], True, green), (190, 550))

        pygame.display.update()
        clock.tick(FPS)


main()
