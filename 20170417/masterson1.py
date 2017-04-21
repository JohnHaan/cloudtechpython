class Infra(object):
    name = "infra"
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members
    def wtd(self):
        print("%s for infra" % self.leader)
    def count_members(self):
        print(self.members)

class Cloudtechteam(Infra):
    def __init__(self, leader, members, gender, age):
        super(Cloudtechteam, self).__init__(leader, members)
        self.gender = gender
        self.age = age
    def wtd(self):
        print("%s is creator, age: %d"% (self.leader,self.age))
    def count_members(self):
        print("how many people in there")
        super().count_members()


c = Cloudtechteam("lee",8,"man",36)
c.wtd()
c.count_members()