# -*- coding: utf-8 -*-
# (определение функций)
import simple_draw as sd
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
# TODO здесь ваш код
# def ellipse(left_bottom, right_top, color=COLOR_YELLOW, width=0):
# def circle(center_position, radius=50, color=COLOR_YELLOW, width=1):
# def lines(point_list, color=COLOR_YELLOW, closed=False, width=1):
x0, y0 = sd.random_number(0, sd.resolution[0] - 8), sd.random_number(0, sd.resolution[1] - 5)
def smile(x0,y0,color):
    sd.ellipse(sd.get_point(x0,y0),sd.get_point(x0+100,y0+60),color,width=1)
    sd.circle(sd.get_point(x0+30,y0+37),7,color, width=1)
    sd.circle(sd.get_point(x0+70,y0+37),7,color, width=1)
    sd.lines([sd.get_point(x0+25,y0+20),sd.get_point(x0+40,y0+15),sd.get_point(x0+60,y0+15),sd.get_point(x0+75,y0+20)],color,False,width=1)
# smile(x0,y0,color=sd.COLOR_YELLOW)
for _ in range(30):
    color = sd.random_color()
    x0, y0 = sd.random_number(20, sd.resolution[0] - 20), sd.random_number(20, sd.resolution[1] - 20)
    print(color)
    smile(x0,y0,color)
sd.pause()
