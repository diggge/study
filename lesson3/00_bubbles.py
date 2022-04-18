# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
# point = sd.get_point(400, 300)
# radius = 50
# for _ in range(3):
#     radius += 10
#     sd.circle(center_position=point, radius=radius,width=5)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
# def bubble(point,step):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# point = sd.get_point(400, 300)
# bubble(point=point,step=10)
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
def bubble(point,step,color):
    radius = 50
    for _ in range(10):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=3)
#
#
# for y in range(100, 301, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         bubble(point)




# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point=sd.random_point()
    color=sd.random_color()
    step=random.randint(2,30)
    bubble(point,step=step,color=color)
sd.pause()
