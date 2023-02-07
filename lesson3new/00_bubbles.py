# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
# point=sd.get_point(300,200)
# radius=50
# for _ in range(100):
#     radius+=5
#     sd.circle(point,radius,width=2)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def bubble(point, step, kolichestvo_sharikov,color):
    radius = 50
    for _ in range(kolichestvo_sharikov):
        radius += step
        sd.circle(center_position=point, radius=radius,color=color,width=1)


# point = sd.get_point(300, 200)
# bubble(point, 5, 20)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
# for x in range(100,1001,100):
#     for y in range(100,301,100):
#         point=sd.get_point(x,y)
#         bubble(point,3,3)
# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point=sd.random_point()
    color=sd.random_color()
    step=random.randint(3,10)
    kolichestvo_sharikov=random.randint(1,15)
    bubble(point,step,kolichestvo_sharikov,color=color )
sd.pause()
