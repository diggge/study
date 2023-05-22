 # -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам:')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError as v_error:
    print(f"Введенное число - это не число или не одно число : {v_error}")
except IndexError as i_error:
    print(f"Введенном число не пятизначное!: {i_error}")
except:
    print('Ошибка остальное, нужно прочитать логи!')
finally:
    print('Выхожу с программы')




# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение


