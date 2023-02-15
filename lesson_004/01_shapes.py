# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# def triangle(point, angle, length, figure):
    # storony[]=None

# for i in range(figure):
#     print(i)
    # storony(i) == sd.get_point(100+i,100-i)
    # v[i]=sd.get_point(100+i,100-i)
    # v(i)=i
    # print(v(i))

    # v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    # v1.draw()
    # v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    # v2.draw()
    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    # v3.draw()
# for angle in range(0,361, 15):
#     for length in range(0,301,50):
# triangle(sd.get_point(300, 300),angle=0,length=200,figure=3)
# TODO здесь ваш код
def triangle(point, length, angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()
    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    # v3.draw()
    sd.line(v2.end_point, v1.start_point, width=3)
def kvadrat(point, length, angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()
    # v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    # v4.draw()
    sd.line(v3.end_point, v1.start_point, width=3)
def pyatiugolnik(point, length, angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw()
    # v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    # v5.draw()
    sd.line(v4.end_point, v1.start_point, width=3)
def shestiugolnik(point, length, angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw()
    # v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    # v6.draw()
    sd.line(v5.end_point, v1.start_point,width=3)
# x0,y0=sd.random_number(200,400),sd.random_number(100,500)
# point_0=sd.get_point(x0,y0)
# lengt_0=sd.random_number(50,150)
# angle_0=sd.random_number(0,360)
# x1,y1=sd.random_number(200,400),sd.random_number(100,500)
# point_1=sd.get_point(x1,y1)
# lengt_1=sd.random_number(50,150)
# angle_1=sd.random_number(0,360)
# x2,y2=sd.random_number(200,400),sd.random_number(100,500)
# point_2=sd.get_point(x2,y2)
# lengt_2=sd.random_number(50,150)
# angle_2=sd.random_number(0,360)
# x3,y3=sd.random_number(200,400),sd.random_number(100,500)
# point_3=sd.get_point(x3,y3)
# lengt_3=sd.random_number(50,150)
# angle_3=sd.random_number(0,360)
# triangle(point=point_0,length=lengt_0,angle=angle_0)
# kvadrat(point=point_1,length=lengt_1,angle=angle_1)
# pyatiugolnik(point=point_2,length=lengt_2,angle=angle_2)
# shestiugolnik(point=point_3,length=lengt_3,angle=angle_3)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
# n=5
# i=1
# vector1=sd.get_vector(start_point=sd.get_point(300,300), angle=30, length=100, width=3)
# next_vector=vector1
# next_angle=27
# vector1.draw()
# while i<n:
#     i = i + 1
#     next_angle=next_angle+360/n
#     print(i)
#     next_vector = sd.get_vector(start_point=next_vector.end_point, angle=next_angle, length=100, width=3)
#     print(next_vector)
#     next_vector.draw()

def figure(point,length,angle,chislo_storon):
    i,next_angle=1,angle
    next_vector=sd.get_vector(point,angle,length,3)
    vector1=next_vector
    next_vector.draw()
    while i<chislo_storon-1:
        i+=1
        next_angle+=360/chislo_storon
        next_vector=sd.get_vector(next_vector.end_point, next_angle, length, 3)
        next_vector.draw(color=sd.random_color())
    sd.line(next_vector.end_point, vector1.start_point, width=3)
print ('Введите координаты x0')
x0=int(input())
print ('Введите координаты y0')
y0=int(input())
print('Введите длину стороны фигуры')
length=int(input())
print('Введите угол наклона фигуры')
angle=int(input())
print('Введите количество сторон фигуры')
chislo_storon=int(input())
print(sd.get_point(x0,y0),length,angle)
figure(sd.get_point(x0,y0),length=length,angle=angle,chislo_storon=chislo_storon)
sd.pause()
