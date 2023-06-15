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
def sorting(line,good_rs,bad_rs):
    check = 0
    print(f'Обрабатываю строку {line}',flush = True)
    try:
        name, mail, age = line.split(' ')
        if (len(name)<2 or len(mail)<=5 or len(age)<2):
            raise ValueError('Корректно не прописаны все три поля')

        print(f'Имя = {name}, mail = {mail} , age = {age}')
        if name.isalpha() is False:
            raise NotNameError('поле имени содержит НЕ только буквы')

        if mail.count('@') != 1 or mail[0] =='@' or mail.count('.') < 1 or mail.rfind('.')<mail.rfind('@'):
            raise NotEmailError('поле Емейл прописана некорректно')

        if ((age.isdigit() is False) or int(age) < 9 or int(age) > 99):
            raise ValueError('поле Возраст прописан некорректно')
        else:
            check += 1
    except ValueError as exc1:
        if 'unpack' in exc1.args[0]:
            print(f'Не прописаны все три значения в строке {line}')
            bad_rs.write(line + '  Не прописаны все три значения в строке  \n')
        if 'Корректно не прописаны все три поля' in exc1.args[0]:
            print(f'Корректно не прописаны все три поля {line}')
            bad_rs.write(line + '  :Корректно не прописаны все три поля  \n')
    except NotNameError:
        print(f'Ошибка в имени {name}')
        bad_rs.write(line + '  :поле имени содержит НЕ только буквы \n')
    except NotEmailError:
        print(f'Ошибка в электронной почте {mail}')
        bad_rs.write(line +f'  :поле емейл прописана некорректно\n')
    return check

with open('registrations.txt', 'r', encoding='utf8') as rs:
    with open('registrations_good.log', 'w',encoding='utf8') as good_rs:
        with open('registrations_bad.log', 'w', encoding='utf8') as bad_rs:
            for line in rs:
                line = line[:-1]
                check = sorting(line,good_rs,bad_rs)
                line = line+'\n'
                if check == 1:
                    good_rs.write(line)
                    print(f'{line[:-1]} = Хорошая строка, записываю в registrations_good.log')


