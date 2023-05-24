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
def sorting(line):
    check = 0
    print(f'Обрабатываю строку {line}',flush = True)
    name, mail, age = line.split(' ')
    # print(len(name),len(mail),len(age))
    if (len(name)>=2 or len(mail)>=5 or len(age)>1):
        # print('Присутсвуют все три поля')
        check += 1
    else:
        # print('Присутствуют не все поля')
        check -= 1
    print(f'Имя = {name}, mail = {mail} , age = {age}')
    # print(f'Обрабатываю корректность имени {name}')
    if name.isalpha() is True:
        # print(f'Данное имя {name} написано корректно')
        check += 1
    else:
        # print(f'Данное имя {name} написано некорректно')
        check -= 1
    # print(f'Обрабатываю корректность почты {mail}')
    k1=0
    k2=0
    for symbol in mail:
        # print(ord(symbol))
        if ord(symbol) == 64:
            k1 += 1
        if ord(symbol) == 46:
            k2 += 1
    if (k1 ==1 and k2 == 1):
        # print(f'Почта {mail} написано корректно')
        check += 1
    else:
        # print(f'Почта {mail} написано некорректно')
        check -= 1
    # print(f'Обрабатываю на корректность возраст {age}')
    if ((age.isdigit() is True) and (10 <= int(age) <=99)):
        # print(f'Возраст {age} прописан корректно {age.isdigit()}')
        check += 1
    else:
        # print(f' Возраст {age} прописан некорректно {age.isdigit()}')
        check -= 1
    return check

with open('registrations.txt', 'r', encoding='utf8') as rs:
    with open('registrations_good.log', 'a',encoding='utf8') as good_rs:
        with open('registrations_bad.log', 'a', encoding='utf8') as bad_rs:
            for line in rs:
                line = line[:-1]
                check=sorting(line)

                if check == 4:
                    print(f'Хорошая строка {line}')

                else:
                    print(f'Плохая строка {line}')
