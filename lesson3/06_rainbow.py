# -*- coding: utf-8 -*-
# (цикл for)
import simple_draw as sd
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
sd.resolution = (500, 500)
# rainbow_start= sd.get_point(50,50)
# rainbow_end= sd.get_point(350, 450)
# rainbow_test= sd.get_point(50,50)+sd.get_point(50,50)
# print(rainbow_test)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# xx=0
# yy=0
# for _ in range(len(rainbow_colors)):
#     xx=xx+10
#     yy=yy-5
#     rainbow_start= sd.get_point(50+xx,50+yy)
#     rainbow_end = sd.get_point(350+xx, 450+yy)
#     sd.line(rainbow_start, rainbow_end, color=rainbow_colors[_], width=11)
    # rainbow_start=rainbow_start+sd.get_point(5,5)
#     # print(_, rainbow_colors[_])
#     # print(rad)
#     # sd.circle(sd.get_point(600, 600), radius=rad, color=rainbow_colors[_], width=4)
#     sd.line(rainbow_start,rainbow_end, color=rainbow_colors[_], width=4)

# sd.line(rainbow_start, rainbow_end, color=sd.random_color(), width=1)

# sd.circle(sd.get_point(50, 30), radius=50,color=sd.COLOR_RED, width=4)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
xx=0
yy=0
for _ in range(len(rainbow_colors)):
    xx = xx + 10
    yy=yy-5
    sd.circle(sd.get_point(250+xx,250+yy),radius=50,color=rainbow_colors[_],width=15)

sd.pause()
