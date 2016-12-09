class Player:
    def __init__(self):

        self.hp = 20 
        self.mp = 10 
        self.keikenchi=0
    
    def hit(self):
        self.hp -= 5

player = Player()
while 1:
    
    print(player.hp)
    first=raw_input("kougeki").lower()
    if first=="a":
        player.hit()
    
    if player.hp == 0:
        print("Game Over")
        break
    print(player.hp)
