import simple_draw as sd
sd.resolution = (1000, 900)
def draw_branches(point0,angle0,angle,length,width):
    # print(point0,angle0,angle,length,width)
    v1 = sd.get_vector(start_point=point0,angle=angle0+angle,length=length,width=width)
    v2 = sd.get_vector(start_point=point0,angle=angle0-angle,length=length,width=width)
    if length<10:
        return
    else:
        v1.draw()
        v2.draw()
    while length>10:
         x=sd.random_number(70,100)
         y=sd.random_number(90,110)
         length=length*0.8*x/100
         angle=angle*y/100
         width=width-4
         print(x,y)
         if width>1:
             draw_branches(point0=v1.end_point, angle0=angle0+angle, angle=angle, length=length, width=width)
             draw_branches(point0=v2.end_point, angle0=angle0-angle, angle=angle, length=length, width=width)
         else:
             draw_branches(point0=v1.end_point, angle0=angle0+angle,angle=angle,length=length,width=1)
             draw_branches(point0=v2.end_point, angle0=angle0-angle,angle=angle, length=length,width=1)
    else:
        return
v = sd.get_vector(start_point=sd.get_point(500,30), angle=90, length=100, width=10)
v.draw()
point0=v.end_point
draw_branches(point0=point0,angle0=90,angle=30,length=150,width=7)
sd.pause()
