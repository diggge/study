# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# def line(start_point, end_point, color=COLOR_YELLOW, width=1):
#     """
#         Нарисовать линию цветом color
#         Начиная с точки start
#         Заканчивая точкой end
# x0,y0,xf,yf=50,50,350,450
# for color in rainbow_colors:
#     x0+=5
#     xf+=5
#     sd.line(sd.get_point(x0,y0), sd.get_point(xf,yf), color=color, width=4)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
# def circle(center_position, radius=50, color=COLOR_YELLOW, width=1):
radius=400
step=30
for color in rainbow_colors:
    center_position=sd.get_point(250,-100)
    radius=radius+step
    sd.circle(center_position,radius,sd.random_color(),width=30)
sd.pause()
