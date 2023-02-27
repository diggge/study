import simple_draw as sd
def sun(x0,y0,radius,length):
    sd.circle(sd.get_point(x0,y0),radius=radius,color=sd.COLOR_YELLOW,width=0)
    angle=360/16
    for j in range(16):
        angle=angle+360/16
        if j % 2 == 0:
            length = 85
        else:
            length = 75
        v=sd.get_vector(sd.get_point(x0,y0),angle=angle,length=length,width=3)
        v.draw()


