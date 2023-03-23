import simple_draw as sd
#  создать_снежинки(N) - создает N снежинок
def create_snowflake(N):
    global snowflake, x, y, length, factor_a
    x = []
    y = []
    length = []
    factor_a = []
    snowflake = []
    for i in range(N):
        x.append(sd.random_number(0, 1100))
        y.append(sd.random_number(600, 650))
        length.append(sd.random_number(10, 15))
        factor_a.append((sd.random_number(1, 9)) / 10)
        snowflake.append([i, x[i], y[i], length[i], factor_a[i]])
    return snowflake

#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
def draw_snowflake(color):
    j = 0
    while j < len(snowflake):
        sd.snowflake(center=sd.get_point(snowflake[j][1], snowflake[j][2]), length=snowflake[j][3],
                     factor_a=snowflake[j][4], color=color)
        j += 1

#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
def shift_snowflake():
    i = 0
    while i < len(snowflake):
        snowflake[i][1] = snowflake[i][1] + sd.random_number(-5, 5) + 1
        snowflake[i][2] = snowflake[i][2] - sd.random_number(0, 20)
        i += 1

#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
def finish_snowflake():
    global finish
    finish = []
    for i in snowflake:
        if i[2]<100:
            finish.append(i[0])

#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка+добавляет новые снежинки
def del_snowflake():
    finish.reverse()
    print(finish)
    count=0
    for i in finish:
        for j in snowflake:
            if j[0] == i:
                snowflake.remove(j)
                snowflake.append([i, x[i], y[i], length[i], factor_a[i]])


