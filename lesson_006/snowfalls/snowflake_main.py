import simple_draw as sd
from snowflake_engine import create_snowflake, draw_snowflake, shift_snowflake, finish_snowflake, del_snowflake
sd.resolution = (1200, 630)
N=50
snowflake=create_snowflake(N)
# print(snowflake)
while True:
    count=0
    sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowflake(color=sd.background_color)
    #  сдвинуть_снежинки()
    shift_snowflake()
    #  нарисовать_снежинки_цветом(color)
    draw_snowflake(color=sd.COLOR_WHITE)
    #  если есть номера_достигших_низа_экрана() то удалить_снежинки(номера)
    finish_snowflake()
    count=del_snowflake()
    #       создать_снежинки(count)
    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break
sd.pause()
