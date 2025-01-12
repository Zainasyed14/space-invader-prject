import math
import pygame
import random

SCREENWIDTH = 800
SCREENHEIGHT = 800
PLAYERSTART_X = 370
PLAYERSTART_Y = 380
ENEMYSTART_Y_MIN = 50
ENEMYSTART_Y_MAX = 150
ENEMYSPEED_X = 4
ENEMYSPEED_Y = 40
BULLETSPEED_Y = 10
COLLISON_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREENHEIGHT,SCREENWIDTH))
background = pygame.image.load("background.png")
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
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREENWIDTH - 64))
    enemyY.append(random.randint(ENEMYSTART_Y_MIN, ENEMYSTART_Y_MAX))
    enemyX_change.append(ENEMYSPEED_X)
    enemyY_change.append(ENEMYSPEED_Y)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYERSTART_Y
bulletX_change = 0
bulletY_change = BULLETSPEED_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf' , 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf' , 64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER" , True , (255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(playerImg,(x , y))

def enemy(x,y,i):
    screen.blit(enemyIMG[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16 , y+10))

def IsCollision(enemyX,enemyY,bulletX,bulletY):
    distance =  math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    return distance < COLLISON_DISTANCE
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              playerX_change = -5
          if event.key == pygame.K_RIGHT:
              playerX_change = 5
          if event.key == pygame.K_SPACE and bullet_state == "ready":
              bulletX = playerX
              fire_bullet(bulletX, bulletY)
      if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
          playerX_change = 0

    playerX += playerX_change
    playerX = max(0,min(playerX , SCREENWIDTH - 64))

    for i in range(num_of_enemies):
        if enemyY[i]>340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i]<= 0 or enemyX[i] >= SCREENWIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if IsCollision(enemyX[i] , enemyY[i] , bulletX, bulletY):
            bulletY = PLAYERSTART_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREENWIDTH - 64)
            enemyY[i] = random.randint(ENEMYSTART_Y_MIN, ENEMYSTART_Y_MAX) 

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = PLAYERSTART_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX , bulletY)
        bulletY -= bulletY_change
        # bulletY = bulletY-bulletY_change

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
