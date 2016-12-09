class test():
    a = 100
    def __init__(self):
        self.ttt=30
        self.keikenchi = 10
    def pri(self):
        tt = 20
        print(20)
        self.keikenchi = 100
        self.keikenchi = self.keikenchi + 10
        print(self.keikenchi)
        print("ff")
ttt = test()
print(ttt.a)
print(ttt.keikenchi)
ttt.pri()
