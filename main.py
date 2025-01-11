import math
import pygame
import random

SCREENWIDTH = 800
SCREENHEIGHT = 500
PLAYERSTART_X = 370
PLAYERSTART_Y = 380
ENEMYSTART_Y_MIN = 50
ENEMYSTART_Y_MAX = 150
ENEMYSPEED_X = 4
ENEMYSPEED_Y = 40
BULLETSPEED_Y = 10
COLLISON_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode(SCREENHEIGHT,SCREENWIDTH)
bakcground = pygame.image.load("background.png")
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = PLAYERSTART_X
playerY = PLAYERSTART_Y
playerX_change = 0

enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREENWIDTH - 64))
    enemyY.append(random.randint(ENEMYSTART_Y_MIN, ENEMYSTART_Y_MAX))
    enemyX_change.append(ENEMYSPEED_X)
    enemyY_change.append(ENEMYSPEED_Y)

    