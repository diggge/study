from house.wall import paint_wall
import simple_draw as sd
sd.start_drawing()
paint_wall(x0=100, y0=50, dlina_doma=300, shirina_brevna=25, kolichestvo_breven=8, color=sd.COLOR_DARK_ORANGE, width=3)
sd.finish_drawing()

