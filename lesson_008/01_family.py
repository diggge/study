# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.man_food = 50
        self.dirt = 0

    def __str__(self):
        return ' В доме еды осталось: {}, денег осталось: {}, степень загрязности дома: {}'.format(self.man_food,
                                                                                                   self.money,
                                                                                                   self.dirt)
class Human:
    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return 'У {} сытость :{},уровень счастья : {}'.format(self.name, self.satiety, self.happiness)

    def eat(self):
        if self.house.man_food <= 0:
            self.satiety -= 10
            print(Fore.RED + 'нет еды, {} голодает'.format(self.name))
        elif 0 < self.house.man_food < 30:
            self.satiety += self.house.man_food
            print(Fore.LIGHTRED_EX + '{} съел остатки еды'.format(self.name))
        else:
            self.satiety += 30
            self.house.man_food -= 30
            print(Fore.CYAN + '{} поел'.format(self.name))

    def go_to_house(self, house):
        self.house = house
        print(Fore.BLUE + '{} въехал домой'.format(self.name))

    def act(self):

        if (self.satiety <= 0 or self.happiness <= 0):
            print(Fore.RED + '{} вышел из игры'.format(self.name))
            return
        if 0 < self.satiety <= 31:
            self.eat()

class Wife(Human):
    def __init__(self, name):
        super().__init__(name=name)
        self.husband = None

    def __str__(self):
        return super().__str__()

    def shopping(self):
        print(Fore.LIGHTBLUE_EX + '{} сходила в магазин за едой'.format(self.name))
        self.happiness += 10
        self.satiety -= 10
        if 0 <= self.house.money <= 100:
            self.house.man_food += self.house.money
            self.house.money = 0
        else:
            self.house.man_food += 100
            self.house.money -= 100

    def buy_fur_coat(self):
        print(Fore.LIGHTRED_EX + '{} купила себе шубу'.format(self.name))
        self.happiness += 60
        self.satiety -= 10
        self.house.money -= 350
        self.husband.happiness -= 100

    def clean_house(self):
        print(Fore.LIGHTMAGENTA_EX + '{} убирается в доме '.format(self.name))
        self.satiety -= 10
        self.happiness -= 10
        self.husband.happiness +=10
        if (0 <= self.house.dirt <= 100):
            self.house.dirt = 0
        else:
            self.house.dirt -= 100

    def make_up(self):
        print(Fore.LIGHTGREEN_EX + '{} сидела красилась весь день'.format(self.name))
        self.satiety -= 10
        self.happiness += 10
    def create_family(self,husband):
        self.husband = husband
        print(Fore.LIGHTWHITE_EX + '{} согласилась выйти замуж за {}'.format(self.name, self.husband.name))

    def act(self):
        super().act()
        what_to_do = randint(1, 6)
        if self.house.dirt > 80:
            self.clean_house()
        elif self.house.money > 500:
            self.buy_fur_coat()
        elif self.house.man_food < 50:
            self.shopping()
        elif what_to_do == 1:
            self.make_up()
        elif what_to_do ==2:
            self.clean_house()
        elif what_to_do == 3:
            self.shopping()
        else:
            self.make_up()

class Husband(Human):
    def __init__(self, name):
        super().__init__(name=name)
        self.wife = None

    def __str__(self):
        return super().__str__()

    def work(self):
        print(Fore.MAGENTA + '{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.satiety -= 10

    def gaming(self):
        print(Fore.LIGHTGREEN_EX + '{} сидел играл весь день'.format(self.name))
        self.satiety -= 10
        self.happiness += 20
    def create_family(self, wife):
        self.wife = wife
        print(Fore.LIGHTWHITE_EX + '{} согласился взять в жены {}'.format(self.name, self.wife.name))
    def act(self):
        super().act()
        what_to_do = randint(1, 6)
        if self.happiness < 40:
            self.gaming()
        elif self.house.money < 100:
            self.work()
        elif what_to_do ==1:
            self.work()
        elif what_to_do == 2:
            self.gaming()
        elif what_to_do == 3:
            self.work()
        else:
            self.gaming()


house = House()
anatoly = Husband(name='Анатолий')
evgeniya = Wife(name='Евгения')
print(house)
evgeniya.create_family(husband=anatoly)
anatoly.create_family(wife=evgeniya)
evgeniya.go_to_house(house)
anatoly.go_to_house(house)
print(house)

for day in range(365):
    print(Fore.GREEN + '================== День {} =================='.format(day))
    print(house)
    house.dirt += 5
    anatoly.act()
    evgeniya.act()
    print(anatoly)
    print(evgeniya)
    print(house)

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass

# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# house = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
