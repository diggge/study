import simple_draw as sd
def paint_wall(quantity_x,quantity_y,color,width):
    y0=-50
    for j in range(quantity_y):
        y0 = y0 + 50
        if j % 2== 0:
            x0= 0
        else:
            x0=-50
        for i in range(quantity_x):
            sd.rectangle(sd.get_point(x0,y0),sd.get_point(x0+100,y0+50),color=color,width=width)
            x0, y0 = x0 + 100, y0
quantity_x=sd.resolution[0]//100
quantity_y=sd.resolution[1]//50
paint_wall(quantity_x=sd.resolution[0]//100,quantity_y=sd.resolution[1]//50,color=sd.COLOR_ORANGE,width=1)
sd.pause()
