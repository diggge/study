import simple_draw as sd
from snowflake_engine import create_snowflake, draw_snowflake, shift_snowflake, finish_snowflake, del_snowflake
sd.resolution = (1200, 630)
N=20
create_snowflake(N)
while True:
    sd.start_drawing()
    draw_snowflake(N, color=sd.COLOR_WHITE)


    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
