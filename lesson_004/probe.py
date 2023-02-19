# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)
x = sd.random_number(350,1000)
y = 600
while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=30)
    y -= 5
    if y < 30:
        break
    x = x+sd.random_number(-10,10)+5
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
