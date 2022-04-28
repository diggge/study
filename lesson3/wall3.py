# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (150, 71.5)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# TODO здесь ваш код
yk=sd.resolution[1]//18.8
yn=sd.resolution[0]//39.0
kolichestvo=0
y1=0
for j in range(int(yk)+1):
    x1=0
    # x1=sd.random_number(-20,0)
    if j%2==0:
        x1=x1
    else:
        x1=x1+19.5
        kolichestvo=kolichestvo+1

    for i in range(int(yn)+2):
        kolichestvo = kolichestvo + 1
        sd.rectangle(sd.get_point(x1, y1), sd.get_point(x1 + 39, y1 + 18.8), color=sd.COLOR_ORANGE, width=1)
        x1 = x1 + 39

        if x1 > sd.resolution[0]:
            ostatok=round((x1-sd.resolution[0]),2)
            print( 'Остаток полублока с ряда №',j+1,'составляет',ostatok, 'Количество полублоков в сумме', kolichestvo)

            break
    y1 = y1 + 18.8
    if y1>sd.resolution[1]:
        break
# sd.take_snapshot(file_name='picture', path='E:\')
print('Количество полублоков=',kolichestvo)
sd.pause()
