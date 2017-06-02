class Unit(object):
    def __init__(self):
        self.name = None
        self.hp = None
        self.speed = None
        self.power = 5
        self.attrs = ['name', 'hp', 'speed', 'power']
    
    def attack(self):
        print("attack! -%d", self.power)
    
    def explain(self):
        for a in self.attrs:
            print("%s : %s" % (a, getattr(self,a)))


class Scv(Unit):
    def __init__(self):
        super(Scv, self).__init__()
        self.name = "scv"
        self.capacity = 7
        self.attrs.append('capacity')
    

class Marine(Unit):
    def __init__(self):
        super(Marine, self).__init__()
        self.name = "marine"
        self.power = 10
        
    def patrol(self):
        pass
    

class Vulture(Unit):
    def __init__(self):
        super(Vulture, self).__init__()
        self.name = "vulture"
        self.power = 25


if __name__ == '__main__':
    for u in [Scv(), Marine(), Vulture()]:
        print("\n%s:" % u.__class__)
        u.explain()
