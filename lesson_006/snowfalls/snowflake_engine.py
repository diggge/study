import simple_draw as sd
#  создать_снежинки(N) - создает N снежинок
def create_snowflake(N):
    global snowflake,x,y,lengt,factor_a
    x = []
    y = []
    length = []
    factor_a = []
    snowflake=[]
    for i in range(N):
        if i==0:
            x.append(sd.random_number(0,50))
            y.append(sd.random_number(600,650))
        else:
            x.append(x[i - 1] + sd.random_number(50, 100))
            y.append(y[i - 1] + sd.random_number(-10, 10))
        length.append(sd.random_number(10,15))
        factor_a.append((sd.random_number(1,9))/10)
        snowflake.append([i, x[i], y[i], length[i], factor_a[i]])
    print(snowflake)
create_snowflake(20)
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
def draw_snowflake(N,color):
    for j in range(N):
        sd.snowflake(center=sd.get_point(snowflake[j][1],snowflake[j][2]),length=snowflake[j][3],factor_a=snowflake[j][4], color=color)
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
def shift_snowflake(N):
    print(x,y)
    for i in range(N):
        x[i]=x[i]+sd.random_number(-10,10)+10
        y[i]=y[i]-2
        print(x[i],y[i])
# shift_snowflake(20)
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
def finish_snowflake(N):
    global finish
    finish=[]
    for i in range(N):
        if y[i]<2:
            finish.append(i)
    print(finish)
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
def del_snowflake(N):
    for i in finish:
        














