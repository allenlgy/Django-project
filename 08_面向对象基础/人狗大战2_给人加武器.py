class Dog(object):
    role = 'dog'

    def __init__(self, name, breed, attack):

        self.name = name
        self.breed = breed
        self.attack = attack
        self.life = 100

    def bite(self,person):  # 这里传进来的是一个对象
        person.life -= self.attack
        print("狗【%s】咬了人[%s]%s血，人还剩[%s]"%(self.name,person.name,self.attack,person.life))

class Weapon():

    def knif(self,obj):
        self.name = '屠龙刀'
        self.attack = 60
        obj.life -= self.attack
        self.print(obj)


    def print(self, obj):
        print('[%s]被【%s】攻击了【%s】血,还剩[%s]'%(obj.name,self.name,self.attack,obj.life))

class Person(object):
    role = 'person'

    def __init__(self, name,sex,attack ):
        self.name = name
        self.sex = sex
        self.attack = attack
        self.life = 10
        self.weapon = Weapon()  # 实例化一个weapon对象

    def attack_d(self,dog):  # 这里传进来的是一个对象
        dog.life -= self.attack
        print('人【%s】攻击了【%s】【%s】血，狗还剩【%s】'%(self.name,dog.name,self.attack,dog.life))

d = Dog('旺财','哈士奇',30)
p = Person('小明','男',500)

# d.bite(p)
# p.attack_d(d)

p.weapon.knif(d)