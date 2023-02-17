import simple_draw as sd
sd.resolution = (700, 800)
# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100
# sd.get_vector(point_0,90,100,width=3).draw()
def branch(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point
point_0 = sd.get_point(300, 5)
angle_0 = 90
length_0 = 200
next_angle = angle_0
next_length = length_0
next_point = point_0
while next_length > 1:
    next_point = branch(point=next_point, angle=next_angle, length=next_length)
    next_angle = next_angle - 30
    next_length = next_length * .75
sd.pause()
