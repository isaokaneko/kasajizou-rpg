import pygame 
from pygame.locals import * 
from sys import exit
import random
import datetime
import time
import pickle
filename="ojizousan2.png"
filename2="tesita2.png"
background_image_filename = 'j.png'
basho = []
list1 = []
y = 0
x = 0
xy = []
class jizouclass:
    def __init__(self):
        self.hp =20
        self.mp =10
        self.tuyosa =8
        self.keikenchi=0
        self.list1 = []

    def hit(self,screen,background1,enemy,y):
        f =  int((5 * random.random()))
        enemy.hp -=  (self.tuyosa + f )
        screen.blit(background1,(0,0))
        list1.append("jizou no kougeki")
        a = f + self.tuyosa
        list1.append(str(a) + " no damage")
        list1.append("")
        font = pygame.font.Font(None,32)
        font_height = font.get_linesize()
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
            print(text+("AAAAAAA"))
            print(list1)

            print(text+"BBBBBBB")
            print(list1)
            """
        if enemy.hp <= 0:
            field(basho)
            """
    def taosita(self,screen,background1,enemy,y):
        font = pygame.font.Font(None,32)
        font_height = font.get_linesize()
        screen.blit(background1,(0,0))
        list1.append("tesita wo taosita!")
        list1.append("")
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
        return list1

    def bougyo(self,screen,background1,y):
        font = pygame.font.Font(None,32)
        font_height = font.get_linesize()
        screen.blit(background1,(0,0))
        print(list1)
        print("CCC")
        list1.append("jizou no bougyo")
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
        return list1
    def nigeru(self,screen,background1,y,teki):
        font = pygame.font.Font(None,32)
        font_height = font.get_linesize()
        screen.blit(background1,(0,0))
        print(list1)
        print("CCC")
        list1.append("tesita wo taosita")
        self.keikenchi = self.keikenchi + teki.keikenchiout
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
        time.sleep(3)
        return list1

        t = 1
        
        #field(basho)
    def del1(self,list1):
        del list1[:]
        print list1
    def levelup(self,screen,background1,enemy,y):
        if self.keikenchi >= 30:
            self.hp = self.hp + int((3 * random.random())) + 10
            f =  int((3 * random.random()))
            screen.blit(background1,(0,0))
            list1.append("jizou no levelup")
            font = pygame.font.Font(None,32)
            font_height = font.get_linesize()
            for text in reversed(list1):
                screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
                y += font_height

"""
    def nigeru(self,screen,background1,y):
        font = pygame.font.Font(None,32)
        font_height = font.get_linesize()
        screen.blit(background1,(0,0))
        print(list1)
        print("CCC")
        list1.append("nigeta obbbbbbbbb")
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
"""
class tesita1:
    def __init__(self):
        self.hp =20
        self.mp =4
        self.tuyosa =3
        self.keikenchiout=10
    def hit(self,screen,background1,enemy,y):
        f =  int((1 * random.random()))
        enemy.hp -=  (self.tuyosa + f )
        screen.blit(background1,(0,0))
        #time.sleep(1)
        list1.append("tesita no kougeki")
        a = f + self.tuyosa

        list1.append(str(a) + " no damage")
        list1.append("")
        font = pygame.font.Font(None,32)
        font_height = font.get_linesize()
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
    def tao2(self,screen,background1,jj,y):
        font = pygame.font.Font(None,32)
        font_height = font.get_linesize()
        screen.blit(background1,(0,0))
        print(list1)
        print("CCC")
        print("CCC")
        list1.append("tesita wo taosita")
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
        return list1
        jj.keikenchi = jj.keikenchi + 10
        print("kkk")
        xy = [x,y]
        sss(self,xxx,yyy)
        
class Save:
    """
    def __init__(self):
        self.x = x
        self.y = y
    def load(self):
        f = open("save.txt","r")
        xy = pickle.load(f)
        return xy
    def save(self,xy):
        f = open("save.txt","w")
        pickle.dump(xy2,f)

    f.write(str(self.x))
    f.write(str(self.y))
    f.write(str("\n"))
    """
class XY():
   ##def __init__(self,x,y):
   def load(self):
       try:
            f = open("test.txt","r")
            return xy
       except:
            f = open("test.txt","w")
   def save(self,xy):
       f = open("test.txt","w")
       pickle.dump(xy,f)
class kei():
   ##def __init__(self,x,y):
   def load(self):
       d = open("testkei.txt","r")
       self.keikenchi = pickle.load(d)
       return self.keikenchi
   def save(self,kk):
       d = open("testkei.txt","w")
       pickle.dump(self.keikenchi,d)
xxxyyy = XY()
keikei=kei()
xy =  xxxyyy.load()
xxx = xy[0]
yyy = xy[1]


