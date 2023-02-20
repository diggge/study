# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)
x1,y1 = sd.random_number(150,700), 600
while True:
    # sd.clear_screen()
    sd.background_color
    sd.start_drawing()
    sd.snowflake(center=sd.get_point(x1, y1), length=30)
    y1 -= 5
    if y1 < 30:
        break
    x1 = x1+sd.random_number(-10,10)+5
    sd.sleep(0.04)
    if sd.user_want_exit():
        break
sd.pause()
# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()