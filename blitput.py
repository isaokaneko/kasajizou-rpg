#<F11><F11:wq
import pygame 
from pygame.locals import *
from sys import exit
import random
import datetime
import time
filename = []
flag = 0
filename="ojizousan2.png"
filename2="tesita2.png"
filename3="kougeki.png"
filename4="bougyo.png"
filename5="nigeru.png"
filename6="kougeki2.png"
filename7="bougyo2.png"
filename8="nigeru2.png"
filename9="waku2.png"
filename10="back.png"
background_image_filename = 'j.png'
class jizou:
    def __init__(self):
        self.hp =20
        self.mp =10
        self.tuyosa =3
        self.keikenchi=0
        
    def hit(self,enemy,list1,screen):
        f =  int((3 * random.random()))
        enemy.hp -=  (self.tuyosa + f )
        list1.append("jizou no kougeki")
        font_height = font.get_linesize()
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-font_height))
            font_height -= font_height
    def levelup(self):
        if self.keikenchi >= 30:
            self.hp = self.hp + int((3 * random.random())) + 1

class tesita1:
    def __init__(self):
        self.hp =20
        self.mp =4
        self.tuyosa =3
        self.keikenchiout=10
    def hit(self,enemy):
        f =  int((3 * random.random()))
        enemy.hp -=  (self.tuyosa + f )

jj= jizou() 
teki = tesita1()
pygame.init()
background_image_filename = "sentou.png"
screen = pygame.display.set_mode((640,480),0,32)
background = pygame.image.load(background_image_filename).convert()
jizou = pygame.image.load(filename).convert_alpha()
tesita = pygame.image.load(filename2).convert_alpha()
kou = pygame.image.load(filename3).convert_alpha()

bou = pygame.image.load(filename4).convert_alpha()
nige = pygame.image.load(filename5).convert_alpha()
k2 = pygame.image.load(filename6).convert_alpha()

b2 = pygame.image.load(filename7).convert_alpha()
n2 = pygame.image.load(filename8).convert_alpha()
waku = pygame.image.load(filename9).convert_alpha()
back = pygame.image.load(filename9).convert_alpha()
x,y = 100, 200
tesita_x,tesita_y = 400, 200
move_x,move_y = 0, 0
c = 1
x2 =1
y2 =1
e =0
playerpos=0
event_text = []
list1 = []
yyy = 0
while True:

    flag1=0
    screen.blit(background,(0,0))
    screen.blit(jizou,(100,200))
    screen.blit(tesita,(tesita_x,tesita_y))
    font = pygame.font.Font(None,32)
    pygame.draw.rect(screen,(0,0,0),(20,20,150,150))
    pygame.draw.rect(screen,(0,0,0),(200,200,150,150))
    pygame.draw.rect(screen,(0,0,0),(20,300,150,150))
    text = font.render(str(jj.hp),False,(255,255,255))
    screen.blit(text,(30,120))
    text = font.render(str(jj.mp),False,(255,255,255))
    screen.blit(text,(60,120))
    text = font.render("HP",False,(255,255,255))
    screen.blit(text,(20,100))
    text = font.render("MP",False,(255,255,255))
    screen.blit(text,(60,100))
    screen.blit(kou,(60,300))
    screen.blit(bou,(60,350))
    screen.blit(nige,(60,400))
    background2 = [kou,bou,nige]
    pt = 300
    pd = 400
    bg=0

    #for i in range(3):
        #screen.blit(background2[i],(i*40,300,350,150))
    #playerpos = 2
    #pygame.draw.rect(screen,(0,0,0),(20,300,150,150),2)
        #pygame.event.set_blocked([KEYDOWN,KEYUP])
    pygame.event.pump()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_ESCAPE]:
        exit()
    if pressed_keys[pygame.K_UP] :
        playerpos -=1
    if pressed_keys[pygame.K_DOWN] : 
        playerpos +=1
                
    #screen.blit(background2[playerpos],(20,i*10))
    #screen[playerpos]=background2[playerpos]
    #playerpos = 2
    #screen.blit(waku,(20,playerpos*40))
    #screen.blit(background2[playerpos],(20,playerpos*40))
    #playerpos = playerpos - 1
    if playerpos == 0:
        pygame.time.wait(100)
        screen.blit(waku,(60,300 ))
        pressed = pygame.key.get_pressed()
        if pressed[K_RETURN]:
            jj.hit(teki,list1,screen)
            flag1 = 1
            """
            tt = font.render("jizou no kougeki",False,(255,255,255))
            screen.blit(tt,(200,200))
            """
    elif playerpos == 1:
        pygame.time.wait(100)
        screen.blit(waku,(60,350 ))
    elif playerpos == 2:
        pygame.time.wait(100)
        screen.blit(waku,(60,400  ))

    if teki.hp <= 0:
        exit()
    flag1=1
    
    """
    screen.blit(k2,(60,300))
    screen.blit(b2,(60,350))
    screen.blit(n2,(60,400))
    text = font.render("kougeki",False,(255,255,255))
    screen.blit(text,(60,300))
    text = font.render("bougyo",False,(255,255,255))
    screen.blit(text,(60,320))
    """
    def kougeki():
        r2 = int(r)
        if r2 >= 7:
            damege = tuyosa + 1
        elif r2 >= 3:
            damege = tuyosa + 3
        elif r2 >= 0:
            damege = tuyosa + 5
    pygame.display.update()

""" 
    for x in reversed(list1):
        y-=font_height
"""





def up():
    pygame.draw.rect(screen,(255,255,255),(60,300,100,20),5)
def down():
    pygame.draw.rect(screen,(255,255,255),(60,300,100,20),5)
def bougyo():
    screen = pygame.display.set_mode((640,480),0,32)
    font = pygame.font.Font(None,32)
    text = font.render("bougyo",False,(255,255,255))
    screen.blit(text,(120,280))
    pygame.display.update()
#sentou()
