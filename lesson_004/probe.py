# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)
x1,y1 = sd.random_number(350,700), 600
x2,y2 = sd.random_number(350,700), 600
while True:
    sd.clear_screen()
    point1 = sd.get_point(x1, y1)
    sd.snowflake(center=point1, length=30)
    y1 -= 5
    if y1 < 30:
        break
    x1 = x1+sd.random_number(-10,10)+5
    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=30)
    y2 -= 5
    if y2 < 30:
        break
    x2 = x2 + 5
    sd.sleep(0.04)
    if sd.user_want_exit():
        break
# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
