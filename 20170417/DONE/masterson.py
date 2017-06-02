class Unit(object):
    def __init__(self, name, hp, move):
        self.name = name
        self.hp = hp
        self.move = move
        self.atk = 5
    def attack(self):
        pass

class SCV(Unit):
    def __init__(self, name, speed, atk):
        super(SCV, self).__init__(name,60,5)
        self.speed=speed
        self.atk=atk

    def attack(self):
        super.attack()

    def explain(self):
        print("SCV info")
        print("name %s", self.name)
        print("hp %d", self.hp)
        print("move %d", self.move)
        print("speed %d", self.speed)
        print("Attack %d", self.atk)

    def repair(self):
        print("i will kill you")

class Marine(Unit):
    def __init__(self, name):
        super(Marine, self).__init__(name,50,4)
        self.atk=10

    def explain(self):
        print("Marine info")
        print("name %s", self.name)
        print("hp %d", self.hp)
        print("move %d", self.move)
        print("Attack %d", self.atk)

    def attack(self):
        print("%d damage",self.atk)

    def patrol(self):
        pass

class Vulture(Unit):
    def __init__(self, name):
        super(Vulture, self).__init__(name,80,15)
        self.atk=25
        self.mine=2

    def explain(self):
        print("Vulture info")
        print("name %s", self.name)
        print("hp %d", self.hp)
        print("move %d", self.move)
        print("Attack %d", self.atk)
        print("mine %d", self.mine)
    def attack(self):
        print("%d damage", self.atk)

def main():
    sc = SCV("labor1",5, 5)
    I = Marine("jim")
    I.attack()
    I.explain()
    V = Vulture("jjim")
    V.attack()
    V.explain()

if __name__ == '__main__':
    main()
