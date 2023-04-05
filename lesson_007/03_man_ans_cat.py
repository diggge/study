# -*- coding: utf-8 -*-
from random import randint
from colorama import Fore, Back, Style
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.
# TODO здесь ваш код
class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.health = 50
        self.entertainment = 50
        self.home= None
        self.man= None
    def __str__(self):
        return 'Я - {}, сытость {},здоровье {},развлечение {}'.format(self.name,self.fullness,self.health,self.entertainment)
    def eat(self):
        if self.home.cat_food >=20:
            print(Fore.YELLOW+ '{} поел'.format(self.name))
            self.fullness+=30
            self.home.cat_food-=20
            self.entertainment-=10
        else:
            print(Fore.RED+'{} нет еды'.format(self.name))
    def sleep(self):
        print(Fore.GREEN+ '{} поспал'. format(self.name))
        self.health+=30
        self.entertainment-=10
        self.fullness-=10
    def tearing_wallpaper(self):
        print(Fore.CYAN+ '{} дерет обои'. format(self.name))
        self.entertainment+=30
        self.fullness-=10
        self.man.nervous_system-=20
        self.home.cleanlinesss-=10

    def go_to_the_home(self, home):
        self.home = home
        self.fullness -= 10
        print(Fore.CYAN+'{} Вьехал в дом'.format(self.name))

    def go_to_the_man(self, man):
        self.man = man
        self.fullness -= 10
        print(Fore.CYAN + '{} Вьехал в человека'.format(self.name))

    def act(self):
        if (self.fullness<=0 or self.health<=0 or self.entertainment<=0):
            print(Fore.RED+'{} откинул копыта'. format(self.name))
        dice = randint(1, 6)
        if self.fullness<=30:
            self.eat()
        elif self.health<=30:
            self.sleep()
        elif self.entertainment<=30:
            self.tearing_wallpaper()
        elif dice==1:
            self.eat()
        elif dice==2:
            self.sleep()
        else:
            self.tearing_wallpaper()
class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 80
        self.nervous_system = 80
        self.home = None
    def __str__(self):
        return 'Я - {}, сытость {},нервная система {}'.format(self.name, self.fullness, self.nervous_system)
    def eat(self):
        if self.home.man_food >= 20:
            print(Fore.YELLOW+'{} поел'.format(self.name))
            self.fullness += 10
            self.home.man_food -= 10
        else:
            print(Fore.RED+'{} нет еды'.format(self.name))
    def work(self):
        print(Fore.RESET+'{} сходил на работу'.format(self.name))
        self.home.money += 150
        self.fullness -= 10
    def watch_MTV(self):
        print(Fore.LIGHTBLUE_EX+'{} смотрел MTV целый день'.format(self.name))
        self.fullness -= 10
        self.nervous_system+=20
    def shopping(self):
        if self.home.money >= 50:
            print(Fore.MAGENTA+'{} сходил в магазин за едой'.format(self.name))
            self.home.money -= 50
            self.nervous_system+=20
            self.home.man_food += 50
            self.home.cat_food += 50
        else:
            print(Fore.RED+'{} деньги кончились!'.format(self.name))
    def go_to_the_home(self, home):
        self.home = home
        self.fullness -= 10
        print(Fore.CYAN+'{} Вьехал в дом'.format(self.name))
    # def pick_up_a_cat(self,cat,home):
    #     self.home=home
    #     self.cat=cat
    #     cat.go_to_the_home(self)
    #     self.fullness -=10
    #     print(Fore.CYAN+'{} Подобрал кота {} в дом {}'.format(self.name, self.cat, self.home))
    def clean_home(self):
        # self.home = home
        self.home.cleanlinesss-=20
        self.fullness-=10
        self.nervous_system-=10
    def caress_cat(self):
        self.nervous_system+=50
        self.fullness -= 10


    def act(self):
        if (self.fullness <= 0 or self.nervous_system <=0 ):
            print(Fore.RED+ '{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.home.man_food < 30:
            self.shopping()
        elif self.home.money < 100:
            self.work()
        elif self.home.cleanlinesss <30:
            self.clean_home()
        elif self.nervous_system <30:
            self.caress_cat()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()
            
class Home:
    def __init__(self):
        self.man_food = 50
        self.cat_food = 50
        self.money = 50
        self.cleanlinesss = 0
    def __str__(self):
        return 'В доме еды осталось {}, кошачей еды осталось {},денег осталось {}, уровень грязности дома {}'.format(self.man_food,self.cat_food, self.money,self.cleanlinesss)
    
my_sweet_home = Home()
busya = Cat(name='Busya')
filippo = Man(name='Filippo')
busya.go_to_the_home(home=my_sweet_home)
filippo.go_to_the_home(home=my_sweet_home)
busya.go_to_the_man(man=filippo)
# filippo.pick_up_a_cat(cat=busya, home=my_sweet_home)
for day in range(1, 60):
    print('================ день {} =================='.format(day))
    filippo.act()
    busya.act()
    print('---------------- в конце дня --------------')
    print(filippo)
    print(busya)
    print(my_sweet_home)






# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
