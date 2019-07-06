class Person:

    def __init__(self,identy,attack):

        self.identy = identy
        self.attack = attack
        self.weapon = Weapon()
        self.life = 100

    def police(self,obj):
        # self.attack = attack
        obj.life -= self.attack
        # print('[%s]打了【%s】【%s】血，还剩【%s】'%(self.identy,obj.identy,self.attack, obj.life))
        # if obj.life <= 0:
        #     print('[%s]血量不足,已退出对局.'%('恐怖分子'))

    def turios(self,obj):
        obj.life -= self.attack
        # print('[%s]用【%s】打了【%s】【%s】血，还剩【%s】'%(self.identy,Weapon.name,obj.identy,self.attack,obj.life))
        # if obj.life <= 0:
        #     print('[%s]血量不足,已退出对局.'%('警察'))

    def log(self,obj):
        obj.life -= self.attack

        print('[%s]打了【%s】【%s】血，还剩【%s】' % (self.identy, obj.identy, self.attack, obj.life))
        if obj.life <= 0:
            print('[%s]血量不足,已退出对局.'%(obj.identy))

class Weapon():

    def gun(self,obj,attack):
        self.name = '枪'
        self.attack = attack
        obj.life -= self.attack
        self.print(obj)

    def rocket(self,obj,attack):
        self.name = '火箭炮'
        self.attack = attack
        obj.life -= self.attack
        self.print(obj)

    def boom(self, obj):
        self.name = '炸药包'
        self.attack = 100
        obj.life -= self.attack

        print('恐怖分子用[%s]杀死了所有玩家' % (self.name))



    # def kill(self):
    #     print('恐怖分子用[%s]杀死了所有玩家'%(self.name))


    def print(self, obj):

        print('[%s]被【%s】攻击了【%s】血,还剩[%s]'%(obj.identy, self.name,self.attack,obj.life))
        if obj.life <= 0:
            print('[%s]血量不足,已退出对局.'%(obj.identy))


p = Person('警察',80)
d = Person('恐怖分子',55)

p.log(d)

p.weapon.rocket(d,50)
d.weapon.gun(p,44)
d.weapon.boom(p)