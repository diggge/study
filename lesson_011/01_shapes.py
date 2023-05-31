# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.

# def figure(point,length,angle,chislo_storon):
#     i,next_angle=1,angle
#     vector1=sd.get_vector(point,angle,length,3)
#     next_vector = vector1
#     vector1.draw()
#     while i < chislo_storon-1:
#         i += 1
#         next_angle += 360/chislo_storon
#         next_vector = sd.get_vector(next_vector.end_point, next_angle, length, 3)
#         next_vector.draw(color=sd.random_color())
#     sd.line(next_vector.end_point, vector1.start_point, width=3)

sd.resolution = (1000, 900)
def get_polygon(n):
    def polygon(point,length,angle):
        i, next_angle = 1, angle
        vector1 = sd.get_vector(point, angle, length, 3)
        next_vector = vector1
        vector1.draw(color=sd.COLOR_BLACK)
        while i < n-1:
            i += 1
            next_angle += 360/(n)
            next_vector = sd.get_vector(next_vector.end_point, next_angle, length, 3)
            next_vector.draw(color=sd.random_color())
        sd.line(next_vector.end_point, vector1.start_point, width=3)
    return polygon

    # TODO здесь ваш код


draw_triangle = get_polygon(n=27)
draw_triangle(point=sd.get_point(450, 150), angle=13, length=80)
# figure(point=sd.get_point(200, 200),length=100,angle=13,chislo_storon=6)

sd.pause()
