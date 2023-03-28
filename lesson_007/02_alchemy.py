# -*- coding: utf-8 -*-
# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
# TODO здесь ваш код
# Elementy=[Water,Air,Fire,Earth,storm,steam,dirt,ligthing,dust,lava]

class Water:
    def __str__(self):
        return 'Вода'
    def __add__(self, other):
        if isinstance(other,Air):
            return Storm(part1=self,part2=other)
        elif isinstance(other,Fire):
            return Steam(part1=self,part2=other)
        elif isinstance(other,Earth):
            return Dirt(part1=self,part2=other)
class Air:
    def __str__(self):
        return 'Воздух'
    def __add__(self,other):
        if isinstance(other, Fire):
            return Lighting(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dust(part1=self, part2=other)
class Fire:
    def __str__(self):
        return 'Огонь'
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava(part1=self, part2=other)
class Earth:
    def __str__(self):
        return 'Земля'
    # def __add__(self, other):
    #     if isinstance(other, Earth):
    #         return Lava(part1=self, part2=other)

class Storm:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
    def __str__(self):
        return 'Игра Алхимик. Соединение двух элементов: ' + str(self.part1) + ' + ' + str(self.part2) + '  = Шторм'
class Steam:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
    def __str__(self):
        return 'Игра Алхимик. Соединение двух элементов: ' + str(self.part1) + ' + ' + str(self.part2) + '  = Пар'

class Dirt:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Игра Алхимик. Соединение двух элементов: ' + str(self.part1) + ' + ' + str(self.part2) + '  = Грязь'

class Lighting:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
    def __str__(self):
        return 'Игра Алхимик. Соединение двух элементов: ' + str(self.part1) + ' + ' + str(self.part2) + '  = Молния'

class Dust:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Игра Алхимик. Соединение двух элементов: ' + str(self.part1) + ' + ' + str(self.part2) + '  = Пыль'

class Lava:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Игра Алхимик. Соединение двух элементов: ' + str(self.part1) + ' + ' + str(self.part2) + '  = Лава'

print(Water()+Air())
print(Water()+Fire())
print(Water()+Earth())
print(Air()+Fire())
print(Air()+Earth())
print(Fire()+Earth())



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
