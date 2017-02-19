#-*- coding: utf-8 -*-
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
mtt = []
mt = []
list1 = []
y = 0
x = 0
xy = []
class Yakusou:
    def __init__(self):
        self.name  = "薬草"
        self.price = 100
    def buy(self,money):
        money = money - self.price  

class Gravia:
    def __init__(self):
        self.name = "グラビア"
        self.price = 100000000
yakusou = Yakusou()
gravia = Gravia()

class Tenin:
    def __init__(self):
        self.name = "店員"
        self.hp = 200
        self.mp = 30
        self.tuyosa=20
        self.keikenchiout=1000
        self.job = 3
        self.boss =1
        self.dead = 0
        self.zeni = 1000
    def hit(self,screen,background1,enemy,y):
        f =  int((1 * random.random()))
        enemy.hp -=  (self.tuyosa + f )
        #screen.blit(background1,(0,0))
        #time.sleep(1)
        list1.append("悪代官の攻撃")
        a = f + self.tuyosa

        list1.append(str(a) + "のダメージ")
        list1.append("")
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        font_height = font.get_linesize()
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
    def taosita():
        print()
tenin = Tenin()
class Akudaikan:
    def __init__(self):
        self.name = "悪代官"
        self.hp = 200
        self.mp = 30
        self.tuyosa=20
        self.keikenchiout=1000
        self.job = 1
        self.boss=1
        self.dead = 0
        self.zeni = 1000
    def hit(self,screen,background1,enemy,y):
        f =  int((1 * random.random()))
        enemy.hp -=  (self.tuyosa + f )
        #screen.blit(background1,(0,0))
        #time.sleep(1)
        list1.append("悪代官の攻撃")
        a = f + self.tuyosa

        list1.append(str(a) + "のダメージ")
        list1.append("")
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        font_height = font.get_linesize()
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
    def taosita():
        print()
class Jizouclass:
    def __init__(self):
        self.hp =20
        self.mp =10
        self.maxhp = 20
        self.tuyosa =8
        self.keikenchi=0
        self.list1 = []
        self.tttt = 1
        self.level = 1
        self.zeni =  0

    def buy(self,screen,background1,item,y):
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        font_height = font.get_linesize()
        list1.append(item.name + "を買った ")
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
            print(text+("AAAAAAA"))
            print(list1)

    def hit(self,screen,background1,enemy,y):
        f =  int((5 * random.random()))
        enemy.hp -=  (self.tuyosa + f )
        #screen.blit(background1,(0,0))
        list1.append("地蔵の攻撃")
        a = f + self.tuyosa
        list1.append(str(a) + "のダメージ")
        list1.append("")
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        font_height = font.get_linesize()
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
            print(text+("AAAAAAA"))
            print(list1)

            print(text+"BBBBBBB")
            print(list1)


    def bougyo(self,screen,background1,y):
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        font_height = font.get_linesize()
        screen.blit(background1,(0,0))
        print(list1)
        print("CCC")
        list1.append("地蔵の防御")
        pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
        return list1
        #t = 1
    def tao3(self,screen,background1,teki,y):
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        font_height = font.get_linesize()
        #screen.blit(background1,(0,0))
        print(list1)
        print("CCC")
        pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
        list1.append(teki.name + "を倒した ")
        self.zeni = self.zeni + teki.zeni
        list1.append(str(self.zeni)+"ゼニーを手に入れた")
        self.keikenchi = self.keikenchi + teki.keikenchiout
        list1.append(str(self.keikenchi)+"経験値を手に入れた")

        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
        if teki.dead == 1:
            time.sleep(2)
            field(basho)

        time.sleep(2)
        return list1

        
        #field(basho)
    def del1(self,list1):
        del list1[:]
        print(list1)

    def levelup(self,screen,background1,jizou2,enemy,y):
        if jizou2.keikenchi >= 60 and jizou2.level == 1 and jizou2.keikenchi <=99:

            jizou2.maxhp = jizou2.maxhp + int((3 * random.random())) + 10
            jizou2.tuyosa = jizou2.tuyosa +  int((3 * random.random())) + 5
            screen.blit(background1,(0,0))
            pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
            list1.append("地蔵レベルアップ２")
            jizou2.level=2
            font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
            font_height = font.get_linesize()
            for text in reversed(list1):
                screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
                y += font_height
        elif jizou2.keikenchi >= 100 and jizou2.level == 2 and jizou2.keikenchi <= 199:
            jizou2.maxhp = jizou2.maxhp + int((3 * random.random())) + 20
            jizou2.tuyosa = jizou2.tuyosa +  int((3 * random.random())) + 10
            screen.blit(background1,(0,0))
            pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
            list1.append("地蔵レベルアップ3")
            font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
            font_height = font.get_linesize()
            for text in reversed(list1):
                screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
                y += font_height
            jizou2.level=3
        elif jizou2.keikenchi >= 200 and jizou2.level == 3 and jizou2.keikenchi <= 299 :
            jizou2.maxhp = jizou2.maxhp + int((3 * random.random())) + 30
            jizou2.tuyosa = jizou2.tuyosa +  int((3 * random.random())) + 20
            screen.blit(background1,(0,0))
            pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
            list1.append("地蔵レベルアップ4")
            font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
            font_height = font.get_linesize()
            for text in reversed(list1):
                screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
                y += font_height
            jizou2.level=4
        elif jizou2.keikenchi >= 300 and jizou2.level == 4 and jizou2.keikenchi < 399:
            jizou2.maxhp = jizou2.maxhp + int((3 * random.random())) + 50
            jizou2.tuyosa = jizou2.tuyosa +  int((3 * random.random())) + 30
            screen.blit(background1,(0,0))
            pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
            list1.append("地蔵レベルアップ5")
            font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
            font_height = font.get_linesize()
            for text in reversed(list1):
                screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
                y += font_height
            jizou2.level=5
