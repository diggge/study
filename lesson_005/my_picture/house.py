from house.wall import paint_wall
from house.windows import paint_windows
from house.krysha import triangle
from trees import draw_branches
from rainbow import raduga
import simple_draw as sd
sd.resolution=(1800,1000)
paint_wall(x0=600, y0=100, dlina_doma=300, shirina_brevna=20, kolichestvo_breven=11, color=sd.COLOR_DARK_ORANGE, width=3)
paint_windows((750,230),100,100)
triangle(sd.get_point(600,340),300/(2*sd.cos(45)),45)
#Лес
for _ in range(5):
    x0 = sd.random_number(1000, 1700)
    y0 = sd.random_number(0, 400)
    v = sd.get_vector(start_point=sd.get_point(x0, y0), angle=90, length=90, width=7)
    v.draw(color=sd.COLOR_DARK_ORANGE)
    point0 = v.end_point
    draw_branches(point0=point0, angle0=90, angle=30, length=70, width=6,color=sd.COLOR_DARK_ORANGE)
#Радуга
raduga(sd.get_point(600,-200),1400,30)
sd.pause()

