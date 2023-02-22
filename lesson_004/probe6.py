# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)
x1,y1 = sd.random_number(150,700), 600
while True:
    sd.start_drawing()
    sd.snowflake(center=sd.get_point(x1, y1), length=30, color=sd.COLOR_WHITE)
    y1 -= 5
    if y1 < 20:
        break
    x1 = x1+sd.random_number(-10,10)+5
    sd.finish_drawing()
    sd.sleep(0.04)
    if sd.user_want_exit():
        break


sd.pause()
