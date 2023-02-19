# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
import simple_draw as sd
sd.resolution = (1200, 600)
x=[]
y=[]
x[0]=x.append(sd.random_number(0,900))
for i in range(1,7):
    x[i]=x[i-1]+sd.random_number(0,100)
    x.append(sd.random_number(0,900))
    y.append(600)
print(x,y)
while True:
    sd.clear_screen()
    for j in range(7):
        point=sd.get_point(x[j],y[j])
        print(j,x[j], y[j], point)
        print(j,x[j], y[j], point)
        sd.snowflake(center=point, length=30)
        y[j] -= 5
        print('y=',y[j])
        x[j] = x[j] + sd.random_number(-10, 10) + 2
    if y[j] < 30:
        break

    sd.sleep(0.1)
    if sd.user_want_exit():
        break
# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