jj = Jizouclass() 
print("#lfskdjklajfdasl" + str(jj.level))
class Tesita:
    def __init__(self):
        self.name = "手下"
        self.hp =20
        self.mp =4
        self.tuyosa =3
        self.keikenchiout=90
        self.job=2
        self.boss=0
        self.dead=0
        self.zeni=100
    def hit(self,screen,background1,enemy,y):
        pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
        f =  int((1 * random.random()))
        enemy.hp -=  (self.tuyosa + f )
        screen.blit(background1,(0,0))
        pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
        #time.sleep(1)
        list1.append(self.name + "の攻撃")
        a = f + self.tuyosa

        list1.append(str(a) + "のダメージ")
        list1.append("")
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        font_height = font.get_linesize()
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
    def tao2(self,screen,background1,jj,y):
        font = pygame.font.Font(None,32)
        font_height = font.get_linesize()
        screen.blit(background1,(0,0))
        pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
        print(list1)
        print("CCC")
        print("CCC")
        list1.append("手下を倒した")
        for text in reversed(list1):
            screen.blit(font.render(text,True,(255,255,255)),(200,300-y))
            y += font_height
        return list1
        jj.keikenchi = jj.keikenchi + teki.keikenchiout
        xy = [x,y]
        sss(self,xxx,yyy)
        """
        
        """
class XY():
   ##def __init__(self,x,y):
   def load(self):
       f = open("test.txt","rb")
       xy = pickle.load(f)
       return xy
   def save(self,xy):
       f = open("test.txt","wb")
       pickle.dump(xy,f)
class Status():
   ##def __init__(self,x,y):
   def load(self):
       try:
            d = open("status.txt","rb")
            aa = pickle.load(d)
            return aa
       except IOError:
            d = open("status.txt","wb")
            kk = []
            pickle.dump(kk,d)

   def save(self,mt):
       d = open("status.txt","wb")
       pickle.dump(mt,d)
class level():
    def levelups(jp):
        jp.hp = jp + 10
        jp.tuyosa = jp.tuyosa + 5
class reset():
    def ii(self,defjj,xxxyyy):
        jj.keikenchi = 0
        jj.maxhp = 20
        jj.tuyosa = 10
        jj.level = 1
        jj.zeni =0
        xy = xxxyyy.load

status = Status()
levjj= []
xxxyyy = XY()
xy =  xxxyyy.load()
xxx = xy[0]
yyy = xy[1]
#jj.level=1
resetjj = reset()
levelupjj = level()
mtt = status.load()




