import simple_draw as sd
sd.resolution = (1000, 900)
def draw_branches(point0,angle0,angle,length,width):
    if length<3:
        return
    x1,x2,y1,y2 = sd.random_number(20, 100),sd.random_number(20, 100),sd.random_number(30, 130),sd.random_number(30, 130)
    v1 = sd.get_vector(start_point=point0,angle=angle0+angle*y1/100,length=length*x1/100,width=width)
    v2 = sd.get_vector(start_point=point0,angle=angle0-angle*y2/100,length=length*x2/100,width=width)
    v1.draw()
    v2.draw()
    length=length*0.72
    width=width-1
    if width>1:
        draw_branches(point0=v1.end_point, angle0=angle0+angle, angle=angle, length=length, width=width)
        draw_branches(point0=v2.end_point, angle0=angle0-angle, angle=angle, length=length, width=width)
    else:
        draw_branches(point0=v1.end_point, angle0=angle0+angle,angle=angle,length=length,width=1)
        draw_branches(point0=v2.end_point, angle0=angle0-angle,angle=angle, length=length,width=1)
for _ in range(30):
    x0=sd.random_number(50,950)
    y0=sd.random_number(0,750)
    v = sd.get_vector(start_point=sd.get_point(x0,y0), angle=90, length=60, width=5)
    v.draw()
    point0=v.end_point
    draw_branches(point0=point0,angle0=90,angle=30,length=50,width=4)
sd.pause()
