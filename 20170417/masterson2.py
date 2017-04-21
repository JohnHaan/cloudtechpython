class Animal(object):
    def __init__(self):
        print("Hive")

class Tiger(Animal):
    def __init__(self):
        super(Tiger, self).__init__()
        print("Tiger init")
    def jump(self):
        print("tiger is character")
    def cry(self):
        print("tiger JK")

class Lion(Animal):
    def __init__(self):
        super(Lion, self).__init__()
        print("Lion init")
    def bite(self):
        print("i will kill you")
    def cry(self):
        print("Simba")

class Liger(Lion, Tiger):
    def __init__(self):
        super(Liger, self).__init__()
        print("Liger Init")
        
I = Liger()
