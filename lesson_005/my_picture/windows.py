import simple_draw as sd
sd.resolution = (1000, 900)
print(sd.resolution[0])
def paint_windows(center_position,length_x,length_y):
    sd.rectangle(sd.get_point(center_position[0]-length_x/2,center_position[1]-length_y/2),sd.get_point(center_position[0],center_position[1]+length_y/2),color=sd.COLOR_WHITE,width=1)
    sd.rectangle(sd.get_point(center_position[0],center_position[1]-length_y/2),sd.get_point(center_position[0]+length_x/2,center_position[1]+length_y/2),color=sd.COLOR_WHITE,width=1)
paint_windows((300,300),100,100)
sd.pause()