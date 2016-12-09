







import pygame
screen = [1,1,2,2,2,1,]
print(screen)
screen[3] = 8
print(screen)
playerpos = 3
screen[playerpos] = 8
print(screen)
playerpos = playerpos - 1
screen[playerpos] = 8
print(screen)

background = [1, 1, 2, 2, 2, 1]
screen = [0]*6
for i in range(6):
   screen[i] = background[i]
print(screen)
playerpos = 3
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
print(playerpos)
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
print(playerpos)
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
print(playerpos)
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
print(playerpos)
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
print(playerpos)
"""
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                  exit()
            elif event.key == K_UP:
               playerpos = playerpos -1
               print("play")
               print(playerpos)
            elif event.key == K_DOWN:
                playerpos = playerpos+ 1
                print("play2")
                print(playerpos)
                
"""
