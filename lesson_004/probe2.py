# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
#     point2 = sd.get_point(x2, y2)
#     sd.snowflake(center=point2, length=30)
#     y2 -= 5
#     if y2 < 30:
#         break
#     x2 = x2 + 5
# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)
spisok_sneshinok=[]
for i in range(1,3):
    spisok_sneshinok.append((sd.random_number(350, 700), 600))
print(spisok_sneshinok)
# for i in range(3):
#         x=spisok_sneshinok[i][0]
#         y=spisok_sneshinok[i][1]
#         point=sd.get_point(x,y)
#         print(x,y,point)
while True:
    sd.clear_screen()
    for j in range(1,3):
        x=spisok_sneshinok[j-1][0]
        y=spisok_sneshinok[j-1][1]
        point=sd.get_point(x,y)
        print(j,x,y,point)
        sd.snowflake(center=point, length=30)
        y -= 5
        if y < 30:
            break
        x = x+sd.random_number(-10,10)+5

        sd.sleep(0.01)
        if sd.user_want_exit():
            break
# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
