# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
import simple_draw as sd
sd.resolution = (1200, 600)
x=[]
y=[]
while True:
    sd.clear_screen()
    for j in range(8):
        x.append(sd.random_number(0, 900))
        y.append(600)
        point=sd.get_point(x[j],y[j])
        print(j,x[j], y[j], point)
        sd.snowflake(center=point, length=30)
        y[j] -= 3
        # print('y=',y[j])
        x[j] = x[j] + sd.random_number(-5, 5)+2
    if y[j] < 30:
        break
    sd.sleep(0.05)
    if sd.user_want_exit():
        break
# реализовать падение одной снежинки из произвольного места экранаfdsd

# реализовать падение одной снежинки с ветром - смещение в сторонуf


sd.pause()
