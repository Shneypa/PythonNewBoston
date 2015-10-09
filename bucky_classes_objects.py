class Enemy:

    def __init__(self, life):
        self.life = life

    def attack(self):
        print("Ouch!")
        self.life -= 1

    def checklife(self):
        print(str(self.life) + " lives left")


class Tuna:

    def __init__(self):
        print("a tuna is born!")

    def swim(self):
        print(str(self) + " is swimming")





enemy1 = Enemy(5)
enemy2 = Enemy(100)

enemy1.attack()
enemy1.attack()

enemy1.checklife()
enemy2.checklife()


flipper = Tuna()
flipper.swim()