# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код
class NotNameError(Exception):
    print('Ошибка в имени')
class NotEmailError(Exception):
    print('Ошибка в электронной почте')

def sorting(line):
    check = 0
    print(f'Обрабатываю строку {line}',flush = True)
    try:
        name, mail, age = line.split(' ')
        if (len(name)>=2 or len(mail)>=5 or len(age)>1):
            # print('Присутсвуют все три поля')
            check += 1
        else:
            # print('Присутствуют не все поля')
            check -= 1
        print(f'Имя = {name}, mail = {mail} , age = {age}')
    # print(f'Обрабатываю корректность имени {name}')
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)

        if name.isalpha() is False:
            # print(f'Данное имя {name} написано корректно')
            raise NotNameError
        else:
            # print(f'Данное имя {name} написано некорректно')
            check += 1
    # print(f'Обрабатываю корректность почты {mail}')
        k1=0
        k2=0
        for symbol in mail:
            # print(ord(symbol))
            if ord(symbol) == 64:
                k1 += 1
            if ord(symbol) == 46:
                k2 += 1
        if (k1 !=1 or k2 != 1):
            # print(f'Почта {mail} написано корректно')
            raise NotEmailError
        else:
            # print(f'Почта {mail} написано некорректно')
                check += 1

        if ((age.isdigit() is True) and (10 <= int(age) <=99)):
            # print(f'Возраст {age} прописан корректно {age.isdigit()}')
            check += 1
        else:
            # print(f' Возраст {age} прописан некорректно {age.isdigit()}')
            check -= 1
    except ValueError as exc1:
        print(f'Ошибка {exc1} в строке {line}')
        return 1
    except NotNameError:
        print(f'Ошибка в имени {name}')
        return 1
    except NotEmailError:
        print(f'Ошибка в электронной почте {mail}')
        return 1
    return check

with open('registrations.txt', 'r', encoding='utf8') as rs:
    with open('registrations_good.log', 'w',encoding='utf8') as good_rs:
        with open('registrations_bad.log', 'w', encoding='utf8') as bad_rs:
            for line in rs:
                line = line[:-1]
                check = sorting(line)
                line = line+'\n'
                if check == 4:
                    good_rs.write(line)
                    print(f'{line[:-1]} = Хорошая строка, записываю в registrations_good.log')

                else:
                    bad_rs.write(line)
                    print(f'{line[:-1]} = Плохая строка , записываю в registrations_bad.log ')

