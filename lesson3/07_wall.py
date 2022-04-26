# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (800, 500)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
color = sd.random_color()
# TODO здесь ваш код

#     xx=xx+10
#     yy=yy-5
#     rainbow_start= sd.get_point(50+xx,50+yy)
#     rainbow_end = sd.get_point(350+xx, 450+yy)

# print(sd.resolution[0])
y1=1
for j in range(20):
    x1=sd.random_number(-130,0)
    x1=x1+30
    for i in range(10):
        sd.rectangle(sd.get_point(x1, y1), sd.get_point(x1 + 100, y1 + 50), color=sd.COLOR_ORANGE, width=2)
        x1 = x1 + 100
        if x1 > sd.resolution[0]:
            print(i)
            break
    y1 = y1 + 50
    if y1>sd.resolution[1]:
        break
sd.pause()
