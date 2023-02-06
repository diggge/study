# -*- coding: utf-8 -*-

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
def bubble(point, step, kolichestvo_sharikov):
    radius = 50
    for _ in range(kolichestvo_sharikov):
        radius += step
        sd.circle(point, radius, width=3)


point = sd.get_point(300, 200)
bubble((100, 100), 3, 2)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()
