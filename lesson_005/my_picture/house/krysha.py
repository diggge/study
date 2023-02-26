import simple_draw as sd
print(sd.resolution[0])
def triangle(point, length, angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(sd.COLOR_DARK_ORANGE)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 270, length=length, width=3)
    v2.draw(sd.COLOR_DARK_ORANGE)
    sd.line(v2.end_point, v1.start_point, width=3,color=sd.COLOR_DARK_ORANGE)
# triangle(sd.get_point(300,300),90,30)
# sd.pause()