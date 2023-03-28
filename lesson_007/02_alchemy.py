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
Elementy=[Water,Air,Fire,Earth,storm,steam,dirt,ligthing,dust,lava]

class Water:
    def __str__(self):
        return 'Я вода'
    def __add__(self, other):
        return Alchemy(part1=self, part2=other)
class Air:
    def __str__(self):
        return 'Я воздух'
    def __add__(self, other):
        return Alchemy(part1=self, part2=other)
class Fire:
    def __str__(self):
        return 'Я огонь'
    def __add__(self, other):
        return Alchemy(part1=self, part2=other)
class Alchemy:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
    def __str__(self):
        return 'Игра Алхимик. Соединение двух элементов' + str(self.part1) + ' и ' + str(self.part2)




# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
