class muzh:
    def __init__(self,name):
        self.name = name
        self.fullness = 50
        self.house = None
    def __str__(self):
        return 'я - {}, сытость {}'.format(self.name,self.fullness)
    def eat(self):
        self.fullness +=30
        self.house.food -=10
        print('{} поел'.format(self.name))
    def go_to_house(self,house):
        self.house=house
        self.fullness -= 10
        print('{} вьехал в дом'.format(self.name))
class house:
    def __init__(self):
        self.food = 50
    def __str__(self):
        return 'в доме еды осталось {}'.format(self.food)

my_home=house()
muzh=muzh(name='муж')
print(muzh)
muzh.go_to_house(my_home)
muzh.eat()
print(muzh)
