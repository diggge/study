# -*- coding: utf-8 -*-
from random import randint
# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777

# TODO здесь ваш код

# https://goo.gl/JnsDqu
def one_day():
    dice = randint(1,13)
    karma = randint(1,7)
    if dice ==1:
        try:
            raise NameError('Ошибка: Я - бог')
        except NameError as IamGodError:
            print(f'Поймано исключение {IamGodError},{type(IamGodError)}  | параметры {IamGodError.args}')
    if dice ==2:
        try:
            raise NameError('Ошибка: я - выпил')
        except NameError as DrunkError:
            print(f'Поймано исключение {DrunkError},{type(DrunkError)}  | параметры {DrunkError.args}')
    if dice ==3:
        try:
            raise NameError('Ошибка - сломалась машина')
        except NameError as CarCrashError:
            print(f'Поймано исключение {CarCrashError},{type(CarCrashError)}  | параметры {CarCrashError.args}')
    if dice ==4:
        try:
            raise NameError('Ошибка - я обжора')
        except NameError as GluttonyError:
            print(f'Поймано исключение {GluttonyError},{type(GluttonyError)}  | параметры {GluttonyError.args}')
    if dice ==5:
        try:
            raise NameError('Ошибка - Депрессия')
        except NameError as DepressionError:
            print(f'Поймано исключение {DepressionError},{type(DepressionError)}  | параметры {DepressionError.args}')
    if dice ==6:
        try:
            raise NameError('Ошибка - Жесткая депрессия')
        except NameError as SuicideError:
            print(f'Поймано исключение {SuicideError},{type(SuicideError)}  | параметры {SuicideError.args}')
    return karma
total_karma = 0
while True:
    print(f'Новый день сурка! Текущая карма = {total_karma}')
    if total_karma <= ENLIGHTENMENT_CARMA_LEVEL:
        total_karma += one_day()
    else:
        print("Мы достигли нужной кармы, выход из дня сурка")
        break




