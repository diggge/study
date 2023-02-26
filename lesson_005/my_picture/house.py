from house.wall import paint_wall
from house.windows import paint_windows
from house.krysha import triangle
import simple_draw as sd
sd.resolution=(1800,1000)
paint_wall(x0=600, y0=100, dlina_doma=300, shirina_brevna=20, kolichestvo_breven=11, color=sd.COLOR_DARK_ORANGE, width=3)
paint_windows((750,230),100,100)
triangle(sd.get_point(600,340),300/(2*sd.cos(45)),45)
sd.pause()

