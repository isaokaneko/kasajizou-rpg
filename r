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
    def nigeru(self,screen,background1,y):
        font = pygame.font.Font(None,32)
        font_height = font.get_linesize()
        screen.blit(background1,(0,0))
        print(list1)
        print("CCC")
        list1.append("tesita wo taosita")
        jj.keikenchi = jj.keikenchi + 10
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
        
