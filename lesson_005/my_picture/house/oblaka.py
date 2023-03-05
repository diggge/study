import simple_draw as sd
sd.resolution=(1800,900)
def oblaka(N,x0,x1,x2,x3,x4,y1,y2,y3,y4):
    for _ in range(N):
        x0+=sd.random_number(x1,x2)
        y0 = sd.random_number(y1, y2)
        sd.ellipse(sd.get_point(x0,y0),sd.get_point(x0+sd.random_number(x3,x4),sd.random_number(y3,y4)),color=sd.COLOR_WHITE,width=0)
