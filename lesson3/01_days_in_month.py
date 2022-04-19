# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом
# if <условие>:
#     <блок кода 1>
# elif <условие>:
#     <блок кода 2>
# elif <условие>:
#     <блок кода 3>
# else:
#     <блок кода 4>
# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
user_input = input("Введите, пожалуйста, номер месяца: ")
try:
    month = int(user_input)
    print('Вы ввели', month)
except ValueError:
    print('Ошибка, Вы вели не целое число')

month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

# TODO здесь ваш код
# if (month== 1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
i = -1
finded = 0
j = -1
while i < len(month_31) - 1:
    i += 1
    if month == month_31[i]:
        print('в месяце который вы вели, 31 дней')
        finded = 1
        break
if finded == 0:
    while j < len(month_30) - 1:
        j += 1
        if month == month_30[j]:
            print('в месяце который вы вели, 30 дней')
            finded = 1
            break
if finded == 0:
    if month == 2:
        print('в месяце который вы вели, 28 дней')
    else:
        print('Вы вели некорретный месяц')




# # if month == month_31
# #     print('в месяце который вы вели, 31 дней')
# elif (month== 4 or 6 or 9 or 11):
#     print('в месяце который вы вели, 30 дней')
# elif month== 2:
#     print('в месяце который вы вели, 28 дней')
# else:
#     print('Вы вели некорретный месяц')
