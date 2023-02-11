# -*- coding: utf-8 -*-
# (цикл for)
import simple_draw as sd
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# TODO здесь ваш код
# def rectangle(left_bottom, right_top, color=COLOR_YELLOW, width=0):
# sd.rectangle(sd.get_point(50,50),sd.get_point(600,600),sd.COLOR_RED,width=1)
y0=-50
quantity_x=sd.resolution[0]//100
quantity_y=sd.resolution[1]//50
print(quantity_x,quantity_y)
for j in range(quantity_y):
    y0 = y0 + 50
    if j % 2== 0:
        x0= 0
    else:
        x0=-50
    for i in range(quantity_x):
        sd.rectangle(sd.get_point(x0,y0),sd.get_point(x0+100,y0+50),sd.COLOR_ORANGE,width=1)
        x0, y0 = x0 + 100, y0
sd.pause()
