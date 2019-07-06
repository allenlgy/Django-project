class Person(object):

    def __init__(self, name, age, sex):

        self.name = name
        self.age = age
        self.sex = sex

    def to_do(self, something):

        print('%s,%s,%s,%s'%(self.name,self.age,self.sex, something))


d = Person('小明','10岁','男')
d.to_do('上山去砍柴')

b = Person('老李','90岁','男')
b.to_do('最爱大保健')
