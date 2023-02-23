# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинокf
import simple_draw as sd
sd.resolution = (1200, 600)
x=[]
y=[]
length=[]
factor_a=[]
while True:
    sd.start_drawing()
    for i in range(10):
        if i==0:
            x.append((sd.random_number(0, 100)))
            y.append(sd.random_number(600, 650))
        else:
            x.append(x[i-1]+sd.random_number(50, 150))
            y.append(y[i-1]+sd.random_number(-50, 50))
        length.append(sd.random_number(20,25))
        factor_a.append(sd.random_number(5, 8))
        point=sd.get_point(x[i],y[i])
        print(i,x[i], y[i], point,length[i])
        sd.snowflake(center=point, length=length[i],factor_a=factor_a[i]/10,color=sd.COLOR_WHITE)
        y[i] -= 2
        x[i] = x[i] + sd.random_number(-10, 10) + 2

    if y[i] < 0:
        break
    sd.sleep(0.01)
    if sd.user_want_exit():
        break
# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону
# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()fdsfsadfsadfsadf
sd.pause()
