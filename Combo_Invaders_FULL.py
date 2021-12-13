import pygame

from pygame import mixer

import random
import math

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("lachsa.png")

# Background Music
mixer.music.load('Pokemon_Song.wav')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("First Game")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player Image
playerImg = pygame.image.load("drummer.PNG")
playerX = 370
playerY = 480
playerX_change = 0

# Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

enemy_count = 10

for i in range(enemy_count):
    enemyImg.append(pygame.image.load("kai3.png"))
    enemyX.append(random.randint(7, 729))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.15)
    enemyY_change.append(40)

# Bullet Image
bulletImg = pygame.image.load("drumsticks.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "Ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over Text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over():
    over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fireBullet(x, y):
    global bullet_state
    bullet_state = "Fired"
    screen.blit(bulletImg, (x + 16, y + 10))


def checkCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state == "Ready":
                    bullet_shoot = mixer.Sound('shooting.wav')
                    bullet_shoot.play()
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 6:
        playerX = 6
    elif playerX >= 730:
        playerX = 730

    # Enemy Movement
    for i in range(enemy_count):

        # Game Over
        if enemyY[i] > 416:
            for j in range(enemy_count):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 6:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 730:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = checkCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision is True:
            explosion_Sound = mixer.Sound('explosion_kill.wav')
            explosion_Sound.set_volume(0.25)
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "Ready"
            score_value += 100
            enemyX[i] = random.randint(7, 729)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "Ready"
    if bullet_state == "Fired":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()
