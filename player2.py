







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
print(str(playerpos) + "hl")
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
print(str(playerpos) + "hl")
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos + 1
screen[playerpos] = 8
print(screen)
print(str(playerpos) + "hl")
screen[playerpos] = background[playerpos]
try:
    screen[playerpos] = 8
except:
    playerpos = playerpos - 1
print(screen)
print(str(playerpos) + "hl")
try:
    screen[playerpos] = 8
except:
    playerpos = 5
print(screen)
print(str(playerpos) + "hl")
