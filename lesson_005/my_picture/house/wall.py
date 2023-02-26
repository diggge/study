import simple_draw as sd
def paint_wall(x0,y0,quantity_x,quantity_y,color,width):
    for j in range(quantity_y+2):
        y0 = y0 + 50
        sd.line(sd.get_point(x0,y0),sd.get_point(x0+quantity_x,y0),color=color,width=width)
        sd.circle(sd.get_point(x0,y0+25),25,color=color,width=width)
        sd.circle(sd.get_point(x0+quantity_x, y0 + 25), 25, color=color, width=width)
        print(quantity_x,quantity_y)
paint_wall(x0=50,y0=50,quantity_x=300,quantity_y=5,color=sd.COLOR_DARK_ORANGE,width=2)
sd.pause()
