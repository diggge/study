import simple_draw as sd
def paint_wall(x0, y0, dlina_doma, kolichestvo_breven, shirina_brevna, color, width):
    for j in range(kolichestvo_breven):
        y0 = y0 + shirina_brevna
        sd.line(sd.get_point(x0,y0), sd.get_point(x0 + dlina_doma, y0), color=color, width=width)
        sd.circle(sd.get_point(x0,y0+shirina_brevna/2),shirina_brevna/2,color=color,width=width)
        sd.circle(sd.get_point(x0 + dlina_doma, y0 + shirina_brevna/2), shirina_brevna/2, color=color, width=width)
        # if _auto_flip:
        #     pygame.display.flip()
# paint_wall(x0=100,y0=50,dlina_doma=300,shirina_brevna=25,kolichestvo_breven=9,color=sd.COLOR_DARK_ORANGE,width=2,)

