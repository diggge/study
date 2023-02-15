# -*- coding: utf-8 -*-
import simple_draw as sd
import pprint

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
def figure(point,length,angle,chislo_storon,svet):
    i,next_angle=1,angle
    next_vector=sd.get_vector(point,angle,length,3)
    vector1=next_vector
    next_vector.draw(color=svet)
    while i<chislo_storon-1:
        i+=1
        next_angle+=360/chislo_storon
        next_vector=sd.get_vector(next_vector.end_point, next_angle, length, 3)
        next_vector.draw(color=svet)
    sd.line(next_vector.end_point, vector1.start_point, color=svet, width=3)
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
sveta_dict={1:sd.COLOR_RED,2:sd.COLOR_ORANGE,3:sd.COLOR_YELLOW,4:sd.COLOR_GREEN,5:sd.COLOR_CYAN,6:sd.COLOR_BLUE,7:sd.COLOR_PURPLE}
print("Введите, пожалуйста, номер цвета: 1:Красный,2:Оранжевый,3:Желтый,4:Зеленый,5:голубой,6:синий,7:фиолетовый")
svet = int(input())
print(sd.get_point(x0,y0),length,angle)
figure(sd.get_point(x0,y0),length=length,angle=angle,chislo_storon=chislo_storon,svet=sveta_dict[svet])
sd.pause()


