#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey',]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1,'bear')
print(zoo)



# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
zov=zoo + birds
#zoo.append(birds)
print(zov)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
zov.remove('elephant')
print(zov)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
print('Лев сидит в клетке № ',1+zov.index('lion'),'с левой стороны')
print('жаворонок сидит в клетке № ',1+zov.index('lark'),'с левой стороны')