basho = xy
jj.maxhp = mtt[0]
jj.tuyosa = mtt[1]
jj.keikenchi= mtt[2]
jj.level= mtt[3]
jj.zeni= mtt[4]
def yorozu(teki):
    time.sleep(1)
    print(teki)
    filename = []
    flag = 0
    filename="ojizousan2.png"
    filename9="waku2.png"
    filename10="back.png"
    background_image_filename = 'j.png'
    y=0
 
    pygame.init()
    background_image_filename = "sentou.png"
    screen = pygame.display.set_mode((640,480),0,32)
    background = pygame.image.load(background_image_filename).convert()
    jizou1 = pygame.image.load(filename).convert_alpha()
    tesita = pygame.image.load(filename2).convert_alpha()
    waku = pygame.image.load(filename9).convert_alpha()
    back = pygame.image.load(filename9).convert_alpha()
    akuimage = pygame.image.load(filename13).convert_alpha()
    tenin_image = pygame.image.load(filename14).convert_alpha()
    tesita_x,tesita_y = 400, 200
    move_x,move_y = 0, 0
    jj.hp = jj.maxhp
    print(jj.hp)
    c = 1
    x2 =1
    y2 =1
    e =0
    playerpos=0
    event_text = []
    #list1 = []
    turn = 0
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
    while True:
        if turn == 1:
            teki.hit(screen,background,jj,y)
            turn = 0    
        if teki.hp <= 0:
            time.sleep(3)
            field(basho)
        flag1=0
        screen.blit(jizou1,(100,200))
        if teki.job == 2:
            screen.blit(tesita,(tesita_x,tesita_y))
        elif teki.job == 3:
            screen.blit(tenin_image,(400,200))
            """
        elif teki.job == 1:
            screen.blit(akuimage,(300,100))
            """
        else:
            print()
            
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        pygame.draw.rect(screen,(0,0,0),(20,20,150,150))
        pygame.draw.rect(screen,(0,0,0),(20,300,150,150))
        #pygame.draw.rect(screen,(0,0,0),(200,200,150,150))
        text = font.render(str(jj.hp),False,(255,255,255))
        screen.blit(text,(60,30))
        text = font.render(str(jj.mp),False,(255,255,255))
        screen.blit(text,(60,60))
        text = font.render(str(jj.level),False,(255,255,255))
        screen.blit(text,(60,90))
        text = font.render(str(jj.keikenchi),False,(255,255,255))
        screen.blit(text,(60,120))
        text = font.render("HP",False,(255,255,255))
        screen.blit(text,(20,30))
        text = font.render("MP",False,(255,255,255))
        screen.blit(text,(20,60))
        text = font.render("Lv",False,(255,255,255))
        screen.blit(text,(20,90))
        text = font.render(str(jj.zeni) ,False,(255,255,255))
        screen.blit(text,(20,120))
        text = font.render(str(tenin.name),False,(0,0,0))
        screen.blit(text,(400,120))
        #text = font.render("経験値",False,(255,255,255))
        #screen.blit(text,(20,100))
        yakusou.price=100
        yakusou.name = "薬草"
        text = font.render(yakusou.name+ str(yakusou.price)+"ゼニー",False,(255,255,255))
        screen.blit(text,(20,300))
        gravia.price=100000000000
        gravia.name = "グラビア"
        text = font.render(gravia.name + str(gravia.price)+ "ゼニー",False,(255,255,255))
        screen.blit(text,(20,330))
        text = font.render("店を出る",False,(255,255,255))
        screen.blit(text,(20,360))
        #screen.blit(kou,(60,300))
        #screen.blit(bou,(60,350))
        #screen.blit(nige,(60,400))
        #background2 = [kou,bou,nige]
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
            mt = [jj.maxhp,jj.tuyosa,jj.keikenchi,jj.level.jj.zeni]
            status.save(mt)
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
            screen.blit(waku,(20,300 ))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                #time.sleep(1)
                jj.zeni = jj.zeni - yakusou.price
                jj.buy(screen,background,yakusou,y)
                #    jj.nigeru(screen,background,y)
        elif playerpos == 1:
            pygame.time.wait(100)
            screen.blit(waku,(20,330 ))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                jj.zeni = jj.zeni - gravia.price
                jj.buy(screen,background,gravia,y)
        elif playerpos == 2:
            pygame.time.wait(100)
            screen.blit(waku,(20,360  ))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                jj.keikenchi = 0
                if teki.boss == 1:
                    basho[1] = 400
                    field(basho)
                else:
                    print()
                field(basho)
                print("!!!")
        if jj.hp <= 0:
            basho[0] = 400
            field(basho)
        flag1=1
        
        def kougeki():
            r2 = int(r)
            if r2 >= 7:
                damege = tuyosa + 1
            elif r2 >= 3:
                damege = tuyosa + 3
            elif r2 >= 0:
                damege = tuyosa + 5
        pygame.display.update()
    
    
    
    
    
    
    def up():
        pygame.draw.rect(screen,(255,255,255),(60,300,100,20),5)
    def down():
        pygame.draw.rect(screen,(255,255,255),(60,300,100,20),5)

    def bougyo():
        screen = pygame.display.set_mode((640,480),0,32)
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        text = font.render("bougyo",False,(255,255,255))
        screen.blit(text,(120,280))
        pygame.display.update()
        #first = raw_input("Who ").lower()
        
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
    tttt = 1
    while True:
        #print("#lfskdjklajfdasl" + str(jj.level))
        for event in pygame.event.get():
            #pygame.event.set_blocked([KEYDOWN,KEYUP])
            if event.type == QUIT:
                xy = [xxx,yyy]
                xxxyyy.save(xy)
                mt = [jj.maxhp,jj.tuyosa,jj.keikenchi,jj.level,jj.zeni]
                status.save(mt)
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
                mt = [jj.maxhp,jj.tuyosa,jj.keikenchi,jj.level,jj.zeni]
                status.save(mt)
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
        #jyyy = ccc[1]
        print("llllllll"+str(jj.level))
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
            """
        if yyy < 100:
            aku = Akudaikan()
            sentou(aku)
            """
        if yyy >400:
            basho[0] = xxx + move_x
            basho[1] = yyy + move_y
            tenin = Tenin()
            yorozu(tenin)
            basho[1] = yyy - 100
            """
        if xxx > 500:
            basho[0] = xxx + move_x
            basho[1] = yyy + move_y
            aku = Akudaikan()
            sentou(aku)
            basho[0] = xxx + move_x - 100
            """



        if s == (10 + int(r*100)):
        #if s == 2:
            #t = 1
            basho[0] = xxx + move_x
            basho[1] = yyy + move_y
            tesi = Tesita()
            sentou(tesi)

            #mini.sentou(basho[0],basho[1])
             
            
       #screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(jizou,(xxx,yyy))
        levjj = (jj.maxhp,jj.tuyosa)
        print(xxx,yyy,"jfjkdlksjf",jj.keikenchi,jj.hp,jj.tuyosa)
        print(xxx,yyy,"jfjkdlksjf",jj.keikenchi,levjj)

        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        text = font.render('Reset', False, (55,205,55))
        screen.blit(text,(420,20))
        text = font.render("ゼニー"+str(jj.zeni), False, (225,205,55))
        screen.blit(text,(220,20))
        pressed_mouse = pygame.mouse.get_pressed()

        mpos = pygame.mouse.get_pos()
        print(mpos)
        print(pygame.mouse.get_pressed())
        if mpos[0] > 420 and mpos[1] > 20 and mpos[0] < 500 and mpos[1] < 40 and pygame.mouse.get_pressed()[0] == 1 :
            print("jjjjjjj")
            print(jj.keikenchi)
            jj.keikenchi = 0
            jj.maxhp = 20
            jj.tuyosa = 10       
            jj.level=1
            xxx = 10
            yyy = 180
        
        pygame.display.update()
