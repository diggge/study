# -*- coding: utf-8 -*-
import simple_draw as sd
x=[]
y=[]
sd.resolution = (1200, 600)
x[1] = sd.random_number(350,700)
y[1]=600
x[2] = sd.random_number(350,700)
y[2]=600
while True:
    sd.clear_screen()
    point1 = sd.get_point(x[1], y[1])
    sd.snowflake(center=point1, length=30)
    y[1] -= 5
    if y[1] < 30:
        break
    x[1] = x[1]+sd.random_number(-10,10)+5
    sd.snowflake(center=sd.get_point(x[2], y[2]), length=30)
    y[2] -= 5
    if y[2] < 30:
        break
    x[2] = x[2] + 5

    sd.sleep(0.04)
    if sd.user_want_exit():
        break