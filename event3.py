import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE=(640,480)
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)


try:
    font = pygame.font.SynFont("arial",16);
except:
    font = pygame.font.Font(pygame.font.get_default_font(),16)
font_height = font.get_linesize()
event_text=[]

while True:
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            """
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text=event_text[-SCREEN_SIZE[1]/font_height:]

    if event.type == QUIT:
        exit()
    screen.fill((255,255,255))

    y = SCREEN_SIZE[1]-font_height
    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,0,0)),(0,y))
        y-=font_height
        #print(event_text)

        pygame.display.update()
