import pygame
import time
import random
import sys

pygame.init()
screen = pygame.display.set_mode((600,600))

players_x = 200
players_y = 200

keys = [False,False,False,False]

rocket = pygame.image.load("rock.png")
bg = pygame.image.load("space.jpg")

while players_y < 600:
    screen.blit(bg,(0,0))
    screen.blit(rocket,(players_x,players_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_UP:    keys[0] = True
                if event.key == pygame.K_LEFT:  keys[1] = True
                if event.key == pygame.K_DOWN:  keys[2] = True
                if event.key == pygame.K_RIGHT: keys[3] = True
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_UP:    keys[0] = False
                if event.key == pygame.K_LEFT:  keys[1] = False
                if event.key == pygame.K_DOWN:  keys[2] = False
                if event.key == pygame.K_RIGHT: keys[3] = False
    if keys[0] and players_y > 0:
        players_y -= 7
    if keys[1] and players_x > 0:
        players_x -= 7
    if keys[2] and players_y < 500:
        players_y += 7
    if keys[3] and players_x > 500:
        players_x += 7

    players_y +=  5
    #sleep(0.05)

print("Game Over")
pygame.quit()    



                
                
                




