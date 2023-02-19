# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок

# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)
spisok_sneshinok=[]
for i in range(1,21):
    spisok_sneshinok.append((sd.random_number(350,700), 600))
    print(spisok_sneshinok[i-1])
    while True:
        sd.clear_screen()
        x=spisok_sneshinok[i-1][0]
        y=spisok_sneshinok[i-1][1]
        print
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
