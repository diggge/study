import simple_draw as sd
sd.resolution = (1000, 900)
# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви
def draw_branches(point0,angle0,angle,length,width):
    print(next_point1,length,width)
    v1 =sd.get_vector(start_point=point0,angle=angle0+angle,length=length*0.75,width=width)
    v2 = sd.get_vector(start_point=point0, angle=angle0 - angle, length=length * 0.75, width=width)
    if length<10:
        return
    else :
        v1.draw()
        v2.draw()
    while length>10:
         print(v1.end_point,v2.end_point)
         length=length*0.7
         width=width-4
         if width>1:
             draw_branches(point0=v1.end_point, angle0=angle0+angle, angle=angle, length=length, width=width)
             draw_branches(point0=v2.end_point, angle0=angle0-angle, angle=angle, length=length, width=width)
         else:
             draw_branches(point0=v1.end_point, angle0=angle0+angle,angle=angle,length=length,width=1)
             draw_branches(point0=v2.end_point, angle0=angle0-angle,angle=angle, length=length,width=1)
    else:
        return
v = sd.get_vector(start_point=sd.get_point(500,50), angle=90, length=200, width=20)
v.draw()
next_point1=v.end_point
point0=v.end_point
angle0=90
# angle1=90
# angle2=90
# print(next_point1,next_point2)
draw_branches(point0=point0,angle0=90,angle=30,length=200,width=17)
sd.pause()
