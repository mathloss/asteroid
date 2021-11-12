import pygame
import math
import random
from pygame import mixer

# Initialize Pygame / Initialisation de Pygame

pygame.init()
clock = pygame.time.Clock()

# The screen / L'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

# Background / Fond d'écran
background = pygame.image.load("back.png")
mixer.music.load('music1.ogg')
mixer.music.play(-1)

# Title and icon / Titre et icone pour la fenetre
pygame.display.set_caption("Asteroid")
icon = pygame.image.load("asteroide24.png")
pygame.display.set_icon(icon)

# Player / Joueur
playerImg = pygame.image.load("darkship.png")
rect_player = playerImg.get_rect()
playerX = 20
playerY = 260
playerX_change = 0
playerY_change = 0

# asteroids
asteroidImg =  []
asteroidX =  []
asteroidY = []
asteroidX_change =  []
asteroidY_change =  []
num_of_asteroids = 13

for i in range(num_of_asteroids):
    asteroidImg.append(pygame.image.load("asteroide64.png"))
    asteroidX.append(random.randint(800, 1000))
    asteroidY.append(random.randint(0, 520))
    asteroidX_change.append(random.randint(-5, -1))
    asteroidY_change.append(random.randint(-2, 2))

# Score 
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10 
textY = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 80 )

####################################################### FONCTIONS ############################################################




def show_score(x, y):
    score_value = font.render("Score : " + str(score), True, "white")
    screen.blit(score_value, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (180, 230))


def player(x, y):
    screen.blit(playerImg, (x, y))

def asteroid(x, y, i):
    screen.blit(asteroidImg[i], (x, y))

# game loop
running = True
while running:

    # color screen / couleur de l'ecran
    screen.fill((0, 0, 0))

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Mouvement du vaisseau
        # touche enfoncée
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
        # touche relâchée
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            

    playerX += playerX_change
    playerY += playerY_change

    #  Empêcher le vaisseau de sortir de l'écran
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    for i in range(num_of_asteroids):
        asteroidX[i] += asteroidX_change[i]
        asteroidY[i] += asteroidY_change[i]
        asteroid(asteroidX[i], asteroidY[i], i)   

        if asteroidY[i] <= 0 :
            asteroidY_change[i] *= -1
            asteroidY[i] += asteroidY_change[i]
        if asteroidY[i] >= 536:
            asteroidY_change[i] *= -1
            asteroidY[i] += asteroidY_change[i]    
    
        if asteroidX[i] <= -64:
            score += 1
            asteroidX[i] = random.randint(800, 1000)
            asteroidY[i] = random.randint(0, 520)
            asteroidX_change[i] = random.randint(-5, -1)
            asteroidY_change[i] = random.randint(-2, 2)
            

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
    clock.tick(60)