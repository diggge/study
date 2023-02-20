# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)
x1,y1 = sd.random_number(150,700), 600
x2,y2 = sd.random_number(150,400), 600
while True:
    sd.clear_screen()
# Начало i снежинки
    sd.snowflake(center=sd.get_point(x1, y1), length=30)
    y1 -= 5
    if y1 < 30:
        break
    x1 = x1+sd.random_number(-10,10)+5
#конец i снежинки
#начало i+1 снежинки
    sd.snowflake(center=sd.get_point(x2, y2), length=30)
    y2 -= 5
    if y2 < 30:
        break
    x2 = x2 ++sd.random_number(-30,30)+5
#конец i+1 снежинки
    sd.sleep(0.04)
    if sd.user_want_exit():
        break
# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
