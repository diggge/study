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

def __init__(self, name):
    self.name = name
    self.satiety = 30
    self.happiness = 100
    self.house = None
    self.cat = None

    def eat(self):
        if self.house.man_food <= 0:
            self.satiety -= 10
            print(Fore.RED + 'нет еды, {} голодает'.format(self.name))
        elif 0 < self.house.man_food < 30:
            self.satiety += self.house.man_food
            self.house.man_food = 0
            print(Fore.LIGHTRED_EX + '{} съел остатки еды'.format(self.name))
        else:
            self.satiety += 30
            self.house.man_food -= 30
            print(Fore.CYAN + '{} поел'.format(self.name))

def __init__(self, name):
    self.name = name
    self.satiety = 30
    self.happiness = 100
    self.house = None
    self.cat = None

    def eat(self):
        if self.house.man_food <= 0:
            self.satiety -= 10
            print(Fore.RED + 'нет еды, {} голодает'.format(self.name))
        elif 0 < self.house.man_food < 30:
            self.satiety += self.house.man_food
            self.house.man_food = 0
            print(Fore.LIGHTRED_EX + '{} съел остатки еды'.format(self.name))
        else:
            self.satiety += 30
            self.house.man_food -= 30
            print(Fore.CYAN + '{} поел'.format(self.name))