filename="ojizousan2.png"
filename13="akudaikan.png"
filename14="tenin.png"

background_image_filename = 'j.png'
basho = []
basho = xy
def sentou(teki):
    time.sleep(1)
    print(teki)
    filename = []
    flag = 0
    filename="ojizousan2.png"
    filename9="waku2.png"
    filename10="back.png"
    background_image_filename = 'j.png'
    y=0
 
    pygame.init()
    background_image_filename = "sentou.png"
    screen = pygame.display.set_mode((640,480),0,32)
    background = pygame.image.load(background_image_filename).convert()
    jizou1 = pygame.image.load(filename).convert_alpha()
    tesita = pygame.image.load(filename2).convert_alpha()
    waku = pygame.image.load(filename9).convert_alpha()
    back = pygame.image.load(filename9).convert_alpha()
    akuimage = pygame.image.load(filename13).convert_alpha()
    tesita_x,tesita_y = 400, 200
    move_x,move_y = 0, 0
    jj.hp = jj.maxhp
    print(jj.hp)
    c = 1
    x2 =1
    y2 =1
    e =0
    playerpos=0
    event_text = []
    #list1 = []
    turn = 0
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,(0,0,0),(170,100,220,270))
    while True:
        if turn == 1:
            teki.hit(screen,background,jj,y)
            turn = 0    
        if teki.hp <= 0:
            time.sleep(3)
            field(basho)
        flag1=0
        screen.blit(jizou1,(100,200))
        if teki.job == 2:
            screen.blit(tesita,(tesita_x,tesita_y))
        elif teki.job == 1:
            screen.blit(akuimage,(300,100))
        else:
            print()
            
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        pygame.draw.rect(screen,(0,0,0),(20,20,150,150))
        pygame.draw.rect(screen,(0,0,0),(20,300,150,150))
        #pygame.draw.rect(screen,(0,0,0),(200,200,150,150))
        text = font.render(str(jj.hp),False,(255,255,255))
        screen.blit(text,(60,30))
        text = font.render(str(jj.mp),False,(255,255,255))
        screen.blit(text,(60,60))
        text = font.render(str(jj.level),False,(255,255,255))
        screen.blit(text,(60,90))
        text = font.render(str(jj.keikenchi),False,(255,255,255))
        screen.blit(text,(150,120))
        text = font.render("HP",False,(255,255,255))
        screen.blit(text,(20,30))
        text = font.render("MP",False,(255,255,255))
        screen.blit(text,(20,60))
        text = font.render("Lv",False,(255,255,255))
        screen.blit(text,(20,90))
        text = font.render("経験値",False,(255,255,255))
        screen.blit(text,(20,120))
        text = font.render("攻撃",False,(255,255,255))
        screen.blit(text,(20,300))
        text = font.render("防御",False,(255,255,255))
        screen.blit(text,(20,330))
        text = font.render("逃げる",False,(255,255,255))
        screen.blit(text,(20,360))
        #text = font.render("経験値",False,(255,255,255))
        #screen.blit(text,(20,100))
        #screen.blit(kou,(60,300))
        #screen.blit(bou,(60,350))
        #screen.blit(nige,(60,400))
        #background2 = [kou,bou,nige]
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
            mt = [jj.maxhp,jj.tuyosa,jj.keikenchi,jj.level.jj.zeni]
            status.save(mt)
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
            screen.blit(waku,(20,300 ))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                #time.sleep(1)
                jj.hit(screen,background,teki,y)
                if teki.hp <=0:
                    jj.tao3(screen,background,teki,y)
                    levjj = (jj.maxhp,jj.tuyosa)
                    if jj.keikenchi >= 90 and jj.level == 1 :
                        jj.levelup(screen,background,jj,teki,y)
                        jj.level = 2
                    elif jj.keikenchi >= 100 and jj.level == 2:
                        jj.levelup(screen,background,jj,teki,y)
                        jj.level = 3
                    elif jj.keikenchi >= 200 and jj.level == 3:
                        jj.levelup(screen,background,jj,teki,y)
                        jj.level = 4
                    elif jj.keikenchi >= 300 and jj.level == 4:
                        jj.levelup(screen,background,jj,teki,y)
                        jj.level = 5
                    #levelupjj.levelup(jj)

                turn = 1
                print("$$$")
                flag1 = 1
                #    jj.nigeru(screen,background,y)
        elif playerpos == 1:
            pygame.time.wait(100)
            screen.blit(waku,(20,330 ))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                jj.bougyo(screen,background,y)
                turn = 1
                print("!!!")
        elif playerpos == 2:
            pygame.time.wait(100)
            screen.blit(waku,(20,360  ))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                jj.keikenchi = 0
                if teki.boss == 1:
                    basho[0] = 200
                    basho[1] = 200
                    field(basho)
                    print("jjjj")
                else:
                    print()
                field(basho)
                print("!!!")
        if jj.hp <= 0:
            basho[0] = 400
            field(basho)
        flag1=1
        
        def kougeki():
            r2 = int(r)
            if r2 >= 7:
                damege = tuyosa + 1
            elif r2 >= 3:
                damege = tuyosa + 3
            elif r2 >= 0:
                damege = tuyosa + 5
        pygame.display.update()
    
    
    
    
    
    
    def up():
        pygame.draw.rect(screen,(255,255,255),(60,300,100,20),5)
    def down():
        pygame.draw.rect(screen,(255,255,255),(60,300,100,20),5)

    def bougyo():
        screen = pygame.display.set_mode((640,480),0,32)
        font = pygame.font.Font("VL-Gothic-Regular.ttf",32)
        text = font.render("bougyo",False,(255,255,255))
        screen.blit(text,(120,280))
        pygame.display.update()
        #first = raw_input("Who ").lower()
        


field(basho)
        
