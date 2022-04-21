# -*- coding: utf-8 -*-
# Есть словарь кодов товаров
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
# Есть словарь списков количества товаров на складе.
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
for i in goods:
#     # print(goods[i])
    for j in store:
        if goods[i]==j:
            wtuk=0
            sena=0
            for k in store[j]:
                wtuk=wtuk+k['quantity']
                sena=sena+k['quantity']*k['price']
            print('На складе лежит товара:',i , 'в количестве',wtuk, 'штук с общей суммой',sena, 'рублей')
            # print(d[0]['quantity'])
            # for k in j:
            #     print(store[j])
            # print(store[j][0]['quantity'])






 # zoo_pet_mass = {
 #                'lion': 300,
 #                'skunk': 5,
 #                'elephant': 5000,
 #                'horse': 400,
 #            }
 #            total_mass = 0
 #            for animal in zoo_pet_mass:
 #                print(animal, zoo_pet_mass[animal])
 #                total_mass += zoo_pet_mass[animal]
            # print(d)
    # print(goods[i])

# Рассчитать на какую сумму лежит каждого товара на складе.
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
# Алгоритм должен получиться приблизительно такой:
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

# TODO здесь ваш код


# i=0
# for i in store:
#     print(i,store[i])



# print(goods.items('12345'))
# print(store['12345'])




