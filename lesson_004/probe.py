import simple_draw as sd
sd.resolution = (1000, 900)
def draw_branches(point0,angle0,angle,length):
    print(point0,angle0,angle,round(length,1))
    v1 = sd.get_vector(start_point=point0,angle=angle0+angle,length=length,width=1)
    v2 = sd.get_vector(start_point=point0,angle=angle0-angle,length=length,width=1)
    if length<60:
        return
    else:
        v1.draw()
        v2.draw()
    while length>60:
         # print(v1.end_point,v2.end_point)
         length=length*0.7
         draw_branches(point0=v1.end_point, angle0=angle0+angle,angle=angle,length=length)
         draw_branches(point0=v2.end_point, angle0=angle0-angle,angle=angle, length=length)
    else:
        return
v = sd.get_vector(start_point=sd.get_point(500,30), angle=90, length=200, width=1)
v.draw()
point0=v.end_point
draw_branches(point0=point0,angle0=90,angle=30,length=200)
sd.pause()
