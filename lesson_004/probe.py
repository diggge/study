def simple():
    # Локальное пространство имен
    print('simple:', a + b)
    a = 9
    print('simple:', a + b)


# параметры - это локальные переменные
def simple_3(a, b):
    print('simple:', a + b)


a, b = 2, 2
print('global', a+b)
simple_3(a=3, b=4)