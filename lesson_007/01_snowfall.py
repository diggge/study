# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 630)
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self, number):
        self.number = number
        self.x = sd.random_number(0, 1100)
        self.y = sd.random_number(600, 650)
        self.length=sd.random_number(12, 17)
        self.factor_a=(sd.random_number(5, 9)) / 10
    def __str__(self):
        return 'Стежинка № - {}, координаты x,y {},{}, размер снежинки {}, фактор_а {}'.format(self.number, self.x, self.y,self.length,self.factor_a)
    def draw(self):
        sd.start_drawing()
        sd.snowflake(center=sd.get_point(self.x,self.y),length=self.length,color=sd.COLOR_WHITE,factor_a=self.factor_a)
        sd.finish_drawing()
        # print('Рисую  снежинку № {} c параметрами x={},y={},length={},factor_a={}'.format(self.number,self.x, self.y,self.length,self.factor_a))
    def move(self):
        self.x += sd.random_number(-5,5)+1
        self.y -= sd.random_number(0, 10)
        # print('Cместил снежинку № {} координату x={},координату y={}'.format(self.number, self.x, self.y))
    def clear_previous_picture(self):
        if self.number==19:
        # sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=sd.background_color, factor_a=self.factor_a)
            sd.clear_screen()
            print('Стираю нарисованные объекты')
    def can_fall(self):
        if self.y<10:
            self.x = sd.random_number(0, 1100)
            self.y=sd.random_number(600, 650)
            self.length = sd.random_number(10, 15)
            self.factor_a = (sd.random_number(1, 9)) / 10
# Одна снежинка
# flake = Snowflake(1)
# while True:
#     flake.clear_previous_picture()
#     flake.draw()
#     flake.move()
#     flake.can_fall()
#     # if not flake.can_fall():
#     #     break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# Много снежинок
flakes=[]
for N in range(20):
    flakes.append(Snowflake(N))
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        flake.can_fall()
    # if not flake.can_fall():
    #     break
        sd.sleep(0.001)
    if sd.user_want_exit():
        break


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
