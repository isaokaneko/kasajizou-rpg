#<F11><F11:wq
import pygame 
from pygame.locals import *
from sys import exit
import random
import datetime
import time
filename="ojizousan2.png"
background_image_filename = 'j.png'
def main():
            

    pygame.init()
    screen = pygame.display.set_mode((640,480),0,32)
    background = pygame.image.load(background_image_filename).convert()
    jizou = pygame.image.load(filename).convert_alpha()

    x,y = 0, 100
    move_x,move_y = 0, 0
    r  = random.random()*10
   
    while True:
        for event in pygame.event.get():
            #pygame.event.set_blocked([KEYDOWN,KEYUP])
            if event.type == QUIT:
                exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -0.1
            elif event.key == K_RIGHT:
                move_x = +0.1
            elif event.key == K_UP:
                move_y = -0.1
            elif event.key == K_DOWN:
                move_y = +0.1
            elif event.key == K_ESCAPE:
                exit()
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0
   
        x+=move_x
        y+=move_y
        if r == move_x:
            sentou()
    
            
       #screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(jizou,(x,y))
   
        pygame.display.update()

def sentou():
    pygame.init()
    screen = pygame.display.set_mode((640,480),0,32)
    background = pygame.image.load(background_image_filename).convert()
    jizou = pygame.image.load(filename).convert_alpha()
    mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

    x,y = 0, 0
    move_x,move_y = 0, 0
   
    while True:
        for event in pygame.event.get():
            #pygame.event.set_blocked([KEYDOWN,KEYUP])
            if event.type == QUIT:
                exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -0.1
            elif event.key == K_RIGHT:
                move_x = +0.1
            elif event.key == K_UP:
                move_y = -0.1
            elif event.key == K_DOWN:
                move_y = +0.1
            elif event.key == K_ESCAPE:
                exit()
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0
   
        x+=move_x
        y+=move_y
   
       #screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(jizou,(x,y))
   
        pygame.display.update()


main()