jj= jizouclass() 
basho = xy
jj.keikenchi = keikei.load()
def field(basho):
            

    pygame.init()
    screen = pygame.display.set_mode((640,480),0,32)
    background = pygame.image.load(background_image_filename).convert()
    jizou = pygame.image.load(filename).convert_alpha()

    s = 0

    
    move_x,move_y = 0, 0
    r  =  random.random()*10
    xxx = basho[0]
    yyy = basho[1]
    """
    """
    while True:
        for event in pygame.event.get():
            #pygame.event.set_blocked([KEYDOWN,KEYUP])
            if event.type == QUIT:
                xy = [xxx,yyy]
                xxxyyy.save(xy)
                keikei.save(jj.keikenchi)
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
                xy = [xxx,yyy]
                xxxyyy.save(xy)
                keikei.save(jj.keikenchi)
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
   
        #xxx = ccc[0]
        #yyy = ccc[1]
        xxx+=move_x
        yyy+=move_y
            
        print("hhh")
        print(xxx)
        print(move_x)
        if move_x == 0.1 or  move_y == 0.1 or move_x == -0.1 or move_y == -0.1:
        #if move_x >= 1 or  y >= 1 or y <= 1 or x <= 1 :
            s = s + 1
        else:
            print("")
        if s == (10 + int(r*100)):
        #if s == 2:
            t = 1
            basho[0] = xxx + move_x
            basho[1] = yyy + move_y
            sentou()
            #mini.sentou(basho[0],basho[1])
             
            
       #screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(jizou,(xxx,yyy))
        print(xxx,yyy,"jfjkdlksjf",jj.keikenchi)
        print(xxx,yyy,"jfjkdlksjf",kkk,jj.keikenchi)

        
        pygame.display.update()
"""
class Player():
    def __init__(self,name):
        self.name = name
        self.hp = hp
        self.
        """
filename="ojizousan2.png"
filename2="tesita2.png"
background_image_filename = 'j.png'
basho = []
basho = xy
def sentou():
    time.sleep(1)
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
    y=0
 
    
    #list1 = []
    tesitajj = tesita1()
    teki = tesita1()
    pygame.init()
    background_image_filename = "sentou.png"
    screen = pygame.display.set_mode((640,480),0,32)
    background = pygame.image.load(background_image_filename).convert()
    jizou1 = pygame.image.load(filename).convert_alpha()
    tesita = pygame.image.load(filename2).convert_alpha()
    kou = pygame.image.load(filename3).convert_alpha()
    
    bou = pygame.image.load(filename4).convert_alpha()
    nige = pygame.image.load(filename5).convert_alpha()
    k2 = pygame.image.load(filename6).convert_alpha()
    
    b2 = pygame.image.load(filename7).convert_alpha()
    n2 = pygame.image.load(filename8).convert_alpha()
    waku = pygame.image.load(filename9).convert_alpha()
    back = pygame.image.load(filename9).convert_alpha()
    #x,y = 100, 200
    tesita_x,tesita_y = 400, 200
    move_x,move_y = 0, 0
    c = 1
    x2 =1
    y2 =1
    e =0
    playerpos=0
    event_text = []
    #list1 = []
    turn = 0
    screen.blit(background,(0,0))
    while True:
        if turn == 1:
            tesitajj.hit(screen,background,jj,y)
            turn = 0    
        if teki.hp <= 0:
            """
            jj.nigeru(screen,background,y)
            print("taosita")
            tesitajj.tao2(screen,background,jj,y)
            print("tttttt")
            """
            time.sleep(3)
            field(basho)

        print(teki.hp)
        print("teki")
        flag1=0
        screen.blit(jizou1,(100,200))
        screen.blit(tesita,(tesita_x,tesita_y))
        font = pygame.font.Font(None,32)
        pygame.draw.rect(screen,(0,0,0),(20,20,150,150))
        #pygame.draw.rect(screen,(0,0,0),(200,200,150,150))
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
            xy = [xxx,yyy]
            xxxyyy.save(xy)
            keikei.save(jj.keikenchi)
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
        playerpos %= 3
        if playerpos == 0:
            pygame.time.wait(100)
            screen.blit(waku,(60,300 ))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                #time.sleep(1)
                jj.hit(screen,background,teki,y)
                turn = 1
                print("$$$")
                flag1 = 1
                """
                tt = font.render("jizou no kougeki",False,(255,255,255))
                screen.blit(tt,(200,200))
                """
                if teki.hp  <= 0:
                    jj.nigeru(screen,background,y,tesitajj)
        elif playerpos == 1:
            pygame.time.wait(100)
            screen.blit(waku,(60,350 ))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                jj.bougyo(screen,background,y)
                turn = 1
                print("!!!")
        elif playerpos == 2:
            pygame.time.wait(100)
            screen.blit(waku,(60,400  ))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                jj.nigeru(screen,background,y)
                print("!!!")
            """
        if teki.hp <= 0:
            print("dddddddddddddddddddddddddd")
            screen.blit(background,(0,0))
            print("AAAAAAAAAAAAA")

            list1.append("tesita wo taosita!")
            list1.append("")
            font = pygame.font.Font(None,32)
            font_height = font.get_linesize()
            print("CCCCCCCCCCCCCCCC")
            for text in reversed(list1):
                screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
                y += font_height

            time.sleep(1)
    
            print("ssssssssssssssssssssssssssss")
            #tesitajj.death(jj.keikenchi)
            #jj.hit(screen,background,teki,y)
            #jj.levelup(screen,background,teki,y)
            field(basho)
            time.sleep(10)
            jj.tao(screen,background,teki,y)
            field(basho)
            """
        if jj.hp <= 0:
            field(basho)
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
        #first = raw_input("Who ").lower()
        


field(basho)
        

