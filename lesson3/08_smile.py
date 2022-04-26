# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
sd.resolution=(800,500)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
# TODO здесь ваш код
for i in range(10):
    x = sd.random_number(0, sd.resolution[0]-50)
    y = sd.random_number(0, sd.resolution[1]-70)
    color = sd.random_color()
    sd.ellipse(sd.get_point(x, y), sd.get_point(x + 130, y + 100), color=color, width=1)
    sd.circle(sd.get_point(x + 130 * 0.66, y + 100 * 0.65), radius=7, color=color, width=1)
    sd.circle(sd.get_point(x + 130 * 0.33, y + 100 * 0.65), radius=7, color=color, width=1)
    sd.lines([sd.get_point(x + 130 * 0.2, y + 100 * 0.4), sd.get_point(x + 130 * 0.3, y + 100 * 0.31),
    sd.get_point(x + 130 * 0.4, y + 100 * 0.28), sd.get_point(x + 130 * 0.5, y + 100 * 0.26),sd.get_point(x + 78, y + 100 * 0.28), sd.get_point(x + 91, y + 31), sd.get_point(x + 104, y + 40)], color=color, closed=False, width=1)
sd.pause()
