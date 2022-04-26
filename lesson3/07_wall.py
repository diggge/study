# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (800, 500)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# TODO здесь ваш код
yk=sd.resolution[1]//50
yn=sd.resolution[0]//100
print(yk)
print(yn)
y1=1
for j in range(yk):
    x1=sd.random_number(-20,0)
    if j%2==0:
        x1=x1+50
    else:
        x1=x1
    for i in range(yn+1):
        sd.rectangle(sd.get_point(x1, y1), sd.get_point(x1 + 100, y1 + 50), color=sd.COLOR_ORANGE, width=1)
        x1 = x1 + 100
        if x1 > sd.resolution[0]:
            # print(i)
            break
    y1 = y1 + 50
    if y1>sd.resolution[1]:
        break
sd.pause()
