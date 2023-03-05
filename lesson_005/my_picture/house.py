from house.wall import paint_wall
from house.windows import paint_windows
from house.krysha import triangle
from trees import draw_branches
from rainbow import raduga
from sun import sun
from snegopad import snegopad
from house.oblaka import oblaka
import simple_draw as sd
sd.resolution=(1800,900)
sd.rectangle(sd.get_point(0,0),sd.get_point(1800,50),sd.COLOR_GREEN,width=0)
paint_wall(x0=600, y0=25, dlina_doma=300, shirina_brevna=20, kolichestvo_breven=11, color=sd.COLOR_DARK_ORANGE, width=3)
paint_windows((750,170),100,100)
triangle(sd.get_point(600,265),300/(2*sd.cos(45)),45)
#Лес
x0=sd.random_number(900,1000)
for _ in range(5):
    x0 = x0+sd.random_number(150, 180)
    y0 = sd.random_number(10, 50)
    v = sd.get_vector(start_point=sd.get_point(x0, y0), angle=90, length=110, width=8)
    v.draw(color=sd.COLOR_DARK_ORANGE)
    point0 = v.end_point
    draw_branches(point0=point0, angle0=90, angle=30, length=90, width=7,color=sd.COLOR_DARK_ORANGE)
#Облака
oblaka(100,-100,30,70,60,100,750,800,850,900)
#Радуга
raduga(sd.get_point(600,-200),1400,30)
#Солнце
sun(850,800,50,85)
#Снегопад
snegopad(quantity_snezhinok=10,v_vetra=-2,x_resolution=750,y_resolution=sd.resolution[1])
sd.pause()

