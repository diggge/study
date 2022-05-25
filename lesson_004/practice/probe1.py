# нарисовать треугольник из точки (300, 300) с длиной стороны 200
import simple_draw as sd
from simple_draw import Vector

length = 200
point = sd.get_point(300, 300)


# v1 = sd.get_vector(start_point=point,angle=0,length=200,width=3)
# v1.draw()
# v2 = sd.get_vector(start_point = v1.end_point,angle=120,length=200,width=3)
# v2.draw()
# v3 = sd.get_vector(start_point=point,angle=60,length=200,width=3)
# v3.draw()

# определить функцию рисования треугольника из заданной точки с заданным наклоном
def triangle(point, angle, length):
    v1: Vector = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=point, angle=angle + 60, length=length, width=3)
    v3.draw()

# triangle(point=sd.get_point(100, 100), angle=90, length=50)
for angle in range(0,361, 15):
    for length in range(0,301,50):
        triangle(sd.get_point(300, 300),angle=angle,length=length)
sd.pause()
