import simple_draw as sd
sd.resolution = (1200, 600)
x = []
y = []
length = []
factor_a = []
y_resolution = [600] * 10
while True:
    sd.start_drawing()
    for i in range(10):
        if i == 0:
            x.append((sd.random_number(1, 50)))
            y.append(sd.random_number(400, 550))
        else:
            x.append(x[i - 1] + sd.random_number(50, 100))
            y.append(y[i - 1] + sd.random_number(-100, 100))
        length.append(sd.random_number(20, 25))
        factor_a.append(sd.random_number(5, 8))
        print(i, x[i], y[i], length[i], y_resolution[i])
        sd.snowflake(center=sd.get_point(x[i], y[i]), length=length[i], factor_a=factor_a[i] / 10, color=sd.background_color)
        y[i] -= sd.random_number(1, 13)
        x[i] = x[i] + sd.random_number(-10, 10) + 3
        sd.snowflake(center=sd.get_point(x[i], y[i]), length=length[i], factor_a=factor_a[i] / 10, color=sd.COLOR_WHITE)
        if y[i] < -y_resolution[i] + 600 + length[i]:
            y[i] = sd.random_number(600, 650)
            x[i] = sd.random_number(1, 1000)
            y_resolution[i] = y_resolution[i] - length[i] / 2
        sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()

