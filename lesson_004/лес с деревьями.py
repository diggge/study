import simple_draw as sd
sd.resolution = (1000, 900)
def draw_branches(point0,angle0,angle,length,width):
    if length<3:
        return
    v1 = sd.get_vector(start_point=point0,angle=angle0+angle,length=length,width=width)
    v2 = sd.get_vector(start_point=point0,angle=angle0-angle,length=length,width=width)
    v1.draw()
    v2.draw()
    x=sd.random_number(50,100)
    y=sd.random_number(80,120)
    length=length*0.8*x/100
    angle=angle*y/100
    width=width-2
    if width>1:
        draw_branches(point0=v1.end_point, angle0=angle0+angle, angle=angle, length=length, width=width)
        draw_branches(point0=v2.end_point, angle0=angle0-angle, angle=angle, length=length, width=width)
    else:
        draw_branches(point0=v1.end_point, angle0=angle0+angle,angle=angle,length=length,width=1)
        draw_branches(point0=v2.end_point, angle0=angle0-angle,angle=angle, length=length,width=1)
for _ in range(100):
    point_random=sd.random_point()
    v = sd.get_vector(start_point=point_random, angle=90, length=60, width=5)
    v.draw()
    point0=v.end_point
    draw_branches(point0=point0,angle0=90,angle=30,length=50,width=4)
sd.pause()
