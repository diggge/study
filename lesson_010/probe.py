a, b = 1, 1
try:
    print(a/b)
    print("Это не будет напечатано")
    print('10'+10)
except TypeError:
    print("Вы сложили значения несовместимых типов")
except ZeroDivisionError:
    print("Деление на 0")