import simple_draw as sd
# radius = 400
# step = 30
# center_position = sd.get_point(250, -100)
def raduga(center_position,radius,step):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    for color in rainbow_colors:
        radius = radius + step
        sd.circle(center_position, radius, color, width=step)

