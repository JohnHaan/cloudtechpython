
class Infrasil(object):
    name = "infra"
    
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members
    
    def what_to_do(self):
        print("%s manage." % self.leader)
    
    def count_members(self):
        print(self.members)

class Cloudtechteam(Infrasil):
    def __init__(self, leader, members, gender, age):
        # Infrasil.__init__(self, leader, members)
        # self.leader = leader
        # self.members = members
        super(Cloudtechteam,self).__init__(leader, members)
        self.gender = gender
        self.age = age
    
    def what_to_do(self):
        print("%s leads %s, %d" % ( self.leader, self.gender, self.age) )
    
    def count_members(self):
        super().count_members()

a = Infrasil("kang", 30)
print(a.name)
a.name = "infra-dev"
print(a.name)
a.what_to_do()
a.count_members()

c = Cloudtechteam("lee", 8, "man", 36)
print(c.leader, c.members)
c.what_to_do()
c.count_members()
