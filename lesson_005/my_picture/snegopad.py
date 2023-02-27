import simple_draw as sd
sd.resolution=(1800,900)
def snegopad(quantity_snezhinok, v_vetra,  x_resolution,y_resolution):
    x = []
    y = []
    length = []
    factor_a = []
    h_snezhinok = [y_resolution+50] * quantity_snezhinok
    while True:
        sd.start_drawing()
        for i in range(quantity_snezhinok):
            if i == 0:
                x.append((sd.random_number(1, 50)))
                y.append(sd.random_number(y_resolution, y_resolution+100))
            else:
                x.append(x[i - 1] + sd.random_number(50, 100))
                y.append(y[i - 1] + sd.random_number(-100, 100))
            length.append(sd.random_number(20, 25))
            factor_a.append(sd.random_number(5, 8))
            sd.snowflake(center=sd.get_point(x[i], y[i]), length=length[i], factor_a=factor_a[i] / 10, color=sd.background_color)
            y[i] -= sd.random_number(1, 13)
            x[i] = x[i] + sd.random_number(-10, 10) + v_vetra
            sd.snowflake(center=sd.get_point(x[i], y[i]), length=length[i], factor_a=factor_a[i] / 10, color=sd.COLOR_WHITE)
            if y[i] < -h_snezhinok[i] + y_resolution + length[i]+50:
                y[i] = sd.random_number(y_resolution, y_resolution+50)
                x[i] = sd.random_number(1, x_resolution-100)
                h_snezhinok[i] = h_snezhinok[i] - length[i] / 4
            sd.finish_drawing()
            sd.sleep(0.01)
            if sd.user_want_exit():
                break
# snegopad(quantity_snezhinok=10,v_vetra=2,x_resolution=sd.resolution[0],y_resolution=sd.resolution[1])
# sd.pause()